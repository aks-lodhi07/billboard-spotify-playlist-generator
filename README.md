# billboard-spotify-playlist-generator
# 🎧 Billboard Hot 100 → Spotify Playlist Generator 🎶

Turn back time and instantly create a Spotify playlist of the Billboard Top 100 songs from any historical date.

![Python]
![Web Scraping]
![Spotify API]
![Automation]

---

## 📌 Features

- 🔍 Scrapes the **Billboard Hot 100** for a given date using `BeautifulSoup`.
- 🔐 Authenticates with Spotify using **OAuth 2.0** (Spotipy).
- 🧠 Searches Spotify for each song using `track:{name} year:{YYYY}`.
- 🎶 Automatically creates a **private playlist** and adds all available tracks.
- 💥 Handles missing songs gracefully with logging.
- 💾 Secure credentials using `.env` + `token.txt`.

---

## 🛠️ Tech Stack

- **Language:** Python 3.9+
- **Libraries:** `requests`, `beautifulsoup4`, `spotipy`, `python-dotenv`
- **APIs:** Spotify Web API, Billboard Hot 100 (scraped)

---

## 🚀 How to Use

1. **Clone this repository:**

```bash
git clone https://github.com/yourusername/billboard-spotify-playlist.git
cd billboard-spotify-playlist

Install requirements:
pip install -r requirements.txt

Create a .env file with your Spotify credentials:
SPOTIPY_CLIENT_ID=your_client_id
SPOTIPY_CLIENT_SECRET=your_client_secret
SPOTIPY_REDIRECT_URI=http://localhost:8888/callback

Run the script:
python main.py
