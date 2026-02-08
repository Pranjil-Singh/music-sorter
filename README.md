# 🎵 Smart Vibe Sorter (AI Playlist Generator)

A Python application that uses **Machine Learning (K-Means Clustering)** and **NLP** to automatically organize your YouTube Music library into "Vibe-based" playlists (e.g., *High Energy*, *Chill Lofi*, *Deep Focus*).

Instead of manual sorting, this tool "listens" to the metadata of your music, understands the genre/mood using Last.fm tags, and groups similar songs together.

## 🚀 Features

- **Smart Tagging:** Fetches rich metadata (genres, moods) for every song using the **Last.fm API**.
- **Unsupervised Learning:** Uses **K-Means Clustering** to find hidden patterns in your music taste without pre-defined categories.
- **Auto-Naming:** The AI analyzes the most common tags in a cluster to automatically name the playlist (e.g., "AI Vibe: Dream Pop / Shoegaze").
- **Duplicate Prevention:** Smart sync logic ensures songs aren't added if they already exist in the target playlist.
- **OAuth Authentication:** Secure, token-based login to YouTube Music (no password sharing).

## 🛠️ Tech Stack

- **Language:** Python 3.12+
- **APIs:** [ytmusicapi](https://github.com/sigma67/ytmusicapi), [pylast](https://github.com/pylast/pylast) (Last.fm)
- **Data Science:** `pandas`, `scikit-learn`, `numpy`
- **Authentication:** OAuth 2.0

## 📦 Installation

```bash
### 1. Clone the Repository
git clone [https://github.com/YOUR_USERNAME/smart-vibe-sorter.git](https://github.com/YOUR_USERNAME/smart-vibe-sorter.git)
cd smart-vibe-sorter

2. Set Up Virtual Environment (Recommended)
Bash

# Create environment
python -m venv venv

# Activate (Linux/Mac)
source venv/bin/activate

# Activate (Windows)
venv\Scripts\activate

3. Install Dependencies
Bash

pip install -r requirements.txt

🔑 Configuration (The "Secret Sauce")

You need two things to make this work: API Keys for Last.fm (to analyze music) and Authentication for YouTube Music (to manage playlists).
Step 1: Last.fm API Keys

    Go to the Last.fm API Account Creation Page.

    Create an API account (it's free).

    Copy your API Key and Shared Secret.

    Create a file named my_secrets.py in the project folder.

    Paste your keys inside:
    Python

    # api_config.py
    LASTFM_API_KEY = "paste_your_key_here"
    LASTFM_API_SECRET = "paste_your_secret_here"

Step 2: YouTube Music Login

You need to generate an oauth.json file so the script can access your library securely.

Option A: The Easy Way (OAuth) Run this command in your terminal:
Bash

ytmusicapi oauth

    Follow the link it gives you.

    Log in with your Google account.

    Paste the code.

    It will generate oauth.json.

Option B: The Manual Way (Browser Headers) If OAuth fails, use the manual method:

    Run ytmusicapi browser in your terminal.

    Open YouTube Music in Firefox/Chrome.

    Open Developer Tools (F12) -> Network Tab.

    Filter for browse.

    Copy the Request Headers (starting from accept: */*).

    Paste them into the terminal and press Ctrl+D.

    This generates headers_auth.json.

    If it generated browser.json then rename the file to headers_auth.json.

▶️ Usage

Once configured, simply run the main script:
Bash

python main.py

What happens next?

    The script fetches your "Liked Songs" from YouTube Music.

    It queries Last.fm to find the "Vibe" (tags) for each song.

    The AI groups them into clusters.

    New playlists (e.g., "AI Vibe: Rock / Alternative") appear in your YouTube Music account!

📄 License

Distributed under the MIT License. See LICENSE for more information.
