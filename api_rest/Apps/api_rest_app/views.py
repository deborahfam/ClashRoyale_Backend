from datetime import datetime, date
from django.http.response import JsonResponse
from django.shortcuts import _get_queryset
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
from .filters import *

# Create your views here.
def get_object_or_500(klass, *args, **kwargs):
    """
    Use get() to return an object, or raise an Http404 exception if the object
    does not exist.

    klass may be a Model, Manager, or QuerySet object. All other passed
    arguments and keyword arguments are used in the get() query.

    Like with QuerySet.get(), MultipleObjectsReturned is raised if more than
    one object is found.
    """
    queryset = _get_queryset(klass)
    if not hasattr(queryset, "get"):
        klass__name = (
            klass.__name__ if isinstance(klass, type) else klass.__class__.__name__
        )
        raise ValueError(
            "First argument to get_object_or_404() must be a Model, Manager, "
            "or QuerySet, not '%s'." % klass__name
        )
    try:
        return queryset.get(*args, **kwargs)
    except queryset.model.DoesNotExist:
        raise Exception('No object matches this query')

class RetrieveUpdateDestroyAPIView500(RetrieveUpdateDestroyAPIView):
    def get_object(self):
        """
        Returns the object the view is displaying.

        You may want to override this if you need to provide non-standard
        queryset lookups.  Eg if objects are referenced using multiple
        keyword arguments in the url conf.
        """
        queryset = self.filter_queryset(self.get_queryset())

        # Perform the lookup filtering.
        lookup_url_kwarg = self.lookup_url_kwarg or self.lookup_field

        assert lookup_url_kwarg in self.kwargs, (
            'Expected view %s to be called with a URL keyword argument '
            'named "%s". Fix your URL conf, or set the `.lookup_field` '
            'attribute on the view correctly.' %
            (self.__class__.__name__, lookup_url_kwarg)
        )

        filter_kwargs = {self.lookup_field: self.kwargs[lookup_url_kwarg]}
        obj = get_object_or_500(queryset, **filter_kwargs)

        # May raise a permission denied
        self.check_object_permissions(self.request, obj)

        return obj

class ListRegionAPIView(ListCreateAPIView):
    serializer_class = RegionSerializer
    queryset = Dashboard.objects.all()
    pagination_class = None

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

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
    filterset_class = PlayerFilter
    search_fields = ['nickname']
class RetrieveUpdateDestroyPlayerAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = PlayerSerializer
    queryset = Player.objects.all()
    filterset_class = PlayerFilter
    search_fields = ['nickname']

class ListCreateWarAPIView(ListCreateAPIView):
    serializer_class = WarSerializer
    queryset = War.objects.all()
    pagination_class = CRPagination
    filterset_class = WarFilter
    search_fields = ['W_date']
class RetrieveUpdateDestroyWarAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = WarSerializer
    queryset = War.objects.all()
    filterset_class = WarFilter
    search_fields = ['W_date']

class ListCreateGuildAPIView(ListCreateAPIView):
    serializer_class = GuildSerializer
    queryset = Guild.objects.all()
    pagination_class = CRPagination
    filterset_class = GuildFilter
    search_fields = ['G_name']
class RetrieveUpdateDestroyGuildAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = GuildSerializer
    queryset = Guild.objects.all()
    filterset_class = GuildFilter
    search_fields = ['G_name']

class ListCreateCardAPIView(ListCreateAPIView):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    pagination_class = CRPagination
    filterset_class = CardFilter
    search_fields = ['C_name']
class RetrieveUpdateDestroyCardAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = CardSerializer
    queryset = Card.objects.all()
    filterset_class = CardFilter
    search_fields = ['C_name']

class ListCreateChallengeAPIView(ListCreateAPIView):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    pagination_class = CRPagination
    filterset_class = ChallengeFilter
    search_fields = ['ch_name', 'ch_description']
class RetrieveUpdateDestroyChallengeAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = ChallengeSerializer
    queryset = Challenge.objects.all()
    filterset_class = ChallengeFilter
    search_fields = ['ch_name', 'ch_description']

class ListCreatesimple_PlayerAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Player)
    queryset = Player.objects.all()
    pagination_class = CRPagination
    filterset_class = PlayerFilter
    search_fields = ['nickname']
class RetrieveUpdateDestroysimple_PlayerAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = get_serializer(Player)
    queryset = Player.objects.all()
    filterset_class = PlayerFilter
    search_fields = ['nickname']

class ListCreatesimple_WarAPIView(ListCreateAPIView):
    serializer_class = get_serializer(War)
    queryset = War.objects.all()
    pagination_class = CRPagination
    filterset_class = WarFilter
    search_fields = ['W_date']
class RetrieveUpdateDestroysimple_WarAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = get_serializer(War)
    queryset = War.objects.all()
    filterset_class = WarFilter
    search_fields = ['W_date']

class ListCreatesimple_GuildAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    pagination_class = CRPagination
    filterset_class = GuildFilter
    search_fields = ['G_name']
class RetrieveUpdateDestroysimple_GuildAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = get_serializer(Guild)
    queryset = Guild.objects.all()
    filterset_class = GuildFilter
    search_fields = ['G_name']

class ListCreatesimple_CardAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Card)
    queryset = Card.objects.all()
    pagination_class = CRPagination
    filterset_class = CardFilter
    search_fields = ['C_name']
class RetrieveUpdateDestroysimple_CardAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = get_serializer(Card)
    queryset = Card.objects.all()
    filterset_class = CardFilter
    search_fields = ['C_name']

class ListCreatesimple_ChallengeAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Challenge)
    queryset = Challenge.objects.all()
    pagination_class = CRPagination
    filterset_class = ChallengeFilter
    search_fields = ['ch_name', 'ch_description']
class RetrieveUpdateDestroysimple_ChallengeAPIView(RetrieveUpdateDestroyAPIView500):
    serializer_class = get_serializer(Challenge)
    queryset = Challenge.objects.all()
    filterset_class = ChallengeFilter
    search_fields = ['ch_name', 'ch_description']

class ListCreateDonationAPIView(ListCreateAPIView):
    serializer_class = get_serializer(Donation)
    queryset = Donation.objects.all()
    pagination_class = CRPagination
    filterset_fields = '__all__'
    search_fields = []
class RetrieveUpdateDestroyDonationAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyIs_War_MatchAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyMatchAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyParticipateAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyPlayer_CardAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyPlayer_ChallengeAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyPlayer_GuildAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroySpellAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyStructureAPIView(RetrieveUpdateDestroyAPIView500):
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
class RetrieveUpdateDestroyTroopAPIView(RetrieveUpdateDestroyAPIView500):
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
    
    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#3. La carta o las cartas más donadas por región en el último mes. WORKING
class mostDonatedCards(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=MostDonatedCardRegionSerializer
    pagination_class=CRPagination
    
    def get_queryset(self):     
        regions = set([ guild['region'] for guild in Guild.objects.values()])
        donationIds=[]
        for region in regions:
            donations=Donation.objects.filter(D_G_ID__region=region).all()
            freqs=dict()
            bestCard=None
            bestFreq=0
            for donation in donations.values():
                if (date.today()-donation['donationDate']).days>30:
                    continue
                if donation['D_C_ID_id'] not in freqs.keys():
                    freqs[donation['D_C_ID_id']]=0
                freqs[donation['D_C_ID_id']]+=donation['donationCount']
                if freqs[donation['D_C_ID_id']]>bestFreq:
                    bestCard=donation['D_C_ID_id']
            if bestCard!=None:
                donationIds.append(donations.filter(D_C_ID=bestCard).values()[0]['id'])
        return Donation.objects.filter(id__in=donationIds).all()

    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)

#4. La carta más popular de cada tipo dentro de cada clan existente. Hint: de cada jugador se
#conoce su carta favorita :) WORKING

class mostFavoriteCards(ListCreateAPIView):
    permission_classes=[IsAuthenticated]
    serializer_class=CardSerializer
    pagination_class=CRPagination
    
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
    
    def post(self, request, *args, **kwargs):
        return Response(status=status.HTTP_405_METHOD_NOT_ALLOWED)