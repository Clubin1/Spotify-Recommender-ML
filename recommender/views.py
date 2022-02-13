from django.http import HttpResponse
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

def fetchSpotify(request):
    spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
        'e37014852f9846b5a8d03dc8c58c616c',
        '424ca278b51049f1aa5bd348991c8d75'
    ))

    top_tracks = spotify.current_user_top_tracks()
    
    return HttpResponse(top_tracks)
