from django.shortcuts import redirect, render

from .api_fetch import owned_Games

steam_id = None






def landing_page(request):
    if request.method == "POST":
        steam_id = request.POST.get("steam_id")
        
        response = redirect("home") #after pressing submit
        response.set_cookie('steam_id', steam_id)
        return response
        
    return render(request, 'landing_page.html')
    

def home(request):
    steam_id = request.COOKIES.get("steam_id", None)
    games_list = owned_Games(steam_id).get_recently_played()
    
    return render(request, 'home.html', {'steam_id': steam_id, 'games_list': games_list})


def games_list(request):
    steam_id = request.COOKIES.get("steam_id", None)
    games_list = owned_Games(steam_id).get_owned_games()
    
    return render(request, 'games_list.html', {'games_list': games_list})




#12210 for gta4
def game_achievements(request, appid):
    steam_id = request.COOKIES.get("steam_id", None)
    player_achievements = owned_Games(steam_id).get_player_achievements(appid)
    game_achievements = owned_Games(steam_id).get_game_achievements(appid)
    
    return render(request, 'games_achievements.html', {'player_achievements': player_achievements, 'game_achievements': game_achievements})




#do a check for empty list returned incase of a try catch error in api fetch in each of the html page
#check player and game achievements and render complete incomplete
#frontend
