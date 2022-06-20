from dataclasses import fields
from pyexpat import model
from warnings import filters
from .models import *
from django_filters import rest_framework as filters

class PlayerFilter(filters.FilterSet):
    nickname= filters.CharFilter(lookup_expr='icontains')
    prefCard= filters.NumberFilter()
    P_gold= filters.NumberFilter()
    P_gems= filters.NumberFilter()
    P_level= filters.NumberFilter()
    P_trophies= filters.NumberFilter()
    trophiesMax= filters.NumberFilter()
    winCount= filters.NumberFilter()

    class Meta:
        model = Player
        fields = ['nickname','prefCard','P_gold','P_gems', 'P_level', 'P_trophies', 'trophiesMax', 'winCount']

class GuildFilter(filters.FilterSet):
    G_name= filters.CharFilter(lookup_expr='icontains')
    G_type= filters.CharFilter(lookup_expr='icontains')
    G_description= filters.CharFilter(lookup_expr='icontains')
    region= filters.CharFilter(lookup_expr='icontains')
    trophies= filters.NumberFilter()
    needTrophies= filters.NumberFilter()

    class Meta:
        model = Guild
        fields = ['G_name','G_type','G_description','region', 'trophies', 'needTrophies']
        
class CardFilter(filters.FilterSet):
    C_name= filters.CharFilter(lookup_expr='icontains')
    C_description= filters.CharFilter(lookup_expr='icontains')
    aviableLocation= filters.CharFilter(lookup_expr='icontains')
    C_quality= filters.CharFilter(lookup_expr='icontains')
    elixirCount= filters.NumberFilter()
    initialLevel= filters.NumberFilter()

    class Meta:
        model = Card
        fields = ['C_name','C_description','aviableLocation','C_quality', 'elixirCount', 'initialLevel']

class WarFilter(filters.FilterSet):
    W_date= filters.DateFromToRangeFilter()
    W_duedate= filters.DateFromToRangeFilter()

    class Meta:
        model = War
        fields = ['W_date','W_duedate']
    
    @property
    def qs(self):
        parent = super().qs
        clanIds=self.request.GET.get('clanIds','')

        if clanIds!='':
            clanIds=[int(x) for x in clanIds.split(',')]
            warIds=[ part['P_W_ID_id'] for part in Participate.objects.filter(P_G_ID__in=clanIds).values()]
            parent=parent.filter(id__in=warIds).all()
        return parent

class ChallengeFilter(filters.FilterSet):
    ch_name= filters.CharFilter(lookup_expr='icontains')
    ch_description= filters.CharFilter(lookup_expr='icontains')
    ch_dueDate= filters.DateFromToRangeFilter()
    ch_date= filters.DateFromToRangeFilter()
    ch_minLevel= filters.NumberFilter()
    ch_cost= filters.NumberFilter()
    ch_maxPrices=filters.NumberFilter()

    class Meta:
        model = Challenge
        fields = ['ch_name','ch_description','ch_dueDate','ch_date', 'ch_minLevel', 'ch_cost', 'ch_maxPrices']

    @property
    def qs(self):
        parent = super().qs
        completed=self.request.GET.get('completed','')

        if completed=='true':
            completedChIds=[ PCH['PCH_CH_ID_id'] for PCH in Player_Challenge.objects.values()]
            parent=parent.filter(id__in=completedChIds).all()
        return parent