# Import our custom modules
import auth
import fetcher
import ml_logic
import youtube_manager

def main():
    print("--- AI MUSIC MANAGER APP ---")
    
    # 1. Login
    yt = auth.get_authenticated_client()
    if not yt:
        return

    # 2. Get Data
    tracks = fetcher.get_liked_tracks(yt, limit=30)
    if not tracks:
        print("No tracks found.")
        return

    # 3. Process Data (The Brain)
    # This returns a dictionary of { "Playlist Name": [Song IDs] }
    playlists_to_create = ml_logic.cluster_songs(tracks)
    
    if not playlists_to_create:
        print("No clusters formed.")
        return

    # 4. Execute Actions (The Hands)
    youtube_manager.create_playlists(yt, playlists_to_create)
    
    print("\nDONE!")

if __name__ == "__main__":
    main()