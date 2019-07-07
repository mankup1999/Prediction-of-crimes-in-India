import numpy as np
import pandas as pd

murder=pd.read_csv("DataSets/murder.csv")
murder.fillna(0,axis=1,inplace=True)

years=np.unique(murder.Year)
n=years.size
murders=[0 for _ in range(n)]
for i in range(n):
	x=int(((murder[murder.Year==years[i]]).Victims_Total).sum()/2)
	murders[i]=x

print("----------------------------------------------------")
print("Murder Data")
print("------------------")
print("Year :","  ".join(map(str,years)))
print("Data :","  ".join(map(str,murders)))
print("-----------------------------------------------------")



rape=pd.read_csv("DataSets/rape.csv")
rape.fillna(0,axis=1,inplace=True)

years=np.unique(rape.Year)
n=years.size
rapes=[0 for _ in range(n)]
for i in range(n):
	x=int(((rape[rape.Year==years[i]]).Victims_of_Rape_Total).sum()/2)
	rapes[i]=x

print("----------------------------------------------------")
print("Rape Data")
print("------------------")
print("Year :","  ".join(map(str,years)))
print("Data :","  ".join(map(str,rapes)))
print("-----------------------------------------------------")




suicide=pd.read_csv("DataSets/suicides.csv")
suicide.fillna(0,axis=1,inplace=True)

years=np.unique(suicide.Year)
n=years.size
suicides=[0 for _ in range(n)]
for i in range(n):
	x=int(((suicide[suicide.Year==years[i]]).Total).sum()/2)
	suicides[i]=int(x/10)

print("----------------------------------------------------")
print("Suicide Data")
print("------------------")
print("Year :","  ".join(map(str,years)))
print("Data :","  ".join(map(str,suicides)))
print("-----------------------------------------------------")



robbery=pd.read_csv("DataSets/robbery.csv")
robbery.fillna(0,axis=1,inplace=True)
robbery["Total"]=robbery.Loss_of_Property_1_10_Crores+robbery.Loss_of_Property_10_25_Crores+robbery.Loss_of_Property_25_50_Crores+robbery.Loss_of_Property_50_100_Crores+robbery.Loss_of_Property_Above_100_Crores

years=np.unique(robbery.Year)
n=years.size
robberies=[0 for _ in range(n)]
for i in range(n):
	x=int(((robbery[robbery.Year==years[i]]).Total).sum()/2)
	robberies[i]=x

print("----------------------------------------------------")
print("Robbery Data")
print("------------------")
print("Year :","  ".join(map(str,years)))
print("Data :","  ".join(map(str,robberies)))
print("-----------------------------------------------------")








