import requests, json
import urllib.parse
def _fetch_master_data() -> dict:
    try:
        response = requests.get("https://master1.ddnet.org/ddnet/15/servers.json")
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error parsing: {e}")

def _fetch_player_data(name) -> dict:
    try:
        params = {"player": name}
        response = requests.get("https://ddstats.tw/player/json", params={"player": name}) #корректный запрос при пробеле в нике, но всеравно какие то проблемы...
        response.raise_for_status()
        return json.loads(response.text)
    except requests.exceptions.RequestException as e:
        raise Exception(f"Error parsing: {e}")
