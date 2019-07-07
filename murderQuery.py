import sys
import numpy as np
import pandas as pd

year=int(sys.argv[1])
state=(sys.argv[2]).replace("-"," ")


data=pd.read_csv("DataSets/murder.csv")

data.fillna(0,axis=1,inplace=True)

data=data[data.Year==year]

states=np.unique(data.Area_Name)

n=states.size

murders=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.Area_Name==states[i]])["Victims_Total"].sum()/2)
	murders[i]=x

index=0

for i in range(n):
	if (states[i]).lower()==state.lower():
		index=i
		break

rank=0

for i in range(n):
	if murders[index]<=murders[i]:
		rank+=1

percent=str(round(murders[index]/sum(murders)*100,2))+"%"

print("----------------------------------------------------")
print("\t\tMurder Data")
print("\t     ------------------")
print("\tState Name :",state.title())
print("\tYear :",year)
print("\tData :",murders[index])
print("\tRank :",rank)
print("\tPercent :",percent)
print("-----------------------------------------------------")

		



