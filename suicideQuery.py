import sys
import numpy as np
import pandas as pd

year=int(sys.argv[1])
state=(sys.argv[2]).replace("-"," ")

data=pd.read_csv("DataSets/suicides.csv")

data.fillna(0,axis=1,inplace=True)

data=data[data.Year==year]

states=np.unique(data.State)

n=states.size

suicides=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.State==states[i]])["Total"].sum()/2)
	suicides[i]=x

index=0

for i in range(n):
	if (states[i]).lower()==state.lower():
		index=i
		break

rank=0

for i in range(n):
	if suicides[index]<=suicides[i]:
		rank+=1

percent=str(round(suicides[index]/sum(suicides)*100,2))+"%"

print("----------------------------------------------------")
print("\t\tSuicide Data")
print("\t     ------------------")
print("\tState Name :",state.title())
print("\tYear :",year)
print("\tData :",suicides[index])
print("\tRank :",rank)
print("\tPercent :",percent)
print("-----------------------------------------------------")

		



