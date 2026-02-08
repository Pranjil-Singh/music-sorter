import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from collections import Counter
import vibe_engine  # Importing your existing vibe engine

def generate_smart_name(tags_list):
    """
    Decides a name for the playlist based on common tags.
    Input: ['pop dance', 'dance pop', 'electro']
    Output: "Vibe: Pop / Dance"
    """
    all_words = " ".join(tags_list).split()
    stop_words = ['music', 'song', 'songs', 'mix', 'vibe', 'unknown', 'official', 'video']
    
    # Filter out junk words
    clean_words = [w for w in all_words if w not in stop_words and len(w) > 2]
    
    if not clean_words:
        return "Variety Mix"
        
    # Get top 2 most frequent words
    most_common = Counter(clean_words).most_common(2)
    name = " / ".join([word[0].title() for word in most_common])
    return f"AI Vibe: {name}"

def cluster_songs(tracks):
    """
    Takes raw tracks -> Fetches Tags -> Clusters them -> Returns grouped data.
    """
    print(f"Analyzing {len(tracks)} songs (this calls Last.fm, be patient)...")
    
    song_data = []
    
    # 1. ENRICH DATA (Add Tags)
    for song in tracks:
        title = song['title']
        artist = song['artists'][0]['name']
        video_id = song['videoId']
        
        # Call the existing vibe engine
        tags = vibe_engine.get_song_tags(artist, title)
        tag_sentence = " ".join(tags)
        
        song_data.append({
            "title": title,
            "artist": artist,
            "video_id": video_id,
            "tags": tag_sentence
        })

    # 2. CREATE DATAFRAME
    df = pd.DataFrame(song_data)
    
    # If we don't have enough data, just return empty
    if len(df) < 3:
        print("Not enough data to cluster.")
        return {}

    # 3. VECTORIZE (Text -> Numbers)
    vectorizer = TfidfVectorizer(stop_words='english')
    matrix = vectorizer.fit_transform(df['tags'])

    # 4. CLUSTER (K-Means)
    # Dynamic clusters: 1 cluster for every 10 songs, max 5 clusters
    num_clusters = min(5, max(2, len(df) // 10))
    kmeans = KMeans(n_clusters=num_clusters, random_state=42)
    df['cluster'] = kmeans.fit_predict(matrix)

    # 5. ORGANIZE RESULTS
    # Return a dictionary: { "Playlist Name": [List of Song IDs] }
    playlists_to_create = {}
    
    for i in range(num_clusters):
        cluster_group = df[df['cluster'] == i]
        
        if cluster_group.empty:
            continue
            
        # Generate Name
        name = generate_smart_name(cluster_group['tags'].tolist())
        ids = cluster_group['video_id'].tolist()
        
        playlists_to_create[name] = ids
        
    return playlists_to_create