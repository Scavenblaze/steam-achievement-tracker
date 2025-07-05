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
    api_handler = owned_Games(steam_id)
    games_list = api_handler.get_recently_played()
    
    return render(request, 'home.html', {'steam_id': steam_id, 'games_list': games_list})


def games_list(request):
    steam_id = request.COOKIES.get("steam_id", None)
    api_handler = owned_Games(steam_id)
    games_list = api_handler.get_owned_games()
    
    return render(request, 'games_list.html', {'games_list': games_list})



#FIXME complete this render
def games_achievements(request):
    steam_id = request.COOKIES.get("steam_id", None)
    api_handler = owned_Games(steam_id)
    
    return render(request, 'games_achievements.html')






#get player achievements
#bind recently played and achievements
#bind games list with achievements