import win32com.client
URL = 'http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1'    
COM_OBJ = win32com.client.Dispatch('WinHTTP.WinHTTPRequest.5.1')
COM_OBJ.SetAutoLogonPolicy(0)
COM_OBJ.Open('GET', URL, False)
COM_OBJ.Send()
print(COM_OBJ.ResponseText)