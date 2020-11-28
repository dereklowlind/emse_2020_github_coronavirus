import requests
import json
url = "https://api.github.com/search/repositories?q=language:java&sort=stars&created:<2019-01-01&pushed:>2019-01-01&order=deschttps://api.github.com/repos/elastic/elasticsearch/branches?&per_page=100"

payload={}
headers = {}

first_hundred = requests.request("GET", url+'&page=1', headers=headers, data=payload)
second_hundred = requests.request("GET", url+'&page=2', headers=headers, data=payload)
third_hundred = requests.request("GET", url+'&page=3', headers=headers, data=payload)

print(first_hundred.text)
print(second_hundred.text)
print(third_hundred.text)