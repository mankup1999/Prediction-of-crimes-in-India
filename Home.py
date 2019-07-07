import os,subprocess
from tkinter import *
from tkinter import messagebox

frameQuery=None
frameGraph=None
frameGraph1=None
frameGraph2=None
framePrediction=None


def getQueryAnalysis(t,year,state):
	global frameQuery
	if frameQuery:
		try:
			frameQuery.destroy()
		except:
			frameQuery=None
		del frameQuery
		frameQuery=None
	t.geometry("800x1000")
	year=year.get()
	state=state.get()
	murder=subprocess.Popen("python3 murderQuery.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	murder=murder.read().decode()
	rape=subprocess.Popen("python3 rapeQuery.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	rape=rape.read().decode()
	suicide=subprocess.Popen("python3 suicideQuery.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	suicide=suicide.read().decode()
	robbery=subprocess.Popen("python3 robberyQuery.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	robbery=robbery.read().decode()

	f=Frame(t)
	Label(f,text=murder,bg="yellow").grid(row=1,column=0)
	Label(f,text=rape,bg="yellow").grid(row=1,column=1)
	Label(f,text=suicide,bg="yellow").grid(row=2,column=0)
	Label(f,text=robbery,bg="yellow").grid(row=2,column=1)
	f.pack()

	frameQuery=f

def queryAnalysis(root):
	t=Tk()
	t.title("Prediction of crimes in India")
	t.geometry("800x500")
	year=StringVar(t)
	year.set("select-year")
	state=StringVar(t)
	state.set("select-state")
	f1=Frame(t)
	Label(f1,text="Prediction of crimes in India",font="Verdana 30 bold",fg="green",bg="yellow").grid(row=0,column=1)
	Label(f1,text="[Query Analysis]",font="Verdana 15 bold",fg="red").grid(row=1,column=1)
	Button(f1,text="Home",bg="violet",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=0)
	Button(f1,text="Exit",bg="orange",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=2)
	f1.pack()
	f2=Frame(t)
	Label(f2,text="Results",fg="purple",font="Verdana 20 bold").grid(row=0,column=1)
	Label(f2,text="Year",fg="orange",font="Verdana 10 bold").grid(row=1,column=0)
	Label(f2,text="State",fg="orange",font="Verdana 10 bold").grid(row=2,column=0)
	Button(f2,text="Go",bg="red",activebackground="green",command=lambda: getQueryAnalysis(t,year,state)).grid(row=3,column=1)
	o1=OptionMenu(f2,year,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011)
	o1.config(width=20)
	o1.grid(row=1,column=1)
	o2=OptionMenu(f2,state,"Andhra-Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal-Pradesh","Jammu-&-Kashmir","Jharkhand","Karnataka","Kerala","Madhya-Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil-Nadu","Telangana","Tripura","Uttar-Pradesh","Uttarakhand","West-Bengal")
	o2.config(width=20)
	o2.grid(row=2,column=1)
	f2.pack()
	t.mainloop()

def getGraphAnalysis(t,year):
	global frameGraph,frameGraph1,frameGraph2
	if frameGraph:
		try:
			frameGraph.destroy()
		except:
			frameGraph=None
		del frameGraph
		frameGraph=None
	if frameGraph1:
		try:
			frameGraph1.destroy()
		except:
			frameGraph1=None
		del frameGraph1
		frameGraph1=None
	if frameGraph2:
		try:
			frameGraph2.destroy()
		except:
			frameGraph2=None
		del frameGraph2
		frameGraph2=None
	
	#t.geometry("800x1000")
	year=year.get()

	f=Frame(t,height=40)
	f.pack()
	frameGraph2=f

	f=Frame(t)
	Label(f,text="Click Buttons to get Results for "+year,fg="blue",bg="orange").pack(side="bottom")
	f.pack()
	frameGraph1=f
	
	f=Frame(t)
	Button(f,text="Murder",width=20,height=3,command=lambda: os.system("python3 murderGraph.py "+year)).grid(row=0,column=0)
	Button(f,text="Rape",width=20,height=3,command=lambda: os.system("python3 rapeGraph.py "+year)).grid(row=0,column=1)
	Button(f,text="Suicide",width=20,height=3,command=lambda: os.system("python3 suicideGraph.py "+year)).grid(row=1,column=0)
	Button(f,text="Robbery",width=20,height=3,command=lambda: os.system("python3 robberyGraph.py "+year)).grid(row=1,column=1)
	f.pack()

	frameGraph=f
	

def graphAnalysis(root):
	t=Tk()
	t.title("Prediction of crimes in India")
	t.geometry("800x500")
	year=StringVar(t)
	year.set("select-year")
	f1=Frame(t)
	Label(f1,text="Prediction of crimes in India",font="Verdana 30 bold",fg="green",bg="yellow").grid(row=0,column=1)
	Label(f1,text="[Graphical Analysis]",font="Verdana 15 bold",fg="red").grid(row=1,column=1)
	Button(f1,text="Home",bg="violet",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=0)
	Button(f1,text="Exit",bg="orange",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=2)
	f1.pack()
	f2=Frame(t)
	Label(f2,text="Results",fg="purple",font="Verdana 20 bold").grid(row=0,column=1)
	Label(f2,text="Year",fg="orange",font="Verdana 10 bold").grid(row=1,column=0)
	Button(f2,text="Go",bg="red",activebackground="green",command=lambda: getGraphAnalysis(t,year)).grid(row=3,column=1)
	o1=OptionMenu(f2,year,2001,2002,2003,2004,2005,2006,2007,2008,2009,2010,2011)
	o1.config(width=20)
	o1.grid(row=1,column=1)
	f2.pack()
	t.mainloop()

def getPrediction(t,year,state):
	global framePrediction
	if framePrediction:
		try:
			framePrediction.destroy()
		except:
			framePrediction=None
		del framePrediction
		framePrediction=None
	t.geometry("800x1000")
	year=year.get()
	state=state.get()
	murder=subprocess.Popen("python3 predictionMurder.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	murder=murder.read().decode()
	rape=subprocess.Popen("python3 predictionRape.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	rape=rape.read().decode()
	suicide=subprocess.Popen("python3 predictionSuicide.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	suicide=suicide.read().decode()
	robbery=subprocess.Popen("python3 predictionRobbery.py "+year+" "+state, shell=True, stdout=subprocess.PIPE).stdout
	robbery=robbery.read().decode()

	f=Frame(t)
	Label(f,text=murder,bg="yellow").grid(row=1,column=0)
	Label(f,text=rape,bg="yellow").grid(row=1,column=1)
	Label(f,text=suicide,bg="yellow").grid(row=2,column=0)
	Label(f,text=robbery,bg="yellow").grid(row=2,column=1)
	f.pack()

	framePrediction=f
	

def prediction(root):
	t=Tk()
	t.title("Prediction of crimes in India")
	t.geometry("800x500")
	year=StringVar(t)
	year.set("select-year")
	state=StringVar(t)
	state.set("select-state")
	f1=Frame(t)
	Label(f1,text="Prediction of crimes in India",font="Verdana 30 bold",fg="green",bg="yellow").grid(row=0,column=1)
	Label(f1,text="[Predictions]",font="Verdana 15 bold",fg="red").grid(row=1,column=1)
	Button(f1,text="Home",bg="violet",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=0)
	Button(f1,text="Exit",bg="orange",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=2)
	f1.pack()
	f2=Frame(t)
	Label(f2,text="Results",fg="purple",font="Verdana 20 bold").grid(row=0,column=1)
	Label(f2,text="Year",fg="orange",font="Verdana 10 bold").grid(row=1,column=0)
	Label(f2,text="State",fg="orange",font="Verdana 10 bold").grid(row=2,column=0)
	Button(f2,text="Go",bg="red",activebackground="green",command=lambda: getPrediction(t,year,state)).grid(row=3,column=1)
	o1=OptionMenu(f2,year,2016,2017,2018,2019,2020)
	o1.config(width=20)
	o1.grid(row=1,column=1)
	o2=OptionMenu(f2,state,"Andhra-Pradesh","Arunachal Pradesh","Assam","Bihar","Chhattisgarh","Goa","Gujarat","Haryana","Himachal-Pradesh","Jammu-&-Kashmir","Jharkhand","Karnataka","Kerala","Madhya-Pradesh","Maharashtra","Manipur","Meghalaya","Mizoram","Nagaland","Odisha","Punjab","Rajasthan","Sikkim","Tamil-Nadu","Telangana","Tripura","Uttar-Pradesh","Uttarakhand","West-Bengal")
	o2.config(width=20)
	o2.grid(row=2,column=1)
	f2.pack()
	t.mainloop()
def report(root):
	report=subprocess.Popen("python3 reportQuery.py", shell=True, stdout=subprocess.PIPE).stdout
	report=report.read().decode()
	t=Tk()
	t.title("Prediction of crimes in India")
	t.geometry("800x600")
	f1=Frame(t)
	Label(f1,text="Prediction of crimes in India",font="Verdana 30 bold",fg="green",bg="yellow").grid(row=0,column=1)
	Label(f1,text="[Reports]",font="Verdana 15 bold",fg="red").grid(row=1,column=1)
	Button(f1,text="Home",bg="violet",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=0)
	Button(f1,text="Exit",bg="orange",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: t.destroy()).grid(row=1,column=2)
	f1.pack()
	f=Frame(t)
	Label(f,text="Report/Conclusion",font="Verdana 20 bold",fg="green",bg="lightblue").grid(row=0,column=1)
	Label(f,text=report,bg="yellow").grid(row=2,column=1)
	Button(f,text="Get Graph",fg="orange",bg="blue",activebackground="red",command=lambda: os.system("python3 reportGraph.py")).grid(row=3,column=1)
	f.pack()
	t.mainloop()
	

root=Tk()
root.title("Prediction of crimes in India")
root.geometry("800x500")

f1=Frame(root)
Label(f1,text="Prediction of crimes in India",font="Verdana 30 bold",fg="green",bg="yellow").pack(pady=30)
f1.pack()

f2=Frame(root)
Button(f2,text="Query Analysis",width=20,height=5,fg="blue",bg="lightyellow",activebackground="red",activeforeground="lightgreen",relief="ridge",command=lambda:queryAnalysis(root)).grid(row=0,column=0)
Button(f2,text="Graph Analysis",width=20,height=5,fg="blue",bg="lightyellow",activebackground="red",activeforeground="lightgreen",relief="ridge",command=lambda:graphAnalysis(root)).grid(row=0,column=1)
Button(f2,text="Prediction/Trends",width=20,height=5,fg="blue",bg="lightyellow",activebackground="red",activeforeground="lightgreen",relief="ridge",command=lambda:prediction(root)).grid(row=1,column=0)
Button(f2,text="Report/Conclusion",width=20,height=5,fg="blue",bg="lightyellow",activebackground="red",activeforeground="lightgreen",relief="ridge",command=lambda:report(root)).grid(row=1,column=1)
f2.pack(padx=50,pady=50)

f3=Frame(root)
Button(f3,text="Exit",bg="orange",fg="green",activebackground="red",activeforeground="lightgreen",command=lambda: root.destroy()).pack()
f3.pack(padx=0,pady=0)


root.mainloop()

