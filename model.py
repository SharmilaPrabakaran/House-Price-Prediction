import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import pickle
import requests
import json

dataset = pd.read_csv('kc_house_data.csv')
X = dataset['sqft_living'].values
A = X.reshape(-1,1)
y = dataset['price'].values

#print A

X_train, X_test, y_train, y_test = train_test_split(A, y, test_size = 0.33, random_state = 0)

regressor = LinearRegression()
regressor.fit(X_train, y_train)
y_pred = regressor.predict(X_test)

pickle.dump(regressor, open('model.pkl','wb'))

model = pickle.load(open('model.pkl','rb'))
print(model.predict([[989]]))
