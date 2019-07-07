import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.title("Report/Conclusion")

murder=pd.read_csv("DataSets/murder.csv")
murder.fillna(0,axis=1,inplace=True)

years=np.unique(murder.Year)
n=years.size
murders=[0 for _ in range(n)]
for i in range(n):
	x=int(((murder[murder.Year==years[i]]).Victims_Total).sum()/2)
	murders[i]=x

plt.bar(years+0.00,murders,label="Murders Statistics",color="b",width=0.25)
plt.legend()



rape=pd.read_csv("DataSets/rape.csv")
rape.fillna(0,axis=1,inplace=True)

years=np.unique(rape.Year)
n=years.size
rapes=[0 for _ in range(n)]
for i in range(n):
	x=int(((rape[rape.Year==years[i]]).Victims_of_Rape_Total).sum()/2)
	rapes[i]=x

plt.bar(years+0.25,rapes,label="Rape Statistics",color="g",width=0.25)
plt.legend()


suicide=pd.read_csv("DataSets/suicides.csv")
suicide.fillna(0,axis=1,inplace=True)

years=np.unique(suicide.Year)
n=years.size
suicides=[0 for _ in range(n)]
for i in range(n):
	x=int(((suicide[suicide.Year==years[i]]).Total).sum()/2)
	suicides[i]=int(x/10)

plt.bar(years+0.50,suicides,label="Suicide Statistics(/10)",color="r",width=0.25)
plt.legend()


robbery=pd.read_csv("DataSets/robbery.csv")
robbery.fillna(0,axis=1,inplace=True)
robbery["Total"]=robbery.Loss_of_Property_1_10_Crores+robbery.Loss_of_Property_10_25_Crores+robbery.Loss_of_Property_25_50_Crores+robbery.Loss_of_Property_50_100_Crores+robbery.Loss_of_Property_Above_100_Crores

years=np.unique(robbery.Year)
n=years.size
robberies=[0 for _ in range(n)]
for i in range(n):
	x=int(((robbery[robbery.Year==years[i]]).Total).sum()/2)
	robberies[i]=x


plt.bar(years+0.75,robberies,label="Robbery Statistics",color="y",width=0.25)
plt.legend()


plt.show()




