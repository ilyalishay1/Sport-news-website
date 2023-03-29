from django.urls import path
from news import views


urlpatterns = [
    path('', views.home, name='home'),
    path('football/', views.football, name='football'),
    path('basketball/', views.basketball, name='basketball'),
    path('hockey/', views.hockey, name='hockey'),
    path('tennis/', views.tennis, name='tennis'),
    path('mma/', views.mma, name='mma'),
    path('biathlon/', views.biathlon, name='biathlon'),
    path('add_post/', views.add_post, name='add_post'),
    path('football/epl/', views.epl, name='epl'),
    path('football/laliga/', views.laliga, name='laliga'),
    path('football/seria_a/', views.seria_a, name='seria_a'),
    path('football/bundesliga/', views.bundesliga, name='bundesliga'),
    path('football/ligue1/', views.ligue1, name='ligue1'),
    path('football/ucl/', views.ucl, name='ucl'),
    path('hockey/nhl/', views.nhl, name='nhl'),
    path('hockey/hockey_by/', views.hockey_by, name='hockey_by'),
    path('hockey/nba/', views.nba, name='nba'),
    path('hockey/euroleague/', views.euroleague, name='euroleague'),
]
