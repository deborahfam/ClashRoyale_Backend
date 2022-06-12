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

class UserView(View):    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(User.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Users': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        User.objects.create(
            U_name=jd['U_name'], 
            U_email=jd['U_email'], 
            U_password=jd['U_password'], 
            U_role=jd['U_role']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(User.objects.filter(id=id).values())
        if len(all)>0:
            elem = User.objects.get(id=id)
            elem.U_name=jd['U_name']
            elem.U_email=jd['U_email']
            elem.U_password=jd['U_password']
            elem.U_role=jd['U_role']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(User.objects.filter(id=id).values())
        if len(all)>0:
            User.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class ScopesManagement(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Scopes.objects.create(
            SC_name=jd['SC_name']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = Scopes.objects.get(id=id)
            elem.SC_name=jd['SC_name']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Scopes.objects.filter(id=id).values())
        if len(all)>0:
            Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

class User_Scopes(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(User_Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'User_Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        User_Scopes.objects.create(
            SC_ID=jd['SC_ID'], 
            U_ID=jd['U_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(User_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = User_Scopes.objects.get(id=id)
            elem.SC_ID=jd['SC_ID']
            elem.U_ID=jd['U_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(User_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            User_Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class Roles_Scopes(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Roles_Scopes.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Roles_Scopes': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Roles_Scopes.objects.create(
            SC_ID=jd['SC_ID'], 
            R_ID=jd['R_ID']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Roles_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            elem = Roles_Scopes.objects.get(id=id)
            elem.SC_ID=jd['SC_ID']
            elem.R_ID=jd['R_ID']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Roles_Scopes.objects.filter(id=id).values())
        if len(all)>0:
            Roles_Scopes.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class RolesManagement(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(Roles.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'Roles': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        Roles.objects.create(
            R_name=jd['R_name']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(Roles.objects.filter(id=id).values())
        if len(all)>0:
            elem = Roles.objects.get(id=id)
            elem.R_name=jd['R_name']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(Roles.objects.filter(id=id).values())
        if len(all)>0:
            Roles.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
class OAuth(View):
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request):
        all = list(OAuth.objects.values())
        if len(all)>0:
            data = {'message': "Success", 'OAuths': all}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
    def post(self,request):
        jd = json.loads(request.body)
        OAuth.objects.create(
            OA_token=jd['OA_token'], 
            OA_date=jd['OA_date']
        )
        data={'message':'Success'}
        return JsonResponse(data)
    
    def put(self,request,id):
        jd = json.loads(request.body)
        all = list(OAuth.objects.filter(id=id).values())
        if len(all)>0:
            elem = OAuth.objects.get(id=id)
            elem.OA_token=jd['OA_token']
            elem.OA_date=jd['OA_date']
            elem.save()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

    def delete(self,request,id):
        all = list(OAuth.objects.filter(id=id).values())
        if len(all)>0:
            OAuth.objects.filter(id=id).delete()
            data = {'message': "Success"}
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
    
# 6 Consult
#1. Conocer los mejores jugadores que participan en una guerra, es decir, por cada clan que
#participa en una guerra obtener el jugador con más trofeos.
class bestPlayersforClanView(View):
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

class bestClanView(View):
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
class mostDonatedCards(View):
    
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

class mostFavoriteCards(View):
    
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

class playersJoinClan(View):
    
    @method_decorator(csrf_exempt)    
    def get(self, request, id):        
        player = list(Player.objects.filter(id=id).values())
        guilds = list(Guild.objects.values())
        guilds_matches = []
        if len(guilds)>0:
            for d in guilds:
                if d.NeedTrophies <= player.P_trophies:
                    guilds_matches.append(d)
            for gm in guilds_matches:
                count = list(Player_Guild.objects.filter(id = gm.id).values().count())
                if(count==50):
                    guilds_matches.remove(gm)
            data = {'message': "Success", 'Guilds Matches': guilds_matches}   
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)

#6. Los desafíos donde haya participado al menos un jugador que lo haya completado.

class challengesWinners(View):
    
    @method_decorator(csrf_exempt)    
    def get(self, request):        
        challengeW = list(Player_Challenge.objects.values())
        if len(challengeW)>0:
            data = {'message': "Success", 'Most Donated Card': challengeW}   
            
        else:
            data = {'message': "Fail"}
        return JsonResponse(data)
