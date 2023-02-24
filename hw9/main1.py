import pandas as pd
import numpy as np

#Определить среднюю стоимость дома, где кол-во людей от 0 до 500 (population)
df = pd.read_csv('sample_data/california_housing_train.csv')
dataset_1 = df[['population', 'median_income']]
qr = dataset_1.query('0 < population < 500 ')
res = qr[['median_income']].mean().item()
print(res) #3.87454440974391

#Узнать какая максимальная households в зоне минимального значения population
dataset_2 = df[['population' ,'households']]
min_p = dataset_2[['population']].min().item()
qr2 = dataset_2[dataset_2['population'] == min_p]
res2 = qr2[['households']].max().item()
print(res2) #4.0

