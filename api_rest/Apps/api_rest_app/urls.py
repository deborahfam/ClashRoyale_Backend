from django.urls import path
from .views import *

urlpatterns = [
    path('wars/', ListCreateWarAPIView.as_view()),
    path('wars/<pk>', RetrieveUpdateDestroyWarAPIView.as_view()),
    path('guilds/', ListCreateGuildAPIView.as_view()),
    path('guilds/<pk>', RetrieveUpdateDestroyGuildAPIView.as_view()),
    path('cards/', ListCreateCardAPIView.as_view()),
    path('cards/<pk>', RetrieveUpdateDestroyCardAPIView.as_view()),
    path('challenges/', ListCreateChallengeAPIView.as_view()),
    path('challenges/<pk>', RetrieveUpdateDestroyChallengeAPIView.as_view()),
    path('players/', ListCreatePlayerAPIView.as_view()),
    path('players/<pk>', RetrieveUpdateDestroyPlayerAPIView.as_view()),
    path('simple_wars/', ListCreatesimple_WarAPIView.as_view()),
    path('simple_wars/<pk>', RetrieveUpdateDestroysimple_WarAPIView.as_view()),
    path('simple_guilds/', ListCreatesimple_GuildAPIView.as_view()),
    path('simple_guilds/<pk>', RetrieveUpdateDestroysimple_GuildAPIView.as_view()),
    path('simple_cards/', ListCreatesimple_CardAPIView.as_view()),
    path('simple_cards/<pk>', RetrieveUpdateDestroysimple_CardAPIView.as_view()),
    path('simple_challenges/', ListCreatesimple_ChallengeAPIView.as_view()),
    path('simple_challenges/<pk>', RetrieveUpdateDestroysimple_ChallengeAPIView.as_view()),
    path('simple_players/', ListCreatesimple_PlayerAPIView.as_view()),
    path('simple_players/<pk>', RetrieveUpdateDestroysimple_PlayerAPIView.as_view()),
    path('donations/', ListCreateDonationAPIView.as_view()),
    path('donations/<pk>', RetrieveUpdateDestroyDonationAPIView.as_view()),
    path('is_war_matchs/', ListCreateIs_War_MatchAPIView.as_view()),
    path('is_war_matchs/<pk>', RetrieveUpdateDestroyIs_War_MatchAPIView.as_view()),
    path('matchs/', ListCreateMatchAPIView.as_view()),
    path('matchs/<pk>', RetrieveUpdateDestroyMatchAPIView.as_view()),
    path('participates/', ListCreateParticipateAPIView.as_view()),
    path('participates/<pk>', RetrieveUpdateDestroyParticipateAPIView.as_view()),
    path('player_cards/', ListCreatePlayer_CardAPIView.as_view()),
    path('player_cards/<pk>', RetrieveUpdateDestroyPlayer_CardAPIView.as_view()),
    path('player_challenges/', ListCreatePlayer_ChallengeAPIView.as_view()),
    path('player_challenges/<pk>', RetrieveUpdateDestroyPlayer_ChallengeAPIView.as_view()),
    path('player_guilds/', ListCreatePlayer_GuildAPIView.as_view()),
    path('player_guilds/<pk>', RetrieveUpdateDestroyPlayer_GuildAPIView.as_view()),
    path('spells/', ListCreateSpellAPIView.as_view()),
    path('spells/<pk>', RetrieveUpdateDestroySpellAPIView.as_view()),
    path('structures/', ListCreateStructureAPIView.as_view()),
    path('structures/<pk>', RetrieveUpdateDestroyStructureAPIView.as_view()),
    path('troops/', ListCreateTroopAPIView.as_view()),
    path('troops/<pk>', RetrieveUpdateDestroyTroopAPIView.as_view()),
    path('challenges_winners', challengesWinners.as_view()),
    path('players_join_clan/<pk>', playersJoinClan.as_view()),
    path('most_favorite_cards', mostFavoriteCards.as_view()),
    path('most_donated_cards_by_region', mostDonatedCards.as_view()),
    path('best_clan_by_region', bestClanView.as_view()),
    path('best_players_for_clan_at_war/<pk>', bestPlayersforClanView.as_view()),
    path('dashboard', ListDashboardAPIView.as_view())
]