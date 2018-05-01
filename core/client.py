from core.secrets import SecretManager
import core.settings as settings
from core.models import Summoner, Champion, ChampionInfo, ChampionStats, ChampionTag, ChampionMastery

from django.utils import timezone
from humanize import naturaldelta

import datetime
import logging
import requests
import urllib.parse

logging.basicConfig(filename=settings.LOG_FILE, level=logging.DEBUG)

class RiotClient(object):
	def __init__(self):
		self.sm = SecretManager()
		logging.info("Initialized client")

	def _call_riot_api(self, url, verb="GET", region=settings.DEFAULT_REGION, **kwargs):
		riot_api_key_header = {"X-Riot-Token": self.sm.RIOT_API_KEY}
		if not "headers" in kwargs:
			kwargs["headers"] = riot_api_key_header
		else:
			kwargs["headers"].update(riot_api_key_header)

		request_url = "%s/%s" % (settings.BASE_API_URL % region, url)
		response = requests.request(verb, url=request_url, **kwargs)

		if response.status_code != 200:
			raise Exception("Bad request [%s]:\n%s" % (response.status_code, response.text))

		return response.json()

	def _map_raw_data_keys(self, mapping, raw_data, last_updated=False):
		mapped_object = {}
		for old_key, value in mapping.items():
			if isinstance(value, str):
				mapped_object[value] = raw_data[old_key]
			elif isinstance(value, tuple):
				new_key, fn = value
				mapped_object[new_key] = fn(raw_data[old_key])
			else:
				raise Exception("Unexpected type: %s" % type(value))
		if last_updated:
			mapped_object["last_updated"] = timezone.now()
		return mapped_object

	def update_summoner_data(self, summoner_name):
		url = "summoner/v3/summoners/by-name/%s" % urllib.parse.quote(summoner_name)
		try:
			summoner = Summoner.objects.get(name=summoner_name)
			time_remaining = (summoner.last_updated + datetime.timedelta(seconds=settings.UPDATE_COOLDOWN)) - timezone.now()
			if time_remaining > datetime.timedelta(0):
				logging.info("Skipping update on %s...\nTime until next update: %s" % (summoner_name, naturaldelta(time_remaining)))
				return
		except Summoner.DoesNotExist:
			pass
		raw_summoner_data = self._call_riot_api(url)
		summoner_data = self._map_raw_data_keys(settings.SUMMONER_RAW_DATA_MAP, raw_summoner_data, last_updated=True)
		Summoner.objects.update_or_create(name=summoner_name, defaults=summoner_data)
		update_summoner_mastery_data(summoner_name)

	def update_summoner_mastery_data(self, summoner_name):
		summoner = Summoner.objects.get(name=summoner_name)
		url = "champion-mastery/v3/champion-masteries/by-summoner/%s" % summoner.summoner_id
		raw_mastery_data_list = self._call_riot_api(url)
		for raw_mastery_data in raw_mastery_data_list:
			mastery_data = self._map_raw_data_keys(settings.CHAMPION_MASTERY_MAPPING, raw_mastery_data, last_updated=True)
			ChampionMastery.objects.update_or_create(champion_id=mastery_data["champion_id"], defaults=mastery_data)

	def update_static_champion_data(self):
		url = "static-data/v3/champions"
		params = {
			"tags": ["info", "stats", "tags"],
		}
		raw_champion_data_list = self._call_riot_api(url, params=params)
		version = raw_champion_data_list["version"]
		for _, raw_champion_data in raw_champion_data_list["data"].items():
			champion_data = self._map_raw_data_keys(settings.CHAMPION_MAPPING, raw_champion_data)
			champion_id = champion_data["champion_id"]
			Champion.objects.get_or_create(champion_id=champion_id, defaults=champion_data)
			champion_info_data = raw_champion_data["info"]
			ChampionInfo.objects.get_or_create(champion_id=champion_id, defaults=champion_info_data)
			champion_stats_data = raw_champion_data["stats"]
			champion_stats_data["version"] = version
			ChampionStats.objects.update_or_create(champion_id=champion_id, defaults=champion_stats_data)
			champion_tag_data = raw_champion_data["tags"]
			for tag in champion_tag_data:
				ChampionTag.objects.get_or_create(champion_id=champion_id, name=tag)
