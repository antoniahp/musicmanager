# Haces todos los imports de las librerias que vas a utilizar
import requests # Importamos la libreria para hacer peticiones ( el postman de python )
from django.core.management import BaseCommand
from core.models import Artist, Song
from django.conf import settings

class Command(BaseCommand):
    help = "Execute Spotify discover weekly synchronization"

    def handle(self, *args, **options):

        spotify_token_url = "https://accounts.spotify.com/api/token"
        spotify_token_data = {
            "grant_type": "client_credentials",
            "client_id": settings.SPOTIFY_CLIENT_ID,
            "client_secret": settings.SPOTIFY_SECRET,
        }
        response = requests.post(url=spotify_token_url, data=spotify_token_data)
        spotify_token = response.json()["access_token"]

        headers = {
            "Authorization": "Bearer " + spotify_token
        }

        response = requests.get(url="https://api.spotify.com/v1/playlists/37i9dQZEVXcVMlRJWgzONt", headers=headers)
        response_json = response.json()

        tracks = response_json["tracks"]["items"]
        parsed_tracks = []

        for track in tracks:
            parsed_track = {
                "song_name": track["track"]["name"],
                "url": track["track"]["external_urls"]["spotify"],
                "artist_name": track["track"]["artists"][0]["name"],
            }
            parsed_tracks.append(parsed_track)

        for track in parsed_tracks:
            artist, artist_was_created = Artist.objects.get_or_create(name=track["artist_name"])
            song, song_was_created = Song.objects.get_or_create(title=track["song_name"], picture_url="", external_url=track["url"], artist=artist)