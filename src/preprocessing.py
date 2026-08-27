from sklearn.feature_extraction.text import TfidfVectorizer


def preprocess_movies(movies):
    movies = movies.copy()

    movies["genres_clean"] = (
        movies["genres"]
        .fillna("")
        .str.replace("|", " ", regex=False)
        .str.lower()
    )

    movies = movies.reset_index(drop=True)

    return movies


def create_tfidf_matrix(movies):
    tfidf = TfidfVectorizer()

    matrix = tfidf.fit_transform(movies["genres_clean"])
    print(matrix)
    return matrix