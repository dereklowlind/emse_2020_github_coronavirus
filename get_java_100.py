import requests

url = "https://api.github.com/search/repositories?q=language:java&sort=stars&created:<2019-01-01&pushed:>2019-01-01&order=desc"

payload={}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)