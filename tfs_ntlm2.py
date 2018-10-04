import requests
from requests_ntlm import HttpNtlmAuth

url = "http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1"
session = requests.Session()
session.auth = HttpNtlmAuth('akshita.kukreja', 'Akshita@30')
res=session.get(url)
print(res)