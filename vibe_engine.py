import pylast
import re  #Regular expression(for title work)
import api_config

API_KEY=api_config.LASTFM_API_KEY
API_SECRET=api_config.LASTFM_API_SECRET

try:
    #setting connection
    network=pylast.LastFMNetwork(api_key=API_KEY, api_secret=API_SECRET)
except Exception as e:
    print(f"Error connection to Last.fm: {e}")

def clean_title(title):
    #making the title clean
    #remove garbage characters
    title=re.sub(r"\(.*?\)|\[.*?\]", "",title)

    #remove feat. lyrics official video etc.
    title=re.sub(r"(?i)\b(ft\.|feat\.|official video|official audio|lyrics|video)\b","",title)

    #remove left and right space if any
    return title.strip()

def get_song_tags(artist_name, track_name):
    try:
        #cleaning title
        cleaned_title=clean_title(track_name)

        #searching track from Last.fm database
        search=network.search_for_track(artist_name, cleaned_title)
        best_match=search.get_next_page()[0]

        #getting user voted top tags
        top_tags=best_match.get_top_tags(limit=3)

        #taking only lowercase text
        cleaned_tags=[tag.item.name.lower() for tag in top_tags]

        #if song tag not found then getting tags on artist
        if not cleaned_tags:
            artist=network.get_artist(artist_name)
            artist_tags=artist.get_top_tags(limit=5)
            cleaned_tags=[tag.item.name.lower() for tag in artist_tags]

        #if tag still not found
        if not cleaned_tags:
            return ["unknown"]
        return cleaned_tags
    except Exception as e:
        #if song not found
        return ["unknown"]
if __name__=="__main__":
    #checking function
    print("vibe engine test")
    artist = "PSY"
    song = "Gangnam Style"
    print(f"1. Checking '{song}' by {artist}...")
    tags = get_song_tags(artist, song)
    print(f"   -> RESULT: {tags}")