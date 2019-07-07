import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year=int(sys.argv[1])

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

plt.title("Robbery Data("+str(year)+")")
plt.barh(states,robbery)
plt.ylabel("States")
plt.xlabel("Robbery")
plt.show()
#plt.savefig("images/robberyGraph.jpg")

plt.close()

