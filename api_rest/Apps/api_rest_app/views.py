from http.client import ImproperConnectionState
from sre_constants import SUCCESS
from django.http.response import JsonResponse
from django.shortcuts import render
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views import View
from .models import *
import json

# Create your views here.
class WarView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        wars = list(War.objects.values())
        if len(wars)>0:
            data = {'message': "Success", 'wars': wars}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        War.objects.create(W_date=jd['W_date'], W_duedate=jd['W_duedate'])
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        wars = list(War.objects.filter(id=id).values())
        if len(wars)>0:
            war = War.objects.get(id=id)
            war.W_date = jd['W_date']
            war.W_duedate = jd['W_duedate']
            war.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        wars = list(War.objects.filter(id=id).values())
        if len(wars)>0:
            War.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class GuildView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Guild.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'guilds': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Guild.objects.create(
            G_name=jd['G_name'], 
            G_type=jd['G_type'], 
            G_description=jd['G_description'], 
            region=jd['region'], 
            trophies=jd['trophies'], 
            needTrophies=jd['needTrophies']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Guild.objects.filter(id=id).values())
        if len(all)>0:
            elem = Guild.objects.get(id=id)
            elem.G_name=jd['G_name']
            elem.G_type=jd['G_type']
            elem.G_description=jd['G_description']
            elem.region=jd['region']
            elem.trophies=jd['trophies']
            elem.needTrophies=jd['needTrophies']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Guild.objects.filter(id=id).values())
        if len(all)>0:
            Guild.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class CardView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Card.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Cards': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Card.objects.create(
            C_name=jd['C_name'], 
            C_description=jd['C_description'], 
            aviableLocation=jd['aviableLocation'], 
            C_quality=jd['C_quality'], 
            elixirCount=jd['elixirCount'], 
            initialLevel=jd['initialLevel']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Card.objects.filter(id=id).values())
        if len(all)>0:
            elem = Card.objects.get(id=id)
            elem.C_name=jd['C_name']
            elem.C_description=jd['C_description']
            elem.aviableLocation=jd['aviableLocation']
            elem.C_quality=jd['C_quality']
            elem.elixirCount=jd['elixirCount']
            elem.initialLevel=jd['initialLevel']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Card.objects.filter(id=id).values())
        if len(all)>0:
            Card.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class ChallengeView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Challenge.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Challenges': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Challenge.objects.create(
            ch_name=jd['ch_name'], 
            ch_description=jd['ch_description'], 
            ch_dueDate=jd['ch_dueDate'], 
            ch_date=jd['ch_date'], 
            ch_minLevel=jd['ch_minLevel'], 
            ch_cost=jd['ch_cost'], 
            ch_masPrices=jd['ch_masPrices']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Challenge.objects.filter(id=id).values())
        if len(all)>0:
            elem = Challenge.objects.get(id=id)
            elem.ch_name=jd['ch_name']
            elem.ch_description=jd['ch_description']
            elem.ch_dueDate=jd['ch_dueDate']
            elem.ch_date=jd['ch_date']
            elem.ch_minLevel=jd['ch_minLevel']
            elem.ch_cost=jd['ch_cost']
            elem.ch_masPrices=jd['ch_masPrices']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Challenge.objects.filter(id=id).values())
        if len(all)>0:
            Challenge.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class DonationView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Donation.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Donations': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Donation.objects.create(
            D_P_ID=jd['D_P_ID'], 
            D_G_ID=jd['D_G_ID'], 
            D_C_ID=jd['D_C_ID'], 
            donationCount=jd['donationCount']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Donation.objects.filter(id=id).values())
        if len(all)>0:
            elem = Donation.objects.get(id=id)
            elem.D_P_ID=jd['D_P_ID']
            elem.D_G_ID=jd['D_G_ID']
            elem.D_C_ID=jd['D_C_ID']
            elem.donationCount=jd['donationCount']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Donation.objects.filter(id=id).values())
        if len(all)>0:
            Donation.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class PlayerView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Player.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Players': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Player.objects.create(
            nickname=jd['nickname'], 
            prefCard=jd['prefCard'], 
            P_gold=jd['P_gold'], 
            P_gems=jd['P_gems'],
            P_level=jd['P_level'], 
            P_trophies=jd['P_trophies'], 
            trophiesMax=jd['trophiesMax'], 
            winCount=jd['winCount']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Player.objects.filter(id=id).values())
        if len(all)>0:
            elem = Player.objects.get(id=id)
            elem.nickname=jd['nickname']
            elem.prefCard=jd['prefCard']
            elem.P_gold=jd['P_gold']
            elem.P_gems=jd['P_gems']
            elem.P_level=jd['P_level']
            elem.P_trophies=jd['P_trophies']
            elem.trophiesMax=jd['trophiesMax']
            elem.winCount=jd['winCount']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Player.objects.filter(id=id).values())
        if len(all)>0:
            Player.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class Is_War_MatchView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Is_War_Match.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Is_War_Matchs': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Is_War_Match.objects.create(
            IWM_W_ID=jd['IWM_W_ID'], 
            IWM_M_ID=jd['IWM_M_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Is_War_Match.objects.filter(id=id).values())
        if len(all)>0:
            elem = Is_War_Match.objects.get(id=id)
            elem.IWM_W_ID=jd['IWM_W_ID']
            elem.IWM_M_ID=jd['IWM_M_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Is_War_Match.objects.filter(id=id).values())
        if len(all)>0:
            Is_War_Match.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
 
class MatchView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Match.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Matchs': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Match.objects.create(
            M_duration=jd['M_duration'], 
            P1_ID=jd['P1_ID'], 
            P2_ID=jd['P2_ID'], 
            M_date=jd['M_date'], 
            M_trophies=jd['M_trophies']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Match.objects.filter(id=id).values())
        if len(all)>0:
            elem = Match.objects.get(id=id)
            elem.M_duration=jd['M_duration']
            elem.P1_ID=jd['P1_ID']
            elem.P2_ID=jd['P2_ID']
            elem.M_date=jd['M_date']
            elem.M_trophies=jd['M_trophies']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Match.objects.filter(id=id).values())
        if len(all)>0:
            Match.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
     
class ParticipateView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Participate.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Participates': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Participate.objects.create(
            P_W_ID=jd['P_W_ID'], 
            P_G_ID=jd['P_G_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Participate.objects.filter(id=id).values())
        if len(all)>0:
            elem = Participate.objects.get(id=id)
            elem.P_W_ID=jd['P_W_ID']
            elem.P_G_ID=jd['P_G_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Participate.objects.filter(id=id).values())
        if len(all)>0:
            Participate.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class Player_CardView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Player_Card.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Player_Cards': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Player_Card.objects.create(
            PC_P_ID=jd['PC_P_ID'], 
            PC_C_ID=jd['PC_C_ID'], 
            PC_goldNeeded=jd['PC_goldNeeded'], 
            PC_cardNeeded=jd['PC_cardNeeded'], 
            PC_count=jd['PC_count'], 
            PC_currentLevel=jd['PC_currentLevel']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Player_Card.objects.filter(id=id).values())
        if len(all)>0:
            elem = Player_Card.objects.get(id=id)
            elem.PC_P_ID=jd['PC_P_ID']
            elem.PC_C_ID=jd['PC_C_ID']
            elem.PC_goldNeeded=jd['PC_goldNeeded']
            elem.PC_cardNeeded=jd['PC_cardNeeded']
            elem.PC_count=jd['PC_count']
            elem.PC_currentLevel=jd['PC_currentLevel']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Player_Card.objects.filter(id=id).values())
        if len(all)>0:
            Player_Card.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
class Player_ChallengeView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Player_Challenge.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Player_Challenges': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Player_Challenge.objects.create(
            PCH_P_ID=jd['PCH_P_ID'], 
            PCH_CH_ID=jd['PCH_CH_ID'], 
            winCount=jd['winCount']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Player_Challenge.objects.filter(id=id).values())
        if len(all)>0:
            elem = Player_Challenge.objects.get(id=id)
            elem.PCH_P_ID=jd['PCH_P_ID']
            elem.PCH_CH_ID=jd['PCH_CH_ID']
            elem.winCount=jd['winCount']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Player_Challenge.objects.filter(id=id).values())
        if len(all)>0:
            Player_Challenge.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
class Player_GuildView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Player_Guild.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Player_Guilds': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Player_Guild.objects.create(
            PG_P_ID=jd['PG_P_ID'], 
            PG_G_ID=jd['PG_G_ID'], 
            role=jd['role']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Player_Guild.objects.filter(id=id).values())
        if len(all)>0:
            elem = Player_Guild.objects.get(id=id)
            elem.PG_P_ID=jd['PG_P_ID']
            elem.PG_G_ID=jd['PG_G_ID']
            elem.role=jd['role']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Player_Guild.objects.filter(id=id).values())
        if len(all)>0:
            Player_Guild.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
class SpellView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Spell.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Spells': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Spell.objects.create(
            SP_ID=jd['SP_ID'], 
            SP_AoE=jd['SP_AoE'], 
            SP_areaDamage=jd['SP_areaDamage'], 
            SP_towerDamage=jd['SP_towerDamage'], 
            SP_duration=jd['SP_duration']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Spell.objects.filter(id=id).values())
        if len(all)>0:
            elem = Spell.objects.get(id=id)
            elem.SP_ID=jd['SP_ID']
            elem.SP_AoE=jd['SP_AoE']
            elem.SP_areaDamage=jd['SP_areaDamage']
            elem.SP_towerDamage=jd['SP_towerDamage']
            elem.SP_duration=jd['SP_duration']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Spell.objects.filter(id=id).values())
        if len(all)>0:
            Spell.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
class StructureView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Structure.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Structures': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Structure.objects.create(
            ST_ID=jd['ST_ID'], 
            ST_lifePoints=jd['ST_lifePoints'], 
            ST_areaDamage=jd['ST_areaDamage'], 
            ST_attackSpell=jd['ST_attackSpell']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Structure.objects.filter(id=id).values())
        if len(all)>0:
            elem = Structure.objects.get(id=id)
            elem.ST_ID=jd['ST_ID']
            elem.ST_lifePoints=jd['ST_lifePoints']
            elem.ST_areaDamage=jd['ST_areaDamage']
            elem.ST_attackSpell=jd['ST_attackSpell']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Structure.objects.filter(id=id).values())
        if len(all)>0:
            Structure.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
class TroopView(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Troop.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Troops': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Troop.objects.create(
            T_ID=jd['T_ID'], 
            T_lifePoints=jd['T_lifePoints'], 
            T_areaDamage=jd['T_areaDamage'], 
            T_unitCount=jd['T_unitCount']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Troop.objects.filter(id=id).values())
        if len(all)>0:
            elem = Troop.objects.get(id=id)
            elem.T_ID=jd['T_ID']
            elem.T_lifePoints=jd['T_lifePoints']
            elem.T_areaDamage=jd['T_areaDamage']
            elem.T_unitCount=jd['T_unitCount']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Troop.objects.filter(id=id).values())
        if len(all)>0:
            Troop.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
#flkdg
class Query_WarPlayersView(View):
    
    @method_decorator(csrf_exempt)
    def get(self,request,war_id):
        # print(Is_War_Match.objects.filter(IWM_W_ID=war_id).values())
        data1 = {'message': "Success"}
        all=list(((Is_War_Match.objects.filter(IWM_M_ID__P2_ID__nickname__contains="")).filter(IWM_W_ID=war_id)).select_related('P2_ID').values())
        all=list(Is_War_Match.objects.all().select_related('IWM_M_ID').values())
        print(Is_War_Match.objects.filter(IWM_M_ID__P2_ID__nickname__contains="").filter(IWM_W_ID=war_id).select_related('P2_ID').values())
        data = {'message': "Success", 'Consult': all}
        return JsonResponse(data)
        