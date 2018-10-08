import requests
import json
from requests_ntlm import HttpNtlmAuth
import win32com.client
from os import listdir
import pandas as pd
from os.path import isfile, join
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
path="C:\\Users\\akshita.kukreja\\Desktop\\JE\\TFS_Mails\\"
url = 'http://cyg249:8080/tfs/defaultcollection/akshitaK/_apis/wit/workitems/$task?api-version=4'
headers = {'Content-Type':'application/json-patch+json'}
files = [f for f in listdir(path) if isfile(join(path, f))]
i=0
df = pd.DataFrame(columns=['Subject','Body'])
for file in files:
    filename=file
    msg = outlook.OpenSharedItem(path+filename)
    d = [{
    "op": "add",
    "path": "/fields/System.Title",
    "from": "",
    "value": msg.Subject,
    "fields": {
        "System.AreaPath": "akshitaK",
        "System.TeamProject": "akshitaK",
        "System.IterationPath": "akshitaK\\Iteration 1",
        "System.WorkItemType": "Task",
        "System.State": "New",
        "System.Reason": "New",
        "System.AssignedTo": "Akshita Kukreja <CYBERGINDIA\\akshita.kukreja>",
        "System.CreatedDate": "2018-10-01T11:19:50.71Z",
        "System.CreatedBy": "Akshita Kukreja <CYBERGINDIA\\akshita.kukreja>",
        "System.ChangedDate": "2018-10-01T11:19:50.71Z",
        "System.ChangedBy": "Akshita Kukreja <CYBERGINDIA\\akshita.kukreja>",
        "System.Title": msg.Body,
        "Microsoft.VSTS.Common.StateChangeDate": "2018-10-01T11:19:50.71Z",
        "Microsoft.VSTS.Common.Priority": 2,
        "System.Description": msg.Subject
    },
    }]


    data= json.dumps(d)
    print(data)
    res = requests.post(url = url, data = data , headers = headers ,auth=HttpNtlmAuth('akshita.kukreja','Akshita@30'))
    print(res.text)

    df.loc[i] = [msg.Subject, msg.Body]
    i=i+1
print(msg)
# writer = pd.ExcelWriter('tfs_contents.xlsx')
# df.to_excel(writer, sheet_name='Sheet1')
# writer.save()   
