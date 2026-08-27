from pathlib import Path
import pandas as pd

# represents the path to the data folder
DATA_DIR=Path("../data")

def load_movies():
    return pd.read_csv(DATA_DIR / "Movie.csv",sep="\t",encoding="latin1") 
