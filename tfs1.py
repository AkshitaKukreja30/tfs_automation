import requests
# from requests_ntlm import HttpNtlmAuth
from requests.auth import HTTPBasicAuth
from requests.auth import HTTPDigestAuth
username = 'akshita.kukreja'
password = 'Akshita@30'
# tfsApi = 'http://cyg249:8080/tfs/DefaultCollection/akshitaK/_apis/wit/workitems/1/basic-auth/'+username+'/'+password
tfsApi = 'http://cyg249:8080/tfs/DefaultCollection/akshitaK/_apis/wit/workitems/1'
import urllib
response = urllib.request.urlopen(
urllib.request(tfsApi, headers={'Authorization': 'NTLM TlRMTVNTUAADAAAAGAAYAJQAAAAYABgArAAAABQAFABIAAAAOAA4AFwAAAAAAAAAlAAAAAAAAADEAAAABYKIogUBKAoAAAAPQwBZAEIARQBSAEkATgBEAEkAQQBDAFkAQgBFAFIARwBJAE4ARABJAEEAXABcAGEAawBzAGgAaQB0AGEALgBrAHUAawByAGUAagBhAP+X9OqBfHuEAAAAAAAAAAAAAAAAAAAAAFp/8VBGy4cRbjkj+A/9jtbc/nJEuLLhgg=='}))
print(response)
#conv_auth=(username,password)
#response = requests.get(tfsApi,auth=conv_auth)
#response = requests.get(tfsApi,auth=HTTPDigestAuth(username,password))
# response = requests.get(tfsApi,auth=HTTPBasicAuth(username, password))
# print(response)
# # if(tfsResponse.ok):
#     tfsResponse = tfsResponse.json()
#     print(tfsResponse)
# else:
#     tfsResponse.raise_for_status()
 # from requests.auth import HTTPDigestAuth
 # url = 'http://httpbin.org/digest-auth/auth/user/pass'
 # requests.get(url, auth=HTTPDigestAuth('user', 'pass'))
# response = requests.get(tfsApi, headers={'Authorization': 'khzkfwmlmibnpqbmsbw2wd3xxlc6miwgo4yw6y2d24lotorn225q'})
# print(response)
# myToken = 'khzkfwmlmibnpqbmsbw2wd3xxlc6miwgo4yw6y2d24lotorn225q'
# myUrl = tfsApi
# head = {'Authorization': 'token {}'.format(myToken)}
# response = requests.get(myUrl, headers=head)
# print(response)
# import json
# import urllib3
# from pybase64 import base64
# from base64 import encode
 
 
# http = urllib3.PoolManager()
 
# # hash_string = base64.b64encode(f"{username}:{password}")
# hash_string = base64.b64encode(password.encode("utf-8"))
# headers = {
# "Authorization": f"Basic {hash_string}"
# }
 
# # Make your request
# response = http.request("GET", tfsApi, headers=headers)
# # Convert JSON to dict
# # response_data = json.loads(response.data.decode("utf-8"))
# # response_data = json.loads(response.data.decode("utf-8"))
# print(response)

