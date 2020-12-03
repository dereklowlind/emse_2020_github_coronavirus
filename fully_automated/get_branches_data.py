import requests
import json
url = "https://api.github.com/repos/elastic/elasticsearch/branches?&per_page=20&page="

payload={}
headers = {}

branches = []
response = requests.request("GET", url+'1', headers=headers, data=payload)
i = 2
while len(response.text) > 2 : # length is 2 when response text is empty []
    branches.extend(response)
    response = requests.request("GET", url+str(i), headers=headers, data=payload)
    i += 1
    print(response.text)
    print(len(response.text))

print(branches)
