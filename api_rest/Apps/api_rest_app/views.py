from http.client import ImproperConnectionState
from sre_constants import SUCCESS
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
from .serializers import *
import json
from api_rest.pagination import CRPagination
from api_rest.serializers import get_serializer
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView

# Create your views here.
class ListCreatePlayerAPIView(ListCreateAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = ['nickname']
class RetrieveUpdateDestroyPlayerAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    filterset_fields = '__all__'
    search_fields = ['nickname']

class ListCreateWarAPIView(ListCreateAPIView):
    serializer_class = WarSerializer
    queryset = War.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = ['W_date']
class RetrieveUpdateDestroyWarAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = WarSerializer
    queryset = War.objects.all()
    filterset_fields = '__all__'
    search_fields = ['W_date']

class ListCreateGuildAPIView(ListCreateAPIView):
    serializer_class = GuildSerializer
    # serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = ['G_name']
class RetrieveUpdateDestroyGuildAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = GuildSerializer
    # serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    filterset_fields = '__all__'
    search_fields = ['G_name']

class ListCreateCardAPIView(ListCreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyCardAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filterset_fields = '__all__'
    search_fields = []

class ListCreateChallengeAPIView(ListCreateAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyChallengeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChallengeSerializer
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

#1. Conocer los mejores jugadores que participan en una guerra, es decir, por cada clan que
#participa en una guerra obtener el jugador con más trofeos.
class bestPlayersforClanView(GenericAPIView):
    permission_classes=[IsAuthenticated]

    @method_decorator(csrf_exempt)    
    def get(self, request, id):        
        war_matches = list(Is_War_Match.objects.filter(IWM_W_ID=id).values())
        guild_players=[]
        if len(war_matches)>0:
            for wm in war_matches:
                match = Match.objects.get(id = wm['IWM_M_ID_id'])
                p1 = Player.objects.get(id=match.P1_ID_id)
                p2 = Player.objects.get(id=match.P2_ID_id)
                exist1 = False
                exist2 = False
                
                if(Player_Guild.objects.filter(PG_P_ID_id=p1.id).exists()):
                    g1 = Player_Guild.objects.get(PG_P_ID_id=p1.id)
                    exist1 = True
                if(Player_Guild.objects.filter(PG_P_ID_id=p2.id).exists()):
                    g2 = Player_Guild.objects.get(PG_P_ID_id=p2.id)
                    exist2 = True
                matcheo = False
                if len(guild_players)>0:
                    for gp in guild_players:
                        print(gp)
                        if(exist1 and gp[0].id == g1.PG_G_ID_id):
                            matcheo = True
                            if(gp[1].P_trophies < p1.P_trophies):
                                gp[1] = p1
                        elif(exist2 and gp[0].id == g2.PG_G_ID_id):
                            matcheo = True
                            if(gp[1] < p2.P_trophies):
                                gp[1] = p2
                    if matcheo == False:
                        if(exist1):
                            guild_players.append([g1.PG_G_ID, p1])
                        if(exist2):    
                            guild_players.append([g2.PG_G_ID, p2])
                    matcheo = False
                else:
                    if(exist1):
                        guild_players.append([g1.PG_G_ID,p1])
                    if(exist2):
                        guild_players.append([g2.PG_G_ID,p2])
                result = []
                for x in guild_players:
                    print(x)
                    result.append([x[0].G_name, x[1].nickname, x[1].P_trophies])
            data = {'message': "Success", 'Guild': result}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#2. Conocer el clan con mejor desempeño durante las guerras por región del mundo, es decir,
#por cada región obtener el clan con mayor cantidad de trofeos. WORKING

class bestClanView(GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)
    def get(self, request):        
        guilds = list(Guild.objects.values())
        region_guilds = []
        match = False
        if len(guilds)>0:
            for guild in guilds:
                if(len(region_guilds) > 0):
                    for x in region_guilds:
                        print(x[0])
                        print(guild['region'])
                        print()
                        if(x[0] == guild['region']):
                            match=True
                            if x[2]['trophies'] < guild['trophies']:
                                x[2] = guild
                                x[0] = guild['trophies']
                            break
                    if match==False:
                        region_guilds.append([guild['trophies'],guild['region'], guild]) 
                    match=False                           
                else:
                    region_guilds.append([guild['trophies'],guild['region'], guild ])
                region_guilds.sort(reverse=True)
                data = {'message': "Success", 'Best Guild By Region Trophies': region_guilds[0][0], 'Region': region_guilds[0][1]}
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)


#3. La carta o las cartas más donadas por región en el último mes. WORKING
class mostDonatedCards(GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        donations = list(Donation.objects.values())
        card_count = []
        match = False
        if len(donations)>0:
            for d in donations:
                card = Card.objects.get(id = (d)['D_C_ID_id'])
                if len(card_count) > 0:
                    for c in card_count:
                        print(c)
                        if(c[1] == card.id):
                            c[0] = c[0]+1
                            match = True
                    if match == False:
                        card_count.append([1,card.id])
                    match = False
                else:
                    card_count.append([1,card.id])
            card_count.sort()
            returncard = Card.objects.get(id = card_count[card_count.count(1)-1][1])
            data = {'message': "Success", 'Most Donated Card Name': returncard.C_name, 'ID': returncard.id}       
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#4. La carta más popular de cada tipo dentro de cada clan existente. Hint: de cada jugador se
#conoce su carta favorita :) WORKING

class mostFavoriteCards(GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        players = list(Player.objects.values())
        players_card = []
        best = []
        troop = False
        spell = False
        structure = False
        troops = list(Troop.objects.values())
        spells = list(Spell.objects.values())
        structures = list(Structure.objects.values())
        match = False
        if len(players)>0:            
            for p in players:
                if len(players_card)> 0:
                    for pc in players_card:
                        if(pc[1] == p['prefCard_id']):
                            pc[0] = pc[0]+1
                            match = True
                    if match==False:
                        players_card.append([1,p['prefCard_id']])
                    match= False
                else:
                    players_card.append([1,p['prefCard_id']])
            
            players_card.sort(reverse=True)
            print(players_card)
            
            for p in players_card:
                if troop == False:
                    for t in troops:
                        if t['T_ID_id'] == p[1]:
                            best.append(['Troop',(Card.objects.get(id=t['T_ID_id'])).C_name, 'Favorite of', p[0], 'players'])
                            troop = True
                elif spell == False:
                    for t in spells:
                        if t['SP_ID_id'] == p[1]:
                            best.append(['Spell',(Card.objects.get(id=t['SP_ID_id'])).C_name,'Favorite of', p[0], 'players'])
                            spell = True
                            
                elif structure == False:
                    for t in structures:
                        if t['ST_ID_id'] == p[1]:
                            best.append(['Structure',(Card.objects.get(id=t['ST_ID_id'])).C_name,'Favorite of', p[0], 'players'])
                            structure = True
                        
            data = {'message': "Success", 'Most Donated Cards by Type': best}   
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#5. Dado un jugador saber a qué clanes se puede unir, conociendo los requisitos de cada clan. WORKING

class playersJoinClan(GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request, id):        
        player = Player.objects.get(id=id)
        guilds = list(Guild.objects.values())
        guilds_matches = []
        if len(guilds)>0:
            for d in guilds:
                if d['needTrophies'] <= player.P_trophies:
                    guilds_matches.append(d)
            data = {'message': "Success", 'Guilds Matches': guilds_matches}   
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#6. Los desafíos donde haya participado al menos un jugador que lo haya completado. WORKING

class challengesWinners(GenericAPIView):
    permission_classes=[IsAuthenticated]
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        challengeW = list(Player_Challenge.objects.values())
        if len(challengeW)>0:
            data = {'message': "Success", 'Challenge': challengeW}            
        else:
            data = {'message': "There is not challenges to show"}
        return JsonResponse(data)
