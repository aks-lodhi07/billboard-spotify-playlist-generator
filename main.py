from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os


date = input("Enter a date in YYYY-MM-DD format to travel back in time: ")
BILLBOARD_URL = f"https://www.billboard.com/charts/hot-100/{date}"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/138.0.0.0 Safari/537.36 Edg/138.0.0.0"}
# date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

response = requests.get(url=BILLBOARD_URL,headers=header)
soup = BeautifulSoup(response.text, 'html.parser')
songs = [tag.getText().strip() for tag in soup.select("li ul li h3")]
print(f"\nFound {len(songs)} songs from {date}'s Billboard Hot 100.")

# Spotify Authorization
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=f"{os.environ("SPOTIFY_CLIENT_ID=")}",
    client_secret=f"{os.environ("SPOTIFY_CLIENT_SECRET")}",
    redirect_uri="https://example.com/callback",
    scope="playlist-modify-private",
    show_dialog=True,
    cache_path="token.txt",
    username="Akshat Lodhi",
))

user_id = sp.current_user()["id"]
song_names = ["The list of song", "titles from your", "web scrape"]

song_uris = []
year = date.split("-")[0]
for song in songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
