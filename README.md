
# Movie Recommendation System

A content-based movie recommendation system built with Python and machine learning techniques.

The system recommends movies based on their **genre similarity** using **TF-IDF Vectorization** and **Cosine Similarity**.

## How It Works

The recommendation pipeline follows these steps:

1. Load the movie dataset.
2. Clean and preprocess movie genres.
3. Convert genre text into numerical vectors using **TF-IDF**.
4. Calculate similarity between movies using **Cosine Similarity**.
5. Rank movies by similarity score.
6. Return the **Top-N most similar movies**.

```text
Movie Genres
     ↓
Preprocessing
     ↓
TF-IDF Vectorization
     ↓
TF-IDF Matrix
     ↓
Cosine Similarity
     ↓
Similarity Scores
     ↓
Top-N Recommendations
```

## Algorithms

### TF-IDF

TF-IDF (Term Frequency–Inverse Document Frequency) converts textual movie genres into numerical feature vectors.

For example:

```text
Thriller|Mystery|Drama
```

is preprocessed into:

```text
thriller mystery drama
```

and then represented numerically using `TfidfVectorizer`.

### Cosine Similarity

Cosine Similarity measures how similar two movie vectors are.

$$
\text{similarity}(A,B) =
\frac{A \cdot B}
{\|A\|\|B\|}
$$

A higher score means the movies have more similar content.

### Top-N Recommendation

After calculating similarity scores, the movies are sorted from highest to lowest similarity. The selected movie itself is excluded and the Top-N results are returned.

## Project Structure

```text
lab_01/
│
├── data/
│   ├── Movie.csv
│   ├── rating.csv
│   ├── tags.csv
│   └── link.csv
│
├── notebooks/
│   └── 01_data.ipynb
│
├── src/
│   ├── __init__.py
│   ├── data_loader.py
│   ├── preprocessing.py
│   ├── recom.py
│   └── recommender.py
│
├── tests/
│   └── test_recommender.py
│
├── app.py
├── requirements.txt
├── .gitignore
└── README.md
```


## Running the Project

Run:

```bash
python app.py
```

The application will select a movie and return the most similar movies with their similarity scores.

Example:

```text
Selected movie:
Mouse (2021)

Recommendations:

movieId    title                         genres                    score
4707       Liebestraum (1991)            Mystery|Thriller          0.4176
257        Just Cause (1995)             Mystery|Thriller          0.4176
119672     7th Floor (2013)              Mystery|Thriller          0.4176
```

## Technologies

* Python
* Pandas
* NumPy
* Scikit-learn
* TF-IDF Vectorization
* Cosine Similarity
* Jupyter Notebook


## 👤 Author

**Aysel Musayeva**
