import pandas as pd
cars = pd.read_csv('cars.csv')
a = cars.iloc[[0,1,2,3,4],[0,2,4,6,8,10]]
b = cars.iloc[[0]]
c = cars.iloc[[23],[0,2]]
d = cars.iloc[[1,28,18],[0,2,10]]