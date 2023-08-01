import pandas as pd
pd.set_option('display.max_columns', None)
# df = pd.read_csv("ml-latest-small\\ratings.csv", sep=',')
# def rat_of_film(grade):
#     result = ""
#     if grade <= 2:
#         result = "низкий рейтинг"
#     elif 2 < grade <= 4:
#         result = "средний рейтинг"
#     elif 4 < grade <= 5:
#         result = "высокий рейтинг"
#     return result
#
# ratings = df.groupby('movieId').mean().reset_index()
# ratings["class"] = ratings["rating"].apply(rat_of_film)
# print(ratings.head(10))                                   #Первое задание

# db = pd.read_csv("ml-latest-small\\keywords.csv", sep=',')
# geo_data = {
# 'Центр': ['москва', 'тула', 'ярославль'],
#
# 'Северо-Запад': ['петербург', 'псков', 'мурманск'],
#
# 'Дальний Восток': ['владивосток', 'сахалин', 'хабаровск']
# }
# def region_name(city):
#     region = "undefined"
#     for key, value in geo_data.items():
#         if city in value:
#             region = key
#     return region
#
# db["region"] = db.keyword.apply(region_name)
#
# print(db["region"].unique())                              #Второе задание

df_ratings = pd.read_csv("ml-25m\\ratings.csv")
df_movies = pd.read_csv("ml-25m\\movies.csv")

years = list(range(1950, 2011))

def production_year(row):
    for year in years:
        if str(year) in row:
            return year
    else:
        return 1900

df_movies["year"] = df_movies["title"].apply(production_year)
df_ratings = df_ratings.groupby("movieId").mean().reset_index()

df_mov_and_rat = pd.merge(df_ratings, df_movies, on="movieId")
print(df_mov_and_rat.groupby('year')['rating'].mean().reset_index().sort_values('rating', ascending=False).head())






