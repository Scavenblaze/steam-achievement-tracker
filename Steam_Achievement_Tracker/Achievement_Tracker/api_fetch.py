import requests
import os
from dotenv import load_dotenv

load_dotenv()

steam_key = os.getenv('steam_key')

class owned_Games:
    def __init__(self, steam_id) -> None:
        self.steam_id = steam_id
        self.steam_key = steam_key
     
    #-----------------------------------------------------------------------------------------
    #FIXME    
    #test this api out with public and private profile
    #ref: https://developer.valvesoftware.com/wiki/Steam_Web_API#GetPlayerSummaries_(v0002)
    #----------------------------------------------------------------------------------------- 
    
    def get_profile(self):
        url = " http://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002"
        params = {"key": self.steam_key, "steamid": self.steam_id}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            games = response.json()
        except ValueError as e:
            print(f"Error occurred: {e}")
            return []
        
        #filtered_result = [{'appid': game['appid'], 'name': game['name'], 'img_icon_url': game['img_icon_url']} for game in games['response']['games']]
        
        #return filtered_result
            
    
        
        
        
    def get_owned_games(self):
        url = "https://api.steampowered.com/IPlayerService/GetOwnedGames/v1/"
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
    
    
    def get_recently_played(self):
        url = "https://api.steampowered.com/IPlayerService/GetRecentlyPlayedGames/v1/"
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



        
    #FIXME: with the other url in deltelre    
    def get_player_achievements(self, appid):
        url = "https://api.steampowered.com/ISteamUserStats/GetUserStatsForGame/v1/"
        params = {"key": self.steam_key, "steamid": self.steam_id, "appid": appid}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            player_achievements = response.json()
        except ValueError as e:
            print(f"Error Occurred:s {e}")
            return []
        
        if(player_achievements.get('playerstats', {}).get('achievements')):
        
            filtered_result = [{'name': game} for game in player_achievements['playerstats']['achievements'].keys()]
            return filtered_result
        else:
            return []


    def get_game_achievements(self, appid):
        url = "https://api.steampowered.com/ISteamUserStats/GetSchemaForGame/v2/"
        params = {"key": self.steam_key, "steamid": self.steam_id, "appid": appid}
        response = requests.get(url, params=params)
        
        if response.status_code != 200:
            print(f"Error accessing steam api {response.status_code}")
            return []
        try:
            game_achievements = response.json()
    
        except ValueError as e:
            print(f"Error Occurred:s {e}")
            return []
        
        if(game_achievements.get('game')):
            filtered_result2 = [
                {'name': game['name'], 'displayname': game['displayName'], 'description': game.get('description', ''), 'icon': game['icon'], 'icongray': game['icongray']}
                for game in game_achievements['game']['availableGameStats']['achievements']
            ]
            return filtered_result2

        else: return []
        