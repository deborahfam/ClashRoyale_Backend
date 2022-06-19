from msilib.schema import Class
from requests import request
from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):

    clan = serializers.SerializerMethodField()
    prefCardDetails = serializers.SerializerMethodField()
    participatedMatches = serializers.SerializerMethodField()
    ownedCards = serializers.SerializerMethodField()
    availableClans = serializers.SerializerMethodField()

    def get_clan(self, obj : Player):
        id=obj.id
        availables=list(Player_Guild.objects.filter(PG_P_ID=id).values())
        if len(availables)>0:
            pair=availables[0]
            guild=list(Guild.objects.filter(id=pair['PG_G_ID_id']).values())[0]
            return guild
        else :
            return None

    def get_prefCardDetails(self, obj : Player):
        id=int(obj.prefCard.id)
        availables=list(Card.objects.filter(id=id).values())
        if len(availables)>0:
            return availables[0]
        else :
            return None

    def get_participatedMatches(self, obj : Player):
        id=int(obj.id)
        availables=list(Match.objects.filter(P1_ID_id=id).values())+list(Match.objects.filter(P2_ID_id=id).values())
        return availables

    def get_ownedCards(self, obj : Player):
        id=int(obj.id)
        availables=list(Player_Card.objects.filter(PC_P_ID_id=id).values())
        return availables

    def get_availableClans(self, obj : Player):
        id=obj.id
        availables=list(Player_Guild.objects.filter(PG_P_ID=id).values())
        if len(availables)>0:
            return []
        else :
            guilds = list(Guild.objects.values())
            guilds_matches = []
            if len(guilds)>0:
                for d in guilds:
                    if d['needTrophies'] <= obj.P_trophies:
                        guilds_matches.append(d)
            return guilds_matches

    class Meta:
        model=Player
        fields = '__all__'


class GuildSerializer(serializers.ModelSerializer):

    members = serializers.SerializerMethodField()
    bestStructureCard = serializers.SerializerMethodField()
    bestTroopCard = serializers.SerializerMethodField()
    bestSpellCard = serializers.SerializerMethodField()
    bestPlayers = serializers.SerializerMethodField()

    def get_members(self, obj : Guild):
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values()[0])
        return memberList

    def get_bestStructureCard(self, obj : Guild):
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values()[0])

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            cardId = member['prefCard_id']
            if cardId not in freqs.keys():
                freqs[cardId]=0

            card = list(Structure.objects.filter(id=cardId).values())

            if len(card)==0:
                continue
            
            freqs[cardId]+=1

            if freqs[cardId]>best_freq:
                best_freq=freqs[cardId]
                best_card=card[0]
                
        best_card['timesPrefered']=freqs[best_card['id']]
        return best_card
        
    def get_bestTroopCard(self, obj : Guild):
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values()[0])

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            cardId = member['prefCard_id']
            if cardId not in freqs.keys():
                freqs[cardId]=0

            card = list(Troop.objects.filter(id=cardId).values())
            
            if len(card)==0:
                continue
            
            freqs[cardId]+=1

            if freqs[cardId]>best_freq:
                best_freq=freqs[cardId]
                best_card=card[0]

        best_card['timesPrefered']=freqs[best_card['id']]
        return best_card

    def get_bestSpellCard(self, obj : Guild):
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values()[0])

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            cardId = member['prefCard_id']
            if cardId not in freqs.keys():
                freqs[cardId]=0

            card = list(Spell.objects.filter(id=cardId).values())
            
            if len(card)==0:
                continue
            
            freqs[cardId]+=1

            if freqs[cardId]>best_freq:
                best_freq=freqs[cardId]
                best_card=card[0]

        best_card['timesPrefered']=freqs[best_card['id']]
        return best_card
    
    def get_bestPlayers(self, obj : Guild):
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None

        to_sort = []
        for memberId in memberListId:
            player = Player.objects.filter(id=memberId).values()[0]
            to_sort.append(player['P_trophies']*(-1e10)-player['id'])
        
        to_sort.sort()

        bestPlayers = []
        for i in range(0, min(len(to_sort), 5)):
            val=to_sort[i]
            bestPlayers.append(Player.objects.filter(id=(-val)%(int(1e10))).values()[0])
        
        return bestPlayers
        

    class Meta:
        model=Guild
        fields = '__all__'


class WarSerializer(serializers.ModelSerializer):

    participatingClans = serializers.SerializerMethodField()

    def get_participatingClans(self, obj : War):
        id=obj.id
        participatingListId=[ WG['P_G_ID_id'] for WG in list(Participate.objects.filter(P_W_ID=id).values())]
        participatingList = []
        for participatingId in participatingListId:
            participatingList.append(Guild.objects.filter(id=participatingId).values()[0])

        return participatingList

    class Meta:
        model=War
        fields = '__all__'


class ChallengeSerializer(serializers.ModelSerializer):

    topWinners = serializers.SerializerMethodField()

    def get_topWinners(self, obj : Challenge):
        id=obj.id
        participatingListVals=[ PCH['winCount']*(-1e10)-PCH['PCH_P_ID_id'] for PCH in list(Player_Challenge.objects.filter(PCH_CH_ID=id).values())]
        
        participatingListVals.sort()

        topWinnersList = []
        for i in range(0, min(len(participatingListVals),5)):
            partipatingVal=participatingListVals[i]
            winner = Player.objects.filter(id=(-partipatingVal)%(int(1e10))).values()[0]
            winner['challengeWinCount'] = int((-partipatingVal)/(int(1e10)))
            topWinnersList.append(winner)

        return topWinnersList

    class Meta:
        model=Challenge
        fields = '__all__'


