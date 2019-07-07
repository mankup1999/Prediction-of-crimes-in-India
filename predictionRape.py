import sys
import math
import numpy as np
import pandas as pd
from sklearn import utils,preprocessing
from sklearn import metrics
from sklearn.model_selection import cross_val_predict
from sklearn.ensemble import RandomForestRegressor

year=int(sys.argv[1])
state=(sys.argv[2]).replace("-"," ")

data=pd.read_csv("DataSets/rape.csv")
data.fillna(0,axis=1,inplace=True)

data=data[data.Subgroup=="Total Rape Victims"]

data=data.loc[:,["Area_Name","Year","Rape_Cases_Reported"]]

states=np.unique(data.Area_Name)

i=0
valMap={}
stateVal=i

for s in states:
	valMap[s]=i
	if s.lower()==state.lower():
		stateVal=i
	i+=1

data.Area_Name=(data.Area_Name).map(valMap)

data=utils.shuffle(data)
preprocessing.scale(data,copy=True)

X=np.array(data.drop("Rape_Cases_Reported",axis=1,inplace=False))
y=np.array(data.Rape_Cases_Reported)
n=y.size

forest=RandomForestRegressor()

model=forest.fit(X,y)
predicted=model.predict([[stateVal,year]])

print("----------------------------------------------------")
print("\t\tRape Data")
print("\t     ------------------")
print("\tState Name :",state.title())
print("\tYear :",year)
print("\tExpected Data :",int(predicted[0]))
print("-----------------------------------------------------")





