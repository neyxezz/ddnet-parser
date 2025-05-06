import requests, json

def _fetch_master_data() -> dict:
    try:
        response = requests.get("https://master1.ddnet.org/ddnet/15/servers.json")
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error parsing: {e}")

def _fetch_player_data(name) -> dict:
    try:
        response = requests.get(f"https://ddstats.tw/player/json?player={name}")
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error parsing: {e}")

