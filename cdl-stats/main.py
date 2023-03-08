import pandas as pd
from predict import *


if __name__ == "__main__":
    schedule = pd.read_csv("data/major4-bracket.csv", delimiter=";")
    standings = pd.read_csv("data/online-standings.csv", delimiter=";")
