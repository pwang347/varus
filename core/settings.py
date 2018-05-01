import datetime

BASE_API_URL = "https://%s.api.riotgames.com/lol"
DEFAULT_REGION = "na1"
REGIONS = [
	DEFAULT_REGION,
	"ru",
	"kr",
	"br1",
	"oc1",
	"jp1",
	"eun1",
	"euw1",
	"tr1",
	"la1",
	"la2",
]
MILLISECONDS_TO_SECONDS = 1000
UPDATE_COOLDOWN = 600
LOG_FILE = "out.log"

def convert_unix_timestamp(date):
	return datetime.datetime.utcfromtimestamp(date / MILLISECONDS_TO_SECONDS).strftime('%Y-%m-%dT%H:%M:%SZ')

SUMMONER_MAPPING = {
	"profileIconId": "profile_icon_id",
	"summonerLevel": "summoner_level",
	"accountId": "account_id",
	"id": "summoner_id",
	"revisionDate": (
		"revision_date",
		convert_unix_timestamp,
	),
}

CHAMPION_MASTERY_MAPPING = {
	"chestGranted": "chest_granted",
	"championLevel": "champion_level",
	"championPoints": "champion_points",
	"championId": "champion_id",
	"playerId": "summoner_id",
	"championPointsUntilNextLevel": "champion_points_until_next_level",
	"tokensEarned": "tokens_earned",
	"championPointsSinceLastLevel": "champion_points_since_last_level",
	"lastPlayTime": (
		"last_play_time",
		convert_unix_timestamp,
	),
}

CHAMPION_MAPPING = {
	"name": "name",
	"title": "title",
	"id": "champion_id",
}
