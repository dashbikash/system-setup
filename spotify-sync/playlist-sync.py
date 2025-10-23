import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# Client Credentials Flow - No redirect URL needed, but no user-specific data access
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials())

# result=sp.search(q="Verve", limit=10, type="artist")

# for artist in result['artists']['items']:
#     if  artist:
#         print(f"{artist['id']} - {artist['name']}")

artist_result = sp.artist_top_tracks('2cGwlqi3k18jFpUyTrsR84', country='US')
for track in artist_result['tracks']:
    print(f"{track['name']}")