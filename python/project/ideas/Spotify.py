#!/usr/bin/python

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
headers = {

    'Content-Type': 'application/json',
    'Authorization': 'Bearer {token}'.format(token=access_token)

}

def Search():

    Kind = 'Rap'
    Limit = '50'

    BASE_URL = 'https://api.spotify.com/v1/search'
    payload = {

        'q': Kind,
        'type': 'track',
        'market': 'IT',
        'limit': Limit,
        'offset': '5'

    }

    response = requests.get(BASE_URL, params=payload, headers=headers)
    tracks = json.loads(response.text)

    for track in tracks['tracks']['items']:
        print(track['album']['name'])

def Create_Playlist():

    BASE_URL = 'https://api.spotify.com/v1/users/{user_id}/playlists'.format(user_id=USER_ID)
    REQUESTS_BODY = json.dumps({

        "name": "Example",
        "description": "New playlist description",
        "public": False

    })

    response = requests.post(BASE_URL, data=REQUESTS_BODY, headers=headers)
    print(response.text)

Create_Playlist()
