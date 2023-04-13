
from ninja import NinjaAPI
from core.models import Artist, Song

api = NinjaAPI(title="Musicmanger API", version="1.0.0")

@api.get("/artist")
def all_artists(request):
    results = []
    for artist in Artist.objects.filter():
        results.append({
        "name": artist.name,
        })
    return {"artists": results}

@api.get("/Song")
def all_songs(request):
    results = []
    for song in Song.objects.filter():
        results.append({
        "title": song.title,
        "external_url": song.external_url,
        "picture_url": song.picture_url,
        "artist": song.artist.name,
        "created_date": song.created_date,
        })
    return {"songs": results}
