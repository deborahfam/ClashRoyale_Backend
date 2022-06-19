from django.db import models
from django import forms
from datetime import date

# Create your models here.

class War(models.Model):
    W_date = models.DateField()
    W_duedate = models.DateField()
    
class Guild(models.Model):
    G_name = models.CharField(max_length=50)
    G_type = models.CharField(max_length=50)
    G_description = models.TextField(max_length=1000)
    region = models.CharField(max_length=50)
    trophies = models.IntegerField()
    needTrophies = models.IntegerField()
    
class Card(models.Model):
    C_name= models.CharField(max_length=50)
    C_description  = models.TextField(max_length=1000)
    aviableLocation = models.CharField(max_length=50)
    C_quality =models.CharField(max_length=50) 
    elixirCount = models.IntegerField()
    initialLevel= models.IntegerField()

    def __str__(self):
        return self.C_name
    
class Challenge(models.Model):
    ch_name= models.CharField(max_length=50)
    ch_description = models.TextField(max_length=1000)
    ch_dueDate= models.DateField()
    ch_date= models.DateField()
    ch_minLevel= models.IntegerField()
    ch_cost= models.IntegerField()
    ch_masPrices= models.IntegerField()
    
class Donation(models.Model):
    D_P_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    D_G_ID= models.ForeignKey(
        'Guild',
        on_delete=models.CASCADE,
    )
    D_C_ID= models.ForeignKey(
        'Card',
        on_delete=models.CASCADE,
    )
    donationCount= models.IntegerField()
    donationDate = models.DateField(default=date.today)
    
class Player(models.Model):
    nickname= models.CharField(max_length=20)
    prefCard= models.ForeignKey(
        'Card',
        on_delete=models.CASCADE,
    )
    P_gold= models.IntegerField()
    P_gems= models.IntegerField()
    P_level= models.IntegerField()
    P_trophies= models.IntegerField()
    trophiesMax= models.IntegerField()
    winCount= models.IntegerField()

    def __str__(self):
        return self.nickname
    
class Is_War_Match(models.Model):
    IWM_W_ID= models.ForeignKey(
        'War',
        on_delete=models.CASCADE,
    )
    IWM_M_ID= models.ForeignKey(
        'Match',
        on_delete=models.CASCADE,
    )

class Match(models.Model):
    M_duration= models.IntegerField()
    P1_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='Player_1',
    )
    P2_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
        related_name='Player_2',
    )
    M_date= models.DateField()
    M_trophies= models.IntegerField()

class Participate(models.Model):
    P_W_ID= models.ForeignKey(
        'War',
        on_delete=models.CASCADE,
    )
    P_G_ID= models.ForeignKey(
        'Guild',
        on_delete=models.CASCADE,
    )

class Player_Card(models.Model):
    PC_P_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    PC_C_ID= models.ForeignKey(
        'Card',
        on_delete=models.CASCADE,
    )
    PC_goldNeeded= models.IntegerField()
    PC_cardNeeded= models.IntegerField()
    PC_count= models.IntegerField()
    PC_currentLevel= models.IntegerField()

class Player_Challenge(models.Model):
    PCH_P_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    PCH_CH_ID= models.ForeignKey(
        'Challenge',
        on_delete=models.CASCADE,
    )
    winCount= models.IntegerField()

class Player_Guild(models.Model):
    PG_P_ID= models.ForeignKey(
        'Player',
        on_delete=models.CASCADE,
    )
    PG_G_ID= models.ForeignKey(
        'Guild',
        on_delete=models.CASCADE,
    )
    role=models.CharField(max_length=45)

class Spell(models.Model):
    SP_ID= models.ForeignKey(
            'Card',
            on_delete=models.CASCADE,
        )
    SP_AoE= models.IntegerField()
    SP_areaDamage= models.IntegerField()
    SP_towerDamage= models.IntegerField()
    SP_duration= models.IntegerField()

class Structure(models.Model):
    ST_ID= models.ForeignKey(
            'Card',
            on_delete=models.CASCADE,
        )
    ST_lifePoints= models.IntegerField()
    ST_areaDamage= models.IntegerField()
    ST_attackSpell= models.IntegerField()

class Troop(models.Model):
    T_ID= models.ForeignKey(
            'Card',
            on_delete=models.CASCADE,
        )
    T_lifePoints= models.IntegerField()
    T_areaDamage= models.IntegerField()
    T_unitCount= models.IntegerField()

class Dashboard(models.Model):
    pass