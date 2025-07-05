import requests
import os
from dotenv import load_dotenv

load_dotenv()

steam_key = os.getenv('steam_key')

class owned_Games:
    def __init__(self, steam_id) -> None:
        self.steam_id = steam_id
        self.steam_key = steam_key
        
    def get_owned_games(self):
        url = f"https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
        params = {"key": self.steam_key, "steamid": self.steam_id, "include_appinfo": True, "include_played_free_games": True}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            games = response.json()
        except ValueError as e:
            print(f"Error occurred: {e}")
            return []
        
        filtered_result = [{'appid': game['appid'], 'name': game['name'], 'img_icon_url': game['img_icon_url']} for game in games['response']['games']]
            

        return filtered_result
        
    #FIXME: like the others    
    def get_player_achievements(self):
        app_id = "12210"  # gta 4 FIXME: get appid dynamic
        url = f"https://api.steampowered.com/ISteamUserStats/GetPlayerAchievements/v1/"
        params = {"key": self.steam_key, "steamid": self.steam_id, "appid": app_id}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            game_achievement = response.json()
        except ValueError as e:
            print(f"Error Occurred:s {e}")
            return []
        
        return game_achievement


    def get_recently_played(self):
        url = f"https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/"
        params = {"key": self.steam_key, "steamid": self.steam_id}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            recent_games = response.json()
        except ValueError as e:
            print(f"Error Occurred: {e}")
            return []
        
        filtered_result = [{'appid': game['appid'], 'name': game['name'], 'img_icon_url': game['img_icon_url']} for game in recent_games['response']['games']]

        return filtered_result
 
 
 
        
thing = owned_Games(76561198947714890)
print(thing.get_recently_played())