import keras
from helper import read_data

X, y = read_data('data/data.csv')

print(X[0].size)
