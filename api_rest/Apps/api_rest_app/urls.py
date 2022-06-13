from django.urls import path
from .views import *

urlpatterns = [
    # path('wars/', WarView.as_view()),
    # path('wars/<int:id>', WarView.as_view()),
    path('wars/', ListCreateWarAPIView.as_view()),
    path('wars/<pk>', RetrieveUpdateDestroyWarAPIView.as_view()),
    path('guilds/', GuildView.as_view()),
    path('guilds/<int:id>', GuildView.as_view()),
    path('cards/', CardView.as_view()),
    path('cards/<int:id>', CardView.as_view()),
    path('challenges/', ChallengeView.as_view()),
    path('challenges/<int:id>', ChallengeView.as_view()),
    path('donations/', DonationView.as_view()),
    path('donations/<int:id>', DonationView.as_view()),
    path('players/', PlayerView.as_view()),
    path('players/<int:id>', PlayerView.as_view()),
    path('is_war_matchs/', Is_War_MatchView.as_view()),
    path('is_war_matchs/<int:id>', Is_War_MatchView.as_view()),
    path('matchs/', MatchView.as_view()),
    path('matchs/<int:id>', MatchView.as_view()),
    path('participates/', ParticipateView.as_view()),
    path('participates/<int:id>', ParticipateView.as_view()),
    path('player_cards/', Player_CardView.as_view()),
    path('player_cards/<int:id>', Player_CardView.as_view()),
    path('player_challenges/', Player_ChallengeView.as_view()),
    path('player_challenges/<int:id>', Player_ChallengeView.as_view()),
    path('player_guilds/', Player_GuildView.as_view()),
    path('player_guilds/<int:id>', Player_GuildView.as_view()),
    path('spells/', SpellView.as_view()),
    path('spells/<int:id>', SpellView.as_view()),
    path('structures/', StructureView.as_view()),
    path('structures/<int:id>', StructureView.as_view()),
    path('troops/', TroopView.as_view()),
    path('troops/<int:id>', TroopView.as_view()),
    path('challengesWinners/', challengesWinners.as_view()),
    path('playersJoinClan/<id>', playersJoinClan.as_view())
]