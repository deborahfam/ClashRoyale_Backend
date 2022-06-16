from msilib.schema import Class
from rest_framework import serializers
from .models import *

class PlayerSerializer(serializers.ModelSerializer):

    guild = serializers.SerializerMethodField()
    prefCardDetails = serializers.SerializerMethodField()
    participatedMatches = serializers.SerializerMethodField()
    ownedCards = serializers.SerializerMethodField()
    availableClans = serializers.SerializerMethodField()

    def get_guild(self, obj : Player):
        if type(self.instance)!=Player and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        availables=list(Player_Guild.objects.filter(PG_P_ID=id).values())
        if len(availables)>0:
            pair=availables[0]
            guild=list(Guild.objects.filter(id=pair['PG_G_ID_id']).values())[0]
            return guild
        else :
            return None

    def get_prefCardDetails(self, obj : Player):
        if type(self.instance)!=Player and len(self.instance)>2:
            return "Not queried"
        id=int(obj.prefCard.id)
        availables=list(Card.objects.filter(id=id).values())
        if len(availables)>0:
            return availables[0]
        else :
            return None

    def get_participatedMatches(self, obj : Player):
        if type(self.instance)!=Player and len(self.instance)>2:
            return "Not queried"
        id=int(obj.id)
        availables=list(Match.objects.filter(P1_ID_id=id).values())+list(Match.objects.filter(P2_ID_id=id).values())
        return availables

    def get_ownedCards(self, obj : Player):
        if type(self.instance)!=Player and len(self.instance)>2:
            return "Not queried"
        id=int(obj.id)
        availables=list(Player_Card.objects.filter(PC_P_ID_id=id).values())
        return availables

    def get_availableClans(self, obj : Player):
        if type(self.instance)!=Player and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        availables=list(Player_Guild.objects.filter(PG_P_ID=id).values())
        if len(availables)>0:
            return "Already belongs to a clan"
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
        if type(self.instance)!=Guild and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)>0:
            memberList = []
            for memberId in memberListId:
                memberList.append(Player.objects.filter(id=memberId).values())
            return memberList
        else :
            return []

    def get_bestStructureCard(self, obj : Guild):
        if type(self.instance)!=Guild and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values())

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            member=member[0]
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

        return best_card
        
    def get_bestTroopCard(self, obj : Guild):
        if type(self.instance)!=Guild and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values())

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            member=member[0]
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

        return best_card

    def get_bestSpellCard(self, obj : Guild):
        if type(self.instance)!=Guild and len(self.instance)>2:
            return "Not queried"
        id=obj.id
        memberListId=[ PG['PG_P_ID_id'] for PG in list(Player_Guild.objects.filter(PG_G_ID=id).values())]
        if len(memberListId)==0:
            return None
        memberList = []
        for memberId in memberListId:
            memberList.append(Player.objects.filter(id=memberId).values())

        freqs = dict()
        best_card = None
        best_freq = 0
        for member in memberList:
            member=member[0]
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

        return best_card
    
    def get_bestPlayers(self, obj : Guild):
        if type(self.instance)!=Guild and len(self.instance)>2:
            return "Not queried"
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
            bestPlayers.append(Player.objects.filter(id=(-val)%(int(1e10))).values())
        
        return bestPlayers
        

    class Meta:
        model=Guild
        fields = '__all__'