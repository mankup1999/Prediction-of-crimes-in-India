import sys
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

year=int(sys.argv[1])

data=pd.read_csv("DataSets/suicides.csv")

data.fillna(0,axis=1,inplace=True)

data=data[data.Year==year]

states=np.unique(data.State)

n=states.size

suicides=[0 for _ in range(n)]

for i in range(n):
	x=int((data[data.State==states[i]])["Total"].sum()/2)
	suicides[i]=x

plt.title("Suicide Data("+str(year)+")")
plt.barh(states,suicides)
plt.ylabel("States")
plt.xlabel("suicides")
plt.show()
#plt.savefig("images/suicideGraph.jpg")

plt.close()

