import requests
import random
from django.core.management import BaseCommand
from core.models import Song
from django.conf import settings
class Command(BaseCommand):
    help = "Execute Spotify discover weekly synchronization"


    def handle(self, *args, **options):
        all_songs=Song.objects.all()
        random_song = random.choice(all_songs)

        body = {
            "chat_id": 5522560338,
            "text": random_song.external_url
        }
        telegram_token = settings.TELEGRAM_TOKEN
        response = requests.get(
            url=f"https://api.telegram.org/bot{telegram_token}/sendMessage",
            params=body)
        response.raise_for_status()
