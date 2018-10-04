import requests
from requests_ntlm import HttpNtlmAuth

username = 'CYBERINDIA\\akshita.kukreja'
password = 'Akshita@30'
tfsApi = 'http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1'
MY_TOKEN = 'NTLM TlRMTVNTUAADAAAAGAAYAJQAAAAYABgArAAAABQAFABIAAAAOAA4AFwAAAAAAAAAlAAAAAAAAADEAAAABYKIogUBKAoAAAAPQwBZAEIARQBSAEkATgBEAEkAQQBDAFkAQgBFAFIARwBJAE4ARABJAEEAXABcAGEAawBzAGgAaQB0AGEALgBrAHUAawByAGUAagBhAP+X9OqBfHuEAAAAAAAAAAAAAAAAAAAAAFp/8VBGy4cRbjkj+A/9jtbc/nJEuLLhgg=='

# session = requests.Session()
# session.auth = HttpNtlmAuth(username,password)
# response=session.get(tfsApi)
# response = requests.get(tfsApi,auth=HttpNtlmAuth(username,password))
# print(HttpNtlmAuth(username,password))
# print(response)


r = requests.get(tfsApi, headers={'Authorization': 'TOK:<MY_TOKEN>'})
print(r)









# POST https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/${type}?api-version=4.1
# http://cyg249:8080/tfs/defaultcollection/akshitaK/_apis/wit/workitems/$task?api-version=4


# GET https://dev.azure.com/{organization}/{project}/_apis/wit/workitems/{id}?api-version=4.1\
# http://cyg249:8080/tfs/defaultcollection/_apis/wit/workitems/1
#application/json-patch+json

# import requests
# from requests_ntlm import HttpNtlmAuth

# requests.get("http://ntlm_protected_site.com",auth=HttpNtlmAuth('domain\\username','password'))



