import pandas as pd
import numpy as np
from scipy.sparse.linalg import svds

from core.models import Summoner, Champion, ChampionInfo, ChampionStats, ChampionTag, ChampionMastery

def train():
	mastery_list = ChampionMastery.objects.all().values("summoner_id", "champion_id", "champion_points")
	champions_list = Champion.objects.all().values("champion_id", "name")
	champion_info_list = ChampionInfo.objects.all().values("champion_id", "difficulty", "attack", "defense", "magic")
	champion_stats_list = ChampionStats.objects.all().values("champion_id", "attackrange")

	ratings_df = pd.DataFrame.from_records(mastery_list, columns=["summoner_id", "champion_id", "champion_points"]).pivot_table(index="summoner_id", columns="champion_id", values="champion_points")
	user_ratings_mean = np.array(ratings_df.mean(axis=1))
	ratings_demeaned = ratings_df.sub(ratings_df.mean(axis=1), axis=0)
	ratings_demeaned = ratings_demeaned.fillna(0).as_matrix()

	champion_name_df = pd.DataFrame.from_records(champions_list, columns=["champion_id", "name"]).set_index("champion_id")
	champion_info_df = pd.DataFrame.from_records(champion_info_list, columns=["champion_id", "difficulty", "attack", "defense", "magic"]).set_index("champion_id")
	champion_stats_df = pd.DataFrame.from_records(champion_stats_list, columns=["champion_id", "attackrange"]).set_index("champion_id")
	champions_df = pd.concat([champion_name_df, champion_info_df, champion_stats_df], axis=1)
	
	U, sigma, Vt = svds(ratings_demeaned, k=5)
	sigma = np.diag(sigma)
	all_user_predicted_ratings = np.dot(np.dot(U, sigma), Vt) + user_ratings_mean.reshape(-1, 1)
	preds_df = pd.DataFrame(all_user_predicted_ratings, columns=ratings_df.columns)
	
	return ratings_df, champions_df, preds_df
