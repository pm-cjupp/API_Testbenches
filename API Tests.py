import requests
import json

username = 'cjupp'
password = 'ZJcj4GBSF9Frr9KCmGxy'

server_ip = ''
server_port = ''

def jprint(obj):
    # create a formatted string of the Python JSON object
    text = json.dumps(obj, sort_keys=True, indent=4)
    print(text)

# syntax:
# GET / webapi/<CGI_PATH>?api=<API_NAME>&version=<VERSION>&method=<METHOD>[&<PARAMS>][&_sid=<SID>

#response = requests.get("http://192.168.1.65:5001/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=SYNO.API.Auth,SYNO.FileStation.")

response = requests.get("http://192.168.1.65:5000/webapi/query.cgi?api=SYNO.API.Info&version=1&method=query&query=all")
jprint(response.json())


#Need to look into SSL certificates for logging in, for now it's skipped
response = requests.get("https://192.168.1.65:5001/webapi/auth.cgi?api=SYNO.API.Auth&version=6&method=login&account=" + username + "&passwd=" + password, verify = False)


jprint(response.json())


