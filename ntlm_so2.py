def create_challenge_response(self,challenge):
      import pywintypes
      output_buffer = None
      input_buffer = challenge
      error_msg = None
      try:
          error_msg, output_buffer = self.sspi_client.authorize(input_buffer)
      except pywintypes.error:
          return None
      response_msg = output_buffer[0].Buffer        
      response_msg = base64.b64encode(response_msg) 
      return response_msg 


SHOD='qqq.yyy.dev'
answer='result.xml'
fname='request.xml'
# try:
#     a_file = open(fname, 'r')
#     f=open(fname, 'r')
# except IOError:
#     print("error")
# size = os.path.getsize(fname)
# i=0
# for line in f:
#     i=i+1
# count_string=i
# f.close()
# size=size-count_string+1


# print("1")

try:
    webservice = httplib.HTTPConnection(SHOD)     
    webservice.putrequest("GET", "http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1")
    webservice.putheader("Content-length", "%d" % 0)
    webservice.putheader("Content-type", "text/xml")
    #webservice.putheader("User-Agent", 'Python-urllib/2.6')
    webservice.endheaders()
    res=webservice.getresponse()
except:
    msg= "unable to connect to URL:  "+ SHOD
    print("error")
    exit()
    
if res.status == 401:
    auth_methods = [s.strip() for s in 
                    res.msg.get('WWW-Authenticate').split(",")]
    print(auth_methods)
if res.status == 401:
    msg= "unable to connect to URL:  "+ SHOD_
    log_error(msg,answer)
    sys.exit()



print("2")

ntlm_gen = WindoewNtlmMessageGenerator()
auth_req_msg = ntlm_gen.create_auth_req()
webservice.putrequest("GET", "http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1")
webservice.putheader("Content-length", "%d" % 0)
webservice.putheader("Connection", "Keep-Alive")
#webservice.putheader("User-Agent", 'Python-urllib/2.6')
webservice.putheader('Authorization', 'NTLM'+' '+auth_req_msg) 
webservice.endheaders()
resp = webservice.getresponse()
resp.read()
print(resp.status)
challenge = resp.msg.get('WWW-Authenticate')
challenge_dec = base64.b64decode(challenge.split()[1])



print("3")

msg3 = ntlm_gen.create_challenge_response(challenge_dec)
webservice.putrequest("GET", "http://cyg249:8080/tfs/DefaultCollection/_apis/wit/workitems/1")
webservice.putheader("Content-type", "text/xml; charset=UTF-8")
webservice.putheader("Content-length", "%d" %(size))
webservice.putheader("Connection", "Close")
webservice.putheader('Authorization', 'NTLM'+' '+msg3)
#webservice.putheader("User-Agent", 'Python-urllib/2.6') 
webservice.endheaders()
sable = a_file.read()     
webservice.send(sable)
resp = webservice.getresponse()
res=resp.read()
PRINT(res)
