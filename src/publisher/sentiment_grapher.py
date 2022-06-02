import csv
import json
import logging
import os
from enum import Enum

logger = logging.getLogger()

class SentimentEnum(Enum):
    Negative = -1
    Neutral = 0
    Positive = 1

SENTIMENT_LABELS = {
    "LABEL_0": SentimentEnum.Negative,
    "LABEL_1": SentimentEnum.Neutral,
    "LABEL_2": SentimentEnum.Positive
}

class Sentiment:
    def __init__(self, negative, neutral, positive):
        self.negative=negative
        self.neutral=neutral
        self.positive=positive

    def calc_sentiment(self):
        max_val = max(self.neutral, self.positive, self.negative)

        if max_val==self.positive:
            return SentimentEnum.Positive
        if max_val==self.negative:
            return SentimentEnum.Negative

        return SentimentEnum.Neutral



def parse_sentiment_json_label(label):
    pass


def generate_sentiment_output_graph(sentiment_output_files, output_path):
    logger.warn("Going to generate sentiment output graphs for : " + str(sentiment_output_files))
    logger.info("PATH=" + os.getcwd())

    # TBD!!
    # sentiment_output_files = ['../publisher/sentiment_output_example.json']
    sentiment_output_files = ['../publisher/transcript_video_wTXmkn6B7dI&lc.json.out']

    for sentiment_output_file in sentiment_output_files:
        csv_output_path = os.path.join(output_path, "csv_output")
        os.makedirs(csv_output_path, exist_ok=True)
        csv_output_file_path = os.path.join(csv_output_path, os.path.basename(sentiment_output_file)+".csv")
        with open(csv_output_file_path, "w") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['id', 'sentiment'])
            logger.info("Going to write csv output: " + csv_output_file_path)
            with open(sentiment_output_file) as json_file:
                output_json = json.load(json_file)
            for json_data_point in output_json:
                dp_id = json_data_point['OnlineStatement_ID']
                labels = json_data_point['SageMakerOutput'][0]
                dp_sentiments = {SENTIMENT_LABELS[label['label']]:label['score'] for label in labels}
                sentiment_val = Sentiment(
                    negative=dp_sentiments[SentimentEnum.Negative],
                    positive=dp_sentiments[SentimentEnum.Positive],
                    neutral=dp_sentiments[SentimentEnum.Neutral]
                ).calc_sentiment()
                csv_sentiment_row = [dp_id, sentiment_val.value]
                csv_writer.writerow(csv_sentiment_row)