class CardSerializer(serializers.ModelSerializer):

    topOwners = serializers.SerializerMethodField()
    topOwnersWhoPrefered = serializers.SerializerMethodField()
    timesOwned = serializers.SerializerMethodField()
    timesPrefered = serializers.SerializerMethodField()
    cardType = serializers.SerializerMethodField()

    def get_topOwners(self, obj : Card):
        id=obj.id
        owners=[ Player.objects.filter(id=PC['PC_P_ID_id']).values('id','P_trophies')[0] for PC in list(Player_Card.objects.filter(PC_C_ID_id=id).values())]

        to_sort=[]
        for owner in owners:
            to_sort.append(owner['P_trophies']*(-1e10)-owner['id'])

        to_sort.sort()

        topOwnersList = []
        for i in range(0, min(len(to_sort),5)):
            ownerVal=to_sort[i]
            winner = Player.objects.filter(id=(-ownerVal)%(int(1e10))).values()[0]
            topOwnersList.append(winner)

        return topOwnersList

    def get_topOwnersWhoPrefered(self, obj : Card):
        id=obj.id
        to_sort=[ player['P_trophies']*(-1e10)-player['id'] for player in list(Player.objects.filter(prefCard=id).values())]

        to_sort.sort()

        topOwnersPrefList = []
        for i in range(0, min(len(to_sort),5)):
            ownerVal=to_sort[i]
            winner = Player.objects.filter(id=(-ownerVal)%(int(1e10))).values()[0]
            topOwnersPrefList.append(winner)

        return topOwnersPrefList
    
    def get_timesOwned(self, obj : Card):
        id=obj.id
        return len(list(Player_Card.objects.filter(PC_C_ID_id=id).values()))
    
    def get_timesPrefered(self, obj : Card):
        id=obj.id
        return len(list(Player.objects.filter(prefCard=id).values()))

    def get_cardType(self, obj : Card):
        if len(list(Troop.objects.filter(T_ID_id=obj.id).all()))>0:
            return "Troop"
        if len(list(Spell.objects.filter(SP_ID_id=obj.id).all()))>0:
            return "Spell"
        if len(list(Structure.objects.filter(ST_ID_id=obj.id).all()))>0:
            return "Structure"
        return None

    class Meta:
        model=Card
        fields = '__all__'


class DashboardSerializer(serializers.Serializer):
    
    popularCards = serializers.SerializerMethodField()
    topClans = serializers.SerializerMethodField()
    topPlayers = serializers.SerializerMethodField()

    def get_popularCards(self, obj : Dashboard):
        querySet=Card.objects.all()
        request = self.context['request']

        popCname=request.GET.get('popCname','')
        popCdesc=request.GET.get('popCdesc','')
        popCloc=request.GET.get('popCloc','')
        popCqual=request.GET.get('popCqual','')

        if popCname!='':
            querySet=querySet.filter(C_name__contains=popCname).all()
        if popCdesc!='':
            querySet=querySet.filter(C_description__contains=popCdesc).all()
        if popCloc!='':
            querySet=querySet.filter(aviableLocation__contains=popCloc).all()
        if popCqual!='':
            querySet=querySet.filter(C_quality__contains=popCqual).all()
        
        freqs = dict()
        for player in Player.objects.values():
            id = player['prefCard_id']
            if id not in freqs.keys():
                freqs[id]=0
            freqs[id]+=1

        to_sort=[]
        for id in freqs.keys():
            to_sort.append(freqs[id]*(-1e10)-id)

        to_sort.sort()

        popularCardsList = []
        for i in range(0, min(len(to_sort),5)):
            cardVal=to_sort[i]
            list = querySet.filter(id=(-cardVal)%(int(1e10))).values()
            if len(list)>0:
                winner = list[0]
                winner['timesPrefered'] = int((-cardVal)/(1e10))
                popularCardsList.append(winner)

        return popularCardsList
    
    def get_topClans(self, obj : Dashboard):
        querySet=Guild.objects.all()
        request = self.context['request']

        topGname=request.GET.get('topGname','')
        topGdesc=request.GET.get('topGdesc','')
        topGreg=request.GET.get('topGreg','')

        if topGname!='':
            querySet=querySet.filter(G_name__contains=topGname).all()
        if topGdesc!='':
            querySet=querySet.filter(G_description__contains=topGdesc).all()
        if topGreg!='':
            querySet=querySet.filter(region__contains=topGreg).all()
        
        return list(querySet.order_by('-trophies').values()[:5])
    
    def get_topPlayers(self, obj : Dashboard):
        querySet=Player.objects.all()
        request = self.context['request']

        topPnick=request.GET.get('topPnick','')

        if topPnick!='':
            querySet=querySet.filter(nickname__contains=topPnick).all()
        
        return list(querySet.order_by('-P_trophies').values()[:5])


class MostDonatedCardRegionSerializer(serializers.Serializer):

    region = serializers.SerializerMethodField()
    card = serializers.SerializerMethodField()

    def get_region(self, obj : Donation):
        return Guild.objects.filter(id=obj.D_G_ID_id).values()[0]['region']

    def get_card(self, obj : Donation):
        return Card.objects.filter(id=obj.D_C_ID_id).values()[0]

    class Meta:
        model=Donation
        fields = []