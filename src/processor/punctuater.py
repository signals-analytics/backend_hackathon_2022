import requests
from requests.structures import CaseInsensitiveDict


def punctuate_text(text):
    PUNCTUATOR_URL = 'http://bark.phon.ioc.ee/punctuator'

    headers = CaseInsensitiveDict()
    headers["Content-Type"] = "application/json"
    PARAMS = {'text': text}

    # sending get request and saving the response as response object
    resp = requests.post(url=PUNCTUATOR_URL, headers=headers, params=PARAMS)

    response_punctuated_text = str(resp.content)
    response_punctuated_text = response_punctuated_text.replace("b'", "")

    print(resp.status_code)
    return response_punctuated_text

#curl -d "text=hello%20world" http://bark.phon.ioc.ee/punctuator


if __name__ == "__main__":
    text = "hello world what is the status have a good day and nice cookie what a wonderful world"
    punctuated_text_result = punctuate_text(text)
    print(punctuated_text_result)
