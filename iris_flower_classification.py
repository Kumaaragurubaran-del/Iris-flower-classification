# -*- coding: utf-8 -*-
"""iris_flower_classification.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/14oc5-9YMHOFnMZKlqHcOL36bqYVSjOvn
"""

!pip install opendatasets

import opendatasets as od

od.download('https://www.kaggle.com/datasets/uciml/iris')

import pandas as pd

from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('/content/iris/Iris.csv')
data

data.info()

Trans = LabelEncoder()
data.Species = Trans.fit_transform(data.Species) # Converting string to numerical data type

z = data.drop(columns ='Id', inplace = False) # Dropping the unwanted columns ie..features which is not used for our model

cnt = z['Species'].value_counts()
cnt

x = z.drop(columns ='Species',inplace = False) # Independent variable
y = z['Species'] #Target variable

x_train , x_test, y_train, y_test = train_test_split(x,y, test_size =0.3,random_state=40)

scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

model = KNeighborsClassifier(n_neighbors = 3)
model.fit(x_train,y_train)

pred = model.predict(x_test)

acc = accuracy_score(pred,y_test)
print("Accuracy of the model is ", acc*100,"%")