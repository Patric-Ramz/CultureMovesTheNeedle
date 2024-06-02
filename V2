import requests
import pandas as pd

# access token
access_token = 'BQACA5WUs8XTWm703WxkpSkzhRMEHz5dHjdS0lTz16xf8f8srgkLgU1SnA0iy-7KJqLA7q2WMqBksk8AoD4LjlS2VB2oSm4n4p9D4CPhAeVhGtVuCso'

# artist ID (JBP)
artist_id = '04bckYvJEXGoKmBWW9leSz'

# Spotify API URL for getting artist information
artist_url = f'https://api.spotify.com/v1/artists/{artist_id}'

# Request headers
headers = {
    'Authorization': f'Bearer {access_token}'
}

# Make the request to get artist information
response = requests.get(artist_url, headers=headers)

# Parse the response
if response.status_code == 200:
    artist_info = response.json()

# Extract relevant information
    data = {
        'Name': artist_info['name'],
        'Followers': artist_info['followers']['total'],
        'Genres': ', '.join(artist_info['genres']),
        'Popularity': artist_info['popularity'],
        'Spotify URL': artist_info['external_urls']['spotify'],
        'Images': ', '.join([image['url'] for image in artist_info['images']])
    }
    
    # Create a DataFrame
    df = pd.DataFrame([data])
    print(df)    