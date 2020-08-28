import requests
import json

USER_ID = 'o75b2yw7j63ynq88ldv2xbtxx'
CLIENT_ID =  '81a85361a046433299fb5e441100f4e2'
CLIENT_SECRET = 'da76e7c036f04214a39e4ddaa803afaf'


URL = 'https://accounts.spotify.com/api/token'

# POST
auth_response = requests.post(URL, {
    'grant_type': 'client_credentials',
    'scope': 'playlist-modify-private',
    'client_id': CLIENT_ID,
    'client_secret': CLIENT_SECRET,
})

# convert the response to JSON
auth_response_data = auth_response.json()

# save the access token
access_token = auth_response_data['access_token']

endpoint_url = "https://api.spotify.com/v1/recommendations?"

# OUR FILTERS
limit='10'
market="IT"
seed_genres="rap"
target_danceability='1.0'

query = endpoint_url + 'limit=' + limit + '&market=' + market + '&seed_genres=' + seed_genres + '&target_danceability=' + target_danceability

response =requests.get(query,
               headers={"Content-Type":"application/json",
                        "Authorization":"Bearer {token}".format(token=access_token)

                        })
Json = response.text
Python = json.loads(Json)
print(access_token)
#for track in Python['tracks']:
#    print(track['name'])
