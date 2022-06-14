from http.client import ImproperConnectionState
from sre_constants import SUCCESS
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json
from api_rest.pagination import CRPagination
from api_rest.serializers import get_serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView

# Create your views here.
class ListCreateWarAPIView(ListCreateAPIView):
    serializer_class = get_serializer(War)
    queryset = War.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyWarAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(War)
    queryset = War.objects.all()
    filterset_fields = '__all__'
    search_fields = []


class ListCreateGuildAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyGuildAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateCardAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Card)
    queryset = Card.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyCardAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Card)
    queryset = Card.objects.all()
    filterset_fields = '__all__'
    search_fields = []


class ListCreateChallengeAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Challenge)
    queryset = Challenge.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyChallengeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Challenge)
    queryset = Challenge.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateDonationAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Donation)
    queryset = Donation.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyDonationAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Donation)
    queryset = Donation.objects.all()
    filterset_fields = '__all__'
    search_fields = []

    
class ListCreatePlayerAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Player)
    queryset = Player.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyPlayerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Player)
    queryset = Player.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateIs_War_MatchAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Is_War_Match)
    queryset = Is_War_Match.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyIs_War_MatchAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Is_War_Match)
    queryset = Is_War_Match.objects.all()
    filterset_fields = '__all__'
    search_fields = []


class ListCreateMatchAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Match)
    queryset = Match.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyMatchAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Match)
    queryset = Match.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateParticipateAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Participate)
    queryset = Participate.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyParticipateAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Participate)
    queryset = Participate.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreatePlayer_CardAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Player_Card)
    queryset = Player_Card.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyPlayer_CardAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Player_Card)
    queryset = Player_Card.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreatePlayer_ChallengeAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Player_Challenge)
    queryset = Player_Challenge.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyPlayer_ChallengeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Player_Challenge)
    queryset = Player_Challenge.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreatePlayer_GuildAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Player_Guild)
    queryset = Player_Guild.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyPlayer_GuildAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Player_Guild)
    queryset = Player_Guild.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateSpellAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Spell)
    queryset = Spell.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroySpellAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Spell)
    queryset = Spell.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateStructureAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Structure)
    queryset = Structure.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyStructureAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Structure)
    queryset = Structure.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateTroopAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Troop)
    queryset = Troop.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyTroopAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = get_serializer(Troop)
    queryset = Troop.objects.all()
    filterset_fields = '__all__'
    search_fields = []

# 6 Consult
#1. Conocer los mejores jugadores que participan en una guerra, es decir, por cada clan que
#participa en una guerra obtener el jugador con más trofeos.
class bestPlayersforClanView(APIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request, id):        
        war_matches = list(Is_War_Match.objects.filter(IWM_W_ID=id).values())
        guild_players=[]
        if len(war_matches)>0:
            for wm in war_matches:
                match = wm.IWM_M_ID
                p1 = match.P1_ID
                g1 = list(Player_Guild.objects.filter(PG_P_ID=p1).values())
                p2 = match.P2_ID
                g2 = list(Player_Guild.objects.filter(PG_P_ID=p2.values()))
                
                if guild_players.count>0:
                    if(guild_players[0].ID == g1.PG_G_ID):
                        if(guild_players[1] < g1.PG_P_IG.P_trophies):
                            guild_players[1] = g1.PG_P_IG.P_trophies
                    elif(guild_players[0].ID == g2.PG_G_ID):
                        if(guild_players[1] < g2.PG_P_IG.P_trophies):
                            guild_players[1] = g2.PG_P_IG.P_trophies
                    else:
                        guild_players.append(g1.PG_G_ID,g1.PG_P_ID)
                        guild_players.append(g2.PG_G_ID,g2.PG_P_ID)
                else:
                    guild_players.append(g1.PG_G_ID,g1.PG_P_ID)
                    guild_players.append(g2.PG_G_ID,g2.PG_P_ID)
                    
            data = {'message': "Success", 'War': guild_players}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#2. Conocer el clan con mejor desempeño durante las guerras por región del mundo, es decir,
#por cada región obtener el clan con mayor cantidad de trofeos.

class bestClanView(APIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)
    def get(self, request):        
        guilds = list(Guild.objects.values())
        region_guilds = []
        if len(guilds)>0:
            for guild in guild:
                if(region_guilds.count() > 0):
                    for x in region_guilds:
                        if(x[0] == guild.region):
                            x[1] = max(x[1].trophies, guild.trophies)
                else:
                    region_guilds.append((guild.region, guild))
                data = {'message': "Success", 'Best Guild By Region = Region + Guild ID': region_guilds}
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)


#3. La carta o las cartas más donadas por región en el último mes.
class mostDonatedCards(APIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        donations = list(Donation.objects.values())
        card_count = []
        if len(donations)>0:
            for d in donations:
                if card_count.count > 0:
                    if(card_count[0]==d.card):
                        d[1] = d[1]+1
                    else:
                        card_count.append([d.card,0])
                else:
                    card_count.append([d.card,0])
            card_count.sort(reverse=True)
            data = {'message': "Success", 'Most Donated Card': card_count[0][0]}   
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#4. La carta más popular de cada tipo dentro de cada clan existente. Hint: de cada jugador se
#conoce su carta favorita :)

class mostFavoriteCards(APIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        players = list(Player.objects.values())
        players_card = []
        if len(players)>0:
            for p in players:
                if players_card.count > 0:
                    if(players_card[1]==p.prefCard.C_name):
                        p[2] = p[2]+1
                    else:
                        players_card.append([p.prefCard,p.prefCard.C_name,0])
                else:
                    players_card.append([p.prefCard,p.prefCard.C_name,0])
            players_card.sort(reverse=True)
            best = []
            troop = False
            spell = False
            structure = False
            troops = list(Troop.objects.values())
            spells = list(Spell.objects.values())
            structures = list(Structure.objects.values())
            for p in players_card:
                if troop == False:
                    for t in troops:
                        if t.id == p[0].id:
                            best.append(['Troop',p[1]])
                            troop = True
                if spell == False:
                    for t in spells:
                        if t.id == p[0].id:
                            best.append(['Spell',p[1]])
                            spell = True
                            
                if structure == False:
                    for t in structures:
                        if t.id == p[0].id:
                            best.append(['Structure',p[1]])
                            structure = True
                        
            data = {'message': "Success", 'Most Donated Cards by Type': best}   
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#5. Dado un jugador saber a qué clanes se puede unir, conociendo los requisitos de cada clan.

class playersJoinClan(APIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request, id):        
        player = Player.objects.get(id=id)
        print(player.nickname)
        guilds = list(Guild.objects.values())
        guilds_matches = []
        if len(guilds)>0:
            for d in guilds:
                print(d)
                if d['needTrophies'] <= player.P_trophies:
                    guilds_matches.append(d)
            data = {'message': "Success", 'Guilds Matches': guilds_matches}   
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#6. Los desafíos donde haya participado al menos un jugador que lo haya completado.

class challengesWinners(APIView):
    permission_classes=[IsAuthenticated]

    @method_decorator(csrf_exempt)    
    def get(self, request):        
        challengeW = list(Player_Challenge.objects.values())
        if len(challengeW)>0:
            data = {'message': "Success", 'Most Donated Card': challengeW}   
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
