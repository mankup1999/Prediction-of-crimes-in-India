import sys
import numpy as np
import pandas as pd

year=int(sys.argv[1])
state=(sys.argv[2]).replace("-"," ")

data=pd.read_csv("DataSets/robbery.csv")

data.fillna(0,axis=1,inplace=True)

data["Total"]=data.Loss_of_Property_1_10_Crores+data.Loss_of_Property_10_25_Crores+data.Loss_of_Property_25_50_Crores+data.Loss_of_Property_50_100_Crores+data.Loss_of_Property_Above_100_Crores

data=data[data.Year==year]

states=np.unique(data.Area_Name)

n=states.size

robbery=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.Area_Name==states[i]])["Total"].sum())
	robbery[i]=x

index=0

for i in range(n):
	if (states[i]).lower()==state.lower():
		index=i
		break

rank=0

for i in range(n):
	if robbery[index]<=robbery[i]:
		rank+=1

percent=str(round(robbery[index]/sum(robbery)*100,2))+"%"

print("----------------------------------------------------")
print("\t\tRobbery Data")
print("\t     ------------------")
print("\tState Name :",state.title())
print("\tYear :",year)
print("\tData :",robbery[index])
print("\tRank :",rank)
print("\tPercent :",percent)
print("-----------------------------------------------------")

		



