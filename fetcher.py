def get_liked_tracks(yt_client, limit=50):
    """
    Fetches liked songs from YouTube Music.
    """
    print(f"📥 Fetching your last {limit} liked songs...")
    try:
        results = yt_client.get_liked_songs(limit=limit)
        return results.get('tracks', [])
    except Exception as e:
        print(f"Error fetching songs: {e}")
        return []