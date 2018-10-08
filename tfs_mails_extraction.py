import win32com.client
from os import listdir
import pandas as pd
from os.path import isfile, join
outlook = win32com.client.Dispatch("Outlook.Application").GetNamespace("MAPI")
path="C:\\Users\\akshita.kukreja\\Desktop\\JE\\TFS_Mails\\"
files = [f for f in listdir(path) if isfile(join(path, f))]
i=0
df = pd.DataFrame(columns=['Subject','Body'])
for file in files:
	filename=file
	msg = outlook.OpenSharedItem(path+filename)
	print (msg.Subject)
	print("---------------------------------------------------------------")
	print (msg.Body)
	df.loc[i] = [msg.Subject, msg.Body]
	i=i+1
print(msg)
writer = pd.ExcelWriter('tfs_contents.xlsx')
df.to_excel(writer, sheet_name='Sheet1')
writer.save()	

