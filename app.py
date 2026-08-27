import pandas as pd

from src.preprocessing import (
    preprocess_movies,
    create_tfidf_matrix,
)

from src.recommender import recommend_movies


# 1. Load data
movies = pd.read_csv("data/Movie.csv", sep="\t")


# 2. Preprocess data
movies = preprocess_movies(movies)


# 3. Vectorization
matrix = create_tfidf_matrix(movies)


# 4. Choose movie
movie_index = 27278


# 5. Recommendation
recommendations = recommend_movies(
    movies=movies,
    matrix=matrix,
    movie_index=movie_index,
    top_n=100
)

print("\nSelected movie:")
print(movies.loc[movie_index, "title"])

print("\nRecommendations:")
print(recommendations)