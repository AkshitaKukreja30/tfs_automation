import requests
import json
from requests_ntlm import HttpNtlmAuth
# headers = {'Content-Type': 'application/xml'} # set what your server accepts
# url = 'http://localhost:8080/tfs/DefaultCollection/_apis/wit/workitems/1'
url = 'http://cyg249:8080/tfs/defaultcollection/akshitaK/_apis/wit/workitems/$task?api-version=4'
# request_xml= '<Name>Wilson Bright John</Name>'
# r=requests.get(url, data=request_xml,headers=headers,auth=HttpNtlmAuth('domain\\username',
# 'password'))
headers = {'Content-Type':'application/json-patch+json'}
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
  }
 
]

# ,{
#     "op": "add",
#     "path": "/fields/System.IterationPath",
#     "value": "ALL_SUPPORT\\2018 - October 01st to October 05th"
#   }
  # {
  #   "op": "add",
  #   "path": "/fields/Hudson.TFS.Organization",
  #   "value": "Customer Service"
  # }
data= json.dumps(d)
print(data)
# headersForAttachment = {'Accept':'application/json;api-version=1.0'}
# sending post request and saving response as response object 
res = requests.post(url = url, data = data , headers = headers ,auth=HttpNtlmAuth('akshita.kukreja','Akshita@30')).json()
print(res['url'])
print(res['id'])
import requests

fileName = open('C:\\Users\\akshita.kukreja\\Desktop\\JE\\TFS_Mails\\RE Xavier Rivera Jr..msg','rb').read()
resFile = requests.post(url=' http://cyg249:8080/tfs/DefaultCollection/_apis/wit/attachments?uploadType=Simple&areaPath=akshitaK',
                    data=fileName,
                    headers={'Content-Type': 'application/octet-stream','Accept':'application/json;api-version=1.0'},
                    auth=HttpNtlmAuth('akshita.kukreja','Akshita@30')).json()
print(resFile['url'])

#update it
datForupdate = [
   {
    "op": "add",
    "path": "/relations/-",
    "value": {
      "rel": "AttachedFile",
      "url": resFile['url'],
      "attributes": {
        
        "name":"RE Xavier Rivera Jr.msg"
      }
    }
   },
   {
    "op":"add",
    "path": "/fields/System.State",
    "value": "Closed"
  }
   
]
id =res['id']
updateData = json.dumps(datForupdate)
attachFileToTicket = requests.patch(url='http://cyg249:8080/tfs/defaultcollection/_apis/wit/workitems/'+str(id),
  data=updateData,
  headers={'Content-Type':'application/json-patch+json',
           'Accept':'application/json;api-version=1.0'},
  auth=HttpNtlmAuth('akshita.kukreja','Akshita@30'))

print(attachFileToTicket.text)
# r=requests.get(url,auth=HttpNtlmAuth('akshita.kukreja',
# 'Akshita@30'))
# print (r.status_code)
# print (r.text)