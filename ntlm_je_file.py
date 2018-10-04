import win32com.client
from os import listdir
import requests
import json
from os.path import isfile, join
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
path="C:\\Users\\akshita.kukreja\\Desktop\\JE\\TFS_Mails\\"
files = [f for f in listdir(path) if isfile(join(path, f))]

for filename in files:
  msg = outlook.OpenSharedItem(path+filename)
  url = 'https://tfsweb.justenergy.com/tfs/fr_TX/ALL_SUPPORT/_apis/wit/workitems/$Support%20Request'
  headers = {'Content-Type':'application/json-patch+json'}
  d = [
    {
      "op": "add",
      "path": "/fields/System.Title",
      "value": msg.Subject
    },
    {
      "op": "add",
      "path": "/fields/System.Description",
      "value": msg.Body
    },
     {
      "op": "add",
      "path": "/fields/System.AssignedTo",
      "value": "Akshita Kukreja"
    },
    {
       "op": "add",
       "path": "/fields/System.IterationPath",
       "value": "ALL_SUPPORT\\2018 - October 01st to October 05th"
     }
     {
       "op": "add",
       "path": "/fields/Hudson.TFS.Organization",
       "value": "Customer Service"
     },
     {
      "op":"add",
      "path": "/fields/System.State",
      "value": "Ready for Analysis"
    }
   
  ]

  
  data= json.dumps(d)
  res = requests.post(url = url, data = data , headers = headers ,auth=('akukreja', 'Summer2018')).json()
  print(res['url'])
  fileName = open(path+filename,'rb').read()
  resFile = requests.post(
                      url='https://tfsweb.justenergy.com/tfs/fr_TX/_apis/wit/attachments?uploadType=Simple&areaPath=ALL_SUPPORT',
                      data=fileName,
                      headers={'Content-Type': 'application/octet-stream','Accept':'application/json;api-version=1.0'},
                      auth=('akukreja', 'Summer2018')).json()
  

  dataForupdate = [
     {
      "op": "add",
      "path": "/relations/-",
      "value": {
        "rel": "AttachedFile",
        "url": resFile['url'],
        "attributes": {
          
          "name":filename
        }
      }
     },
     {
      "op":"add",
      "path": "/fields/System.State",
      "value": "In Analysis"
    }
     
  ]
  id =res['id']
  updateData = json.dumps(dataForupdate)
  attachFileToTicket = requests.patch(url='https://tfsweb.justenergy.com/tfs/fr_TX/_apis/wit/workitems/'+str(id),
    data=updateData,
    headers={'Content-Type':'application/json-patch+json',
             'Accept':'application/json;api-version=1.0'},
    auth=('akukreja','Summer2018'))
  path2="C:\\Users\\akshita.kukreja\\Desktop\\JE\\"
  filename2="Issue Priority Definition and SLA.docx"
  fileName2 = open(path2+filename2,'rb').read()
  resFile = requests.post(url='https://tfsweb.justenergy.com/tfs/fr_TX/_apis/wit/attachments?uploadType=Simple&areaPath=ALL_SUPPORT',
                      headers={'Content-Type': 'application/octet-stream','Accept':'application/json;api-version=1.0'},
                      data=fileName2,
                      auth=auth=('akukreja', 'Summer2018')).json()
  
  dataForupdate2 = [
     {
      "op": "add",
      "path": "/relations/-",
      "value": {
        "rel": "AttachedFile",
        "url": resFile['url'],
        "attributes": {
          
          "name":filename2
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
  updateData2 = json.dumps(dataForupdate2)
  attachFileToTicket = requests.patch(url='https://tfsweb.justenergy.com/tfs/fr_TX/_apis/wit/workitems/'+str(id),
    data=updateData2,
    headers={'Content-Type':'application/json-patch+json',
             'Accept':'application/json;api-version=1.0'},
    auth=auth=('akukreja', 'Summer2018'))
print("done")