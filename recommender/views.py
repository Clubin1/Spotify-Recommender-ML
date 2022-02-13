from django.http import HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd
def fetchSpotify(request):
    """
    'e37014852f9846b5a8d03dc8c58c616c',
    '424ca278b51049f1aa5bd348991c8d75'
    """
    scope = "user-top-read"
    client_id = "e37014852f9846b5a8d03dc8c58c616c"
    client_secret = "424ca278b51049f1aa5bd348991c8d75"
    redirect_uri = "http://127.0.0.1:8001/recommender/callback"
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
        scope = scope,
        client_id = client_id,
        client_secret = client_secret,
        redirect_uri = redirect_uri
    ))
    #artists = sp.current_user_top_artists()
    #playlists = sp.current_user_playlists()
    tracks = sp.current_user_top_tracks()
    print(tracks['items'][0]['popularity'])
    df = pd.DataFrame.from_dict(tracks)
    df = df.rename(columns={
        'items': 'id', 
        'total': 'name', 
        'limit': 'artist_name', 
        'offset': 'album_name', 
        'previous' : 'popularity'
    })  # old method  
    return HttpResponse(df.to_html())
