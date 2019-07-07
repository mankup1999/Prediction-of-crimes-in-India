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

data=pd.read_csv("DataSets/suicides.csv")
data.fillna(0,axis=1,inplace=True)

states=np.unique(data.State)
i=0
valMap={}
stateVal=i

for s in states:
	valMap[s]=i
	if s.lower()==state.lower():
		stateVal=i
	i+=1

data.State=(data.State).map(valMap)

data=data.loc[:,["State","Year","Total"]]

states=np.unique(data.State)
years=np.unique(data.Year)

numbers=states.size*years.size
stateArray=[0 for _ in range(numbers)]
yearArray=[0 for _ in range(numbers)]
totalArray=[0 for _ in range(numbers)]
i=0

for x in states:
	for y in years:
		stateArray[i]=x
		yearArray[i]=y
		a=data[data.State==x]
		b=a[a.Year==y]
		c=b.Total
		d=c.sum()
		totalArray[i]=d
		i+=1


data=pd.DataFrame(columns=["State","Year","Total"])
data["State"]=stateArray
data["Year"]=yearArray
data["Total"]=totalArray

data=utils.shuffle(data)
preprocessing.scale(data,copy=True)

X=np.array(data.drop("Total",axis=1,inplace=False))
y=np.array(data.Total)
n=y.size

forest=RandomForestRegressor()


model=forest.fit(X,y)
predicted=model.predict([[stateVal,year]])

print("----------------------------------------------------")
print("\t\tSuicide Data")
print("\t     ------------------")
print("\tState Name :",state.title())
print("\tYear :",year)
print("\tExpected Data :",int(predicted[0]/10))
print("-----------------------------------------------------")





