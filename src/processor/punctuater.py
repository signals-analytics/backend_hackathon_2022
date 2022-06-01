import requests
from requests.structures import CaseInsensitiveDict

url = 'http://bark.phon.ioc.ee/punctuator'

headers = CaseInsensitiveDict()
headers["Content-Type"] = "application/json"

data = "text=hello world what is the status have a good day and nice cookie what a wonderful world"

resp = requests.post(url, headers=headers, data=data)

print(resp.status_code)


#curl -d "text=hello%20world" http://bark.phon.ioc.ee/punctuator



