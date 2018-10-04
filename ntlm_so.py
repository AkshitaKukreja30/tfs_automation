import win32com.client

url = 'http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1'

h = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
h.SetAutoLogonPolicy(0)
h.Open('GET', url, False)
h.Send()
result = h.responseText
print(result)