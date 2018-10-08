import requests
import json
# url = 'https://tfsweb.justenergy.com/tfs/fr_TX/_apis/wit/workitems/21125'
url = 'https://tfsweb.justenergy.com/tfs/fr_TX/ALL_SUPPORT/_apis/wit/workitems/$Support%20Request'
headers = {'Content-Type':'application/json-patch+json','Accept':'application/json;api-version=1.0'}
d = [
  {
    "op": "add",
    "path": "/fields/System.Title",
    "value": "Working perfectly"
  },
  {
    "op": "add",
    "path": "/fields/System.Description",
    "value": "This is the description"
  },
   {
    "op": "add",
    "path": "/fields/System.AssignedTo",
    "value": "Akshita Kukreja"
  },{
    "op": "add",
    "path": "/fields/System.IterationPath",
    "value": "ALL_SUPPORT\\2018 - October 01st to October 05th"
  },
  {
    "op": "add",
    "path": "/fields/Hudson.TFS.Organization",
    "value": "Customer Service"
  }

 
]
data= json.dumps(d)
res = requests.post(url = url, data = data , headers = headers ,auth=('akukreja', 'Summer2018')).json()
print(res['url'])
# r=requests.get(url,auth=HttpNtlmAuth('akshita.kukreja',
# 'Akshita@30'))
# print (r.status_code)
# print (r.text)

# patch
# http://cyg249:8080/tfs/defaultcollection/_apis/wit/workitems/162

# [
#    {
#     "op": "add",
#     "path": "/relations/-",
#     "value": {
#       "rel": "AttachedFile",
#       "url": "http://cyg249:8080/tfs/DefaultCollection/_apis/wit/attachments/94940b68-d900-4d96-92fe-0bc1ae99eae9",
#       "attributes": {
#         "comment": "Spec for the work",
#         "name":"RE JIMMY ESTRADA 6976223.msg"
#       }
#     }
#    } 
# ]
   
# post
#  http://cyg249:8080/tfs/DefaultCollection/_apis/wit/attachments?uploadType=Simple&areaPath=akshitaK
