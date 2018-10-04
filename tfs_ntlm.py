import urllib
import ntlm_auth 
# import HTTPNtlmAuthHandler
from sharepoint import SharePointSite
username = 'CYBERINDIA\\akshita.kukreja'
password = 'Akshita@30'
url = 'http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1'
passman = urllib.HTTPPasswordMgrWithDefaultRealm()
passman.add_password(None, url, username, password)
auth_NTLM = urllib.HTTPNtlmAuthHandler.HTTPNtlmAuthHandler(passman)
opener = urllib.build_opener(auth_NTLM)
site = SharePointSite(url, opener)

for sp_list in site.lists:
    print (sp_list.id, sp_list.meta['Title'])