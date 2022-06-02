import json
import time
import requests
import logging
from sagemaker.s3 import S3Downloader

logger = logging.getLogger()
logging.basicConfig(level=logging.INFO)

def wait_for_sentiment_result(req_id):
    get_url = 'http://localhost:8081/get_sentiment_status/' + req_id
    get_result = requests.get(get_url)
    status = json.loads(get_result.text).get("result")


    while (status not in [['FINISHED'], ['FAILED']]):
        logger.info(f'Sentiment status: {status}')
        time.sleep(30)
        get_result = requests.get(get_url)
        status = json.loads(get_result.text).get("result")
    if status == ['FINISHED']:
        logger.info(f'Sentiment status: {status}')
        return True
    else:
        return False

def download_file_from_s3(req_id, target_file_path):
    s3_path = 's3://sentiment-data-input/input/'
    S3Downloader.download(s3_path + req_id, target_file_path)

def call_sentiment_analysis(request_path):

    config = {"added_params": {"third_party_sentiment_service": "sagemaker",
    "third_party_params": {
            "model_path" : "s3://signals-research-data/sentiment/models/roberta-base/pytorch_model.tar.gz",
            "label_map" : {"LABEL_0": "Negative", "LABEL_1": "Neutral", "LABEL_2": "Positive", "LABEL_3": "Mixed" },
            "id": "OnlineStatement_ID",
            "prediction_column": "Sentiment"
        },"data_criteria": {"Solution Type": {"values": ["All"
                    ]
                }, "Source Type": {"values": ["All"
                    ]
                }, "Channel": {"values": ["All"
                    ]
                }
            }
        }
    }



    # api-endpoint
    URL = "http://localhost:8081/run_sentiment"
    data = {
        'request_path': request_path,
        'entities': [],
        'configuration': config,
        'internal_configuration': {},
        'input_kip':  {},
        'output_kip': {}
    }


    result = requests.post(URL, json=data, headers={"Content-Type": "application/json", "Accept": "application/json"})

    req_id = json.loads(result.text).get("request_id")

    sentiment_result = wait_for_sentiment_result(req_id)
    if (sentiment_result == True):
        logger.info('Download output file from S3 to ' + request_path)
        download_file_from_s3(req_id, request_path)
        return [req_id + '.json.out']

