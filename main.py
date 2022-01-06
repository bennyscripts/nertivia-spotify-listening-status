import nertivia4py
import requests
import time
import json

config = json.load(open("config.json"))
spotify_token = config["spotify_token"]
nertivia_token = config["nertivia_token"]

nertivia = nertivia4py.Nertivia(nertivia_token)

def get_spotify_playing():
    response = requests.get("https://api.spotify.com/v1/me/player", headers={"Authorization": f"Bearer {spotify_token}"})
    return response

while True:
    resp = get_spotify_playing()
    if resp.status_code != 200:
        print("Error getting playback")
        continue

    try:
        data = resp.json()
    except:
        print("Error parsing JSON")
        continue
    
    if data["is_playing"]:
        status = f"🎧 {data['item']['name']} by {data['item']['artists'][0]['name']}"
    else:
        status = "🎵 No music playing"

    nertivia.setCustomStatus(status)
    print(f"Updated status to {status}")
    time.sleep(5)