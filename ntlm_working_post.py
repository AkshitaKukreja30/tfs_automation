import requests
import json
from requests_ntlm import HttpNtlmAuth
url = 'http://cyg249:8080/tfs/defaultcollection/akshitaK/_apis/wit/workitems/$task?api-version=4'
headers = {'Content-Type':'application/json-patch+json'}
d = [{
    "op": "add",
    "path": "/fields/System.Title",
    "from": "",
    "value": "TASK 9",
    "fields": {
        "System.AreaPath": "akshitaK",
        "System.TeamProject": "akshitaK",
        "System.IterationPath": "akshitaK",
        "System.WorkItemType": "Task",
        "System.State": "New",
        "System.Reason": "New",
        "System.Title": "TASK 11",
        "Systen.AssignedTO" : "Akshita Kukreja <CYBERGINDIA\\akshita.kukreja>",
        "System.Description" : "DESCRIPTION FOR TASK 11",
        "Microsoft.VSTS.Common.StateChangeDate": "2018-09-28T13:22:48.17Z",
        "Microsoft.VSTS.Common.Priority": 2
    },
  }]
data= json.dumps(d)
print(data)
res = requests.post(url = url, data = data , headers = headers ,auth=HttpNtlmAuth('akshita.kukreja','Akshita@30'))
print(res.status_code)
print(res.text)
