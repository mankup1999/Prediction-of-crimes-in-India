import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year=int(sys.argv[1])

data=pd.read_csv("DataSets/rape.csv")

data.fillna(0,axis=1,inplace=True)

data=data[data.Year==year]

states=np.unique(data.Area_Name)

n=states.size

rapes=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.Area_Name==states[i]])["Victims_of_Rape_Total"].sum()/2)
	rapes[i]=x

plt.title("Rape Data("+str(year)+")")
plt.barh(states,rapes)
plt.ylabel("States")
plt.xlabel("Rapes")
plt.show()
#plt.savefig("images/rapeGraph.jpg")

plt.close()

