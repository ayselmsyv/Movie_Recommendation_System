import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

def genre_similarity(movie_a, movie_b):
    movie_a_genres = set(movie_a["genres"].split("|"))
    movie_b_genres = set(movie_b["genres"].split("|"))

    # Calculate similarity between two movies
    intersection = len(movie_a_genres & movie_b_genres)
    union = len(movie_a_genres.union(movie_b_genres))

    if union == 0:
        return 0
    
    return intersection / union

def recommend_movies(movies, matrix, movie_index, top_n=5):
    movie_vector = matrix[movie_index]

    similarities = cosine_similarity(
        movie_vector,
        matrix
    ).flatten()

    # sort
    sorted_indexes = similarities.argsort()[::-1]
    # exclude original movie
    sorted_indexes = [
        index
        for index in sorted_indexes
        if index != movie_index
    ]
    # select top_n
    top_indexes = sorted_indexes[:top_n]

    recommendations = movies.iloc[top_indexes][
    ["movieId", "title", "genres"]
    ].copy()

    recommendations["score"] = similarities[top_indexes]

    return recommendations.reset_index(drop=True)
    # return movies + scores
    






















# from sklearn.feature_extraction.text import TfidfVectorizer

# corpus = ["good boy", "good girl", "good boy girl"]
# vectorizer = TfidfVectorizer()
# X = vectorizer.fit_transform(corpus)
# print(vectorizer.get_feature_names_out())
# print(X.toarray())

# '''
# Output:
# [[0.78980693 0.         0.61335554]
#  [0.         0.78980693 0.61335554]
#  [0.61980538 0.61980538 0.48133417]]

# Inside this array of array the first number represents boy, the second number 
# represents girl and the third number represents good

# The length of the words in the corpus is 3 and they are arranged in ascending 
# order
# '''