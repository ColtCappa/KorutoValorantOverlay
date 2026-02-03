import requests
import time
import json
import pprint
from pathlib import Path

henrikdev_API_KEY = "*INSERT KEY HERE*"

SLEEP_SECONDS = 30
OUT = Path("C:/Users/Colt/Desktop/Koruto Projects/ValorantProjects/overlay.json")

region = "na"  # Enter region in lowercase!
name = "Koruto" # Riot User
tag = "Colt"    # Riot Tag

# HENRIKDEV URL
#url_leaderboard = "https://api.henrikdev.xyz/valorant/v1/leaderboard/"
url_mmr = f"https://api.henrikdev.xyz/valorant/v2/mmr/{region}/{name}/{tag}"


while True:
    try:
        response = requests.get(url_mmr, headers={"Authorization": henrikdev_API_KEY,"Accept":"*/*"},)

        if response.status_code == 200:
            valorant_data = response.json()["data"]["current_data"]

            payload = {
                "rank": valorant_data["currenttierpatched"],
                "rr": valorant_data["ranking_in_tier"]
            }
            OUT.write_text(json.dumps(payload), encoding="utf-8")

        else:
            print("Error:", response.status_code)
    
    except Exception:
        OUT.write_text(json.dumps({"rank":"--", "rr":"--"}), encoding="utf-8")

    time.sleep(SLEEP_SECONDS)  # Wait 30 seconds before next check



def printRank():
        response = requests.get(url_mmr, headers={"Authorization": henrikdev_API_KEY,"Accept":"*/*"},)

        if response.status_code == 200:
            valorant_data = response.json()["data"]["current_data"]
            #pprint.pprint(valorant_data)
            current_rank = valorant_data["data"]["current_data"]["currenttierpatched"]
            elo = valorant_data["data"]["current_data"]["ranking_in_tier"]
            #print(valorant_data["data"].keys())
            print(f"{current_rank} - {elo}RR")

        else:
            print("Error:", response.status_code)
