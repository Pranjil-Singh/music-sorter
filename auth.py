from ytmusicapi import YTMusic
import os

def get_authenticated_client():
    # Check for the NEW OAuth file
    if os.path.exists("oauth.json"):
        return YTMusic("oauth.json")
    
    # Fallback to the old way
    elif os.path.exists("headers_auth.json"):
        return YTMusic("headers_auth.json")
        
    else:
        raise FileNotFoundError("Error: No login file found. Run 'ytmusicapi oauth' in terminal.")