import requests
import base64
import json

# Step 1 - Authorization
url = "https://accounts.spotify.com/api/token"
headers = {}
data = {}

# Encode as Base64
message = '81a85361a046433299fb5e441100f4e2:da76e7c036f04214a39e4ddaa803afaf'
messageBytes = message.encode('ascii')
base64Bytes = base64.b64encode(messageBytes)
base64Message = base64Bytes.decode('ascii')


headers['Authorization'] = "Basic {base64Message}".format(base64Message=base64Message)
data['grant_type'] = "client_credentials"

r = requests.post(url, headers=headers, data=data)

token = r.json()['access_token']

# Step 2 - Use Access Token to call playlist endpoint

playlistId = "4XYQ4oJE03JHBriNPJ2SSD"
playlistUrl = 'https://api.spotify.com/v1/playlists/{playlistId}'.format(playlistId=playlistId)
headers = {
    "Authorization": "Bearer " + token
}

res = requests.get(url=playlistUrl, headers=headers)

print(json.dumps(res.json(), indent=2))
