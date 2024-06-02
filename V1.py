import requests
import base64

# client credentials
client_id = 'd2e579a8e87545ca8098ab6bec97066c'
client_secret = '5c465b206bad4ed189307afc9a8af016'

# encoding the client credentials
client_credentials = f"{client_id}:{client_secret}"
client_credentials_base64 = base64.b64encode(client_credentials.encode())

# spotify token URL
token_url = 'https://accounts.spotify.com/api/token'

# request headers
headers = {
    'Authorization': f'Basic {client_credentials_base64.decode()}',
    'Content-Type': 'application/x-www-form-urlencoded'
}

# request body
data = {
    'grant_type': 'client_credentials'
}

# Make the request to get the access token
response = requests.post(token_url, headers=headers, data=data)

# Parse the response
if response.status_code == 200:
    token_info = response.json()
    access_token = token_info['access_token']
    print(f"Access Token: {access_token}")
else:
    print(f"Failed to get access token. Status code: {response.status_code}")
    print(response.text)

