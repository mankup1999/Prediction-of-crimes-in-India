import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year=int(sys.argv[1])

data=pd.read_csv("DataSets/murder.csv")

data.fillna(0,axis=1,inplace=True)

data=data[data.Year==year]

states=np.unique(data.Area_Name)

n=states.size

murders=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.Area_Name==states[i]])["Victims_Total"].sum()/2)
	murders[i]=x

plt.title("Murder Data("+str(year)+")")
plt.barh(states,murders)
plt.ylabel("States")
plt.xlabel("Murders")

plt.show()
#plt.savefig("images/murderGraph.jpg")

plt.close()

