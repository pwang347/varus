import pandas as pd

def recommend_champion(predictions_df, summoner_id, champions_df, original_ratings_df, num_recommendations=5):
	user_row_number = original_ratings_df.index.get_loc(summoner_id)
	sorted_user_predictions = predictions_df.iloc[user_row_number].sort_values(ascending=False)
	user_data = original_ratings_df.iloc[user_row_number]
	user_full = pd.DataFrame({"champion_id": user_data.index, "champion_points": user_data.values}).set_index("champion_id").join(champions_df, how="outer").sort_values(["champion_points"], ascending=False)
	user_full = user_full[pd.notnull(user_full["champion_points"])]
	not_owned = champions_df["not_owned"] = [not i in user_full.index for i in champions_df.index.values]
	recommendations = champions_df[champions_df["not_owned"] == True].reset_index().merge(pd.DataFrame(sorted_user_predictions).reset_index(), how='left', left_on='champion_id', right_on='champion_id').rename(columns = {user_row_number: 'predictions'}).sort_values('predictions', ascending = False).iloc[:num_recommendations, :-1]
	return recommendations
