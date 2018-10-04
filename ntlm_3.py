import socket
import flask
from ntlm_auth.ntlm import NtlmContext

username = 'akshita.kukreja'
password = 'Akshita@30'
domain = 'CYBERINDIA' # Can be blank if you are not in a domain
workstation = socket.gethostname().upper() # Can be blank if you wish to not send this info

ntlm_context = NtlmContext(username, password, domain, workstation, ntlm_compatibility=0) # Put the ntlm_compatibility level here, 0-2 for LM Auth/NTLMv1 Auth
negotiate_message = ntlm_context.step()

# Attach the negotiate_message to your NTLM/NEGOTIATE HTTP header and send to the server. Get the challenge response back from the server
challenge_message = http.response.headers['HEADERFIELD']

authenticate_message = ntlm_context.step(challenge_message)
print(authenticate_message)
# # Attach the authenticate_message ot your NTLM_NEGOTIATE HTTP header and send to the server. You are now authenticated with NTLMv1