from django.http.response import JsonResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from requests import Response
from .models import *
from .serializers import *
from api_rest.pagination import CRPagination
from api_rest.serializers import get_serializer
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import RetrieveUpdateDestroyAPIView, ListCreateAPIView, GenericAPIView

# Create your views here.
class ListDashboardAPIView(ListCreateAPIView):
    serializer_class = DashboardSerializer
    queryset = Dashboard.objects.all()
    pagination_class = None

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
    search_fields = ['C_name']
class RetrieveUpdateDestroyCardAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filterset_fields = '__all__'
    search_fields = ['C_name']

class ListCreateChallengeAPIView(ListCreateAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = ['ch_name', 'ch_description']
class RetrieveUpdateDestroyChallengeAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    filterset_fields = '__all__'
    search_fields = ['ch_name', 'ch_description']

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
class bestPlayersforClanView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=PlayerSerializer
    pagination_class=CRPagination
    
    def get_queryset(self):
        id=self.kwargs['pk']   
        clansIds=[x['P_G_ID_id'] for x in Participate.objects.filter(P_W_ID_id=id).values()]
        playerIds=[]
        players=[]
        for i in range(len(clansIds)):
            playerIds.append([x['PG_P_ID_id'] for x in Player_Guild.objects.filter(PG_G_ID_id=clansIds[i]).values() ])
            players.append(Player.objects.filter(id__in=playerIds[i]).order_by('-P_trophies').values()[0]['id'])
        return Player.objects.filter(id__in=players).all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#2. Conocer el clan con mejor desempeño durante las guerras por región del mundo, es decir,
#por cada región obtener el clan con mayor cantidad de trofeos. WORKING

class bestClanView(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=GuildSerializer
    pagination_class=CRPagination
    
    def get_queryset(self):
        regions = set([ guild['region'] for guild in Guild.objects.values()])
        bestGuildIds = []
        for region in regions:
            bestGuildIds.append(Guild.objects.filter(region=region).order_by('-trophies').values()[0]['id'])
        return Guild.objects.filter(id__in=bestGuildIds).all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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

class mostFavoriteCards(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CardSerializer
    pagination_class=CRPagination
    filterset_fields = None
    
    def get_queryset(self):
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
        
        for p in players_card:
            if troop == False:
                for t in troops:
                    if t['T_ID_id'] == p[1]:
                        best.append(t['T_ID_id'])
                        troop = True
            elif spell == False:
                for t in spells:
                    if t['SP_ID_id'] == p[1]:
                        best.append(t['SP_ID_id'])
                        spell = True
            elif structure == False:
                for t in structures:
                    if t['ST_ID_id'] == p[1]:
                        best.append(t['ST_ID_id'])
                        structure = True
        
        return Card.objects.filter(id__in=best).all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#5. Dado un jugador saber a qué clanes se puede unir, conociendo los requisitos de cada clan. WORKING

class playersJoinClan(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=GuildSerializer
    pagination_class=CRPagination
    filterset_fields = '__all__'
    
    def get_queryset(self):
        pk=self.kwargs['pk']

        player = Player.objects.get(id=pk)
        guilds = list(Guild.objects.values())
        guilds_matches = []
        for d in guilds:
            if d['needTrophies'] <= player.P_trophies:
                guilds_matches.append(d['id'])

        guilds_matches=Guild.objects.filter(id__in=guilds_matches).values()
        return guilds_matches
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#6. Los desafíos donde haya participado al menos un jugador que lo haya completado. WORKING

class challengesWinners(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=ChallengeSerializer
    pagination_class=CRPagination
    filterset_fields = '__all__'
    
    def get_queryset(self):
        ids=[ PCH['PCH_CH_ID_id'] for PCH in Player_Challenge.objects.values()]
        return Challenge.objects.filter(id__in=ids).all()
    
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)