from django.db import models
from django.utils import timezone
import datetime

class Summoner(models.Model):
	profile_icon_id = models.IntegerField()
	name = models.CharField(max_length=30, unique=True)
	summoner_level = models.BigIntegerField()
	account_id = models.BigIntegerField(unique=True)
	summoner_id = models.BigIntegerField(unique=True)
	revision_date = models.DateTimeField()
	last_updated = models.DateTimeField(default=timezone.now)

class Champion(models.Model):
	name = models.CharField(max_length=30, unique=True)
	title = models.CharField(max_length=30)
	champion_id = models.BigIntegerField(unique=True)

class ChampionInfo(models.Model):
	champion_id = models.IntegerField(unique=True)
	difficulty = models.IntegerField()
	attack = models.IntegerField()
	defense = models.IntegerField()
	magic = models.IntegerField()

class ChampionStats(models.Model):
	champion_id = models.BigIntegerField(unique=True)
	version = models.CharField(max_length=30)
	armorperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	hpperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	attackdamage = models.DecimalField(decimal_places=3, max_digits=10)
	mpperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	attackspeedoffset = models.DecimalField(decimal_places=3, max_digits=10)
	armor = models.DecimalField(decimal_places=3, max_digits=10)
	hp = models.DecimalField(decimal_places=3, max_digits=10)
	hpregenperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	spellblock = models.DecimalField(decimal_places=3, max_digits=10)
	attackrange = models.DecimalField(decimal_places=3, max_digits=10)
	movespeed = models.DecimalField(decimal_places=3, max_digits=10)
	attackdamageperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	mpregenperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	mp = models.DecimalField(decimal_places=3, max_digits=10)
	spellblockperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	crit = models.DecimalField(decimal_places=3, max_digits=10)
	mpregen = models.DecimalField(decimal_places=3, max_digits=10)
	attackspeedperlevel = models.DecimalField(decimal_places=3, max_digits=10)
	hpregen = models.DecimalField(decimal_places=3, max_digits=10)
	critperlevel = models.DecimalField(decimal_places=3, max_digits=10)

class ChampionTag(models.Model):
	champion_id = models.BigIntegerField()
	name = models.CharField(max_length=30)

	class Meta:
		unique_together = ('champion_id', 'name')

class ChampionMastery(models.Model):
	chest_granted = models.BooleanField(default=False)
	champion_level = models.IntegerField()
	champion_points = models.IntegerField()
	champion_id = models.BigIntegerField()
	summoner_id = models.BigIntegerField()
	champion_points_until_next_level = models.BigIntegerField()
	tokens_earned = models.IntegerField()
	champion_points_since_last_level = models.BigIntegerField()
	last_play_time = models.DateTimeField()
	last_updated = models.DateTimeField(default=timezone.now)

	class Meta:
		unique_together = ('summoner_id', 'champion_id')
