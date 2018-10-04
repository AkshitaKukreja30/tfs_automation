import base64
import urllib.request
username = 'akshita.kukreja'
password = 'Akshita@30'
#'+username+'/'+password
tfsApi = 'http://cyg249:8080/tfs/DefaultCollection/akshitaK/_apis/wit/workitems/1'
encoded = base64.b64encode(password.encode("utf-8"))
print(encoded)
decoded = base64.b64decode(encoded)
print(decoded)

request = urllib.Request(tfsApi) 
base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
request.add_header("Authorization", "Basic %s" % base64string) 
result = urllib.urlopen(request)
print(result)

# import requests, base64

# usrPass = "akshita.kukreja:Akshita@30"
# b64Val = base64.b64encode(usrPass)
# r=requests.post(tfsApi, 
#                 headers={"Authorization": "Basic %s" % b64Val},
#                 data=payload)
# print("------------------------------------------------------------------------------")
# print(r)

# import urllib2, base64 
# request = urllib2.Request("http://api.foursquare.com/v1/user") 
# base64string = base64.encodestring('%s:%s' % (username, password)).replace('\n', '')
# request.add_header("Authorization", "Basic %s" % base64string) 
# result = urllib2.urlopen(request)