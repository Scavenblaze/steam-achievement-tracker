from django.urls import path

from Achievement_Tracker import views

urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('home/', views.home, name='home'),
    path('landing_page/', views.landing_page, name='landing_page'),
    path('games_list/', views.games_list, name='games_list'),
    path('games_achievements/', views.games_achievements, name='games_achievements'),
    
]
