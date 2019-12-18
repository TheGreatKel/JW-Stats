'''This is a project to explore the growth of Jehovah's Witnesses'''

# import necessary libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
from scipy import stats

#List of corresponding years to keep me on track
year=[1991, 1992, 1993, 1994, 1995, 1996, 1997, 1998, 1999, 2000, 2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019]  

#List of Peak Publishers each year
ppubs=np.array([4278820, 4472787, 4709889, 4914094, 5199895, 5413769, 5599931, 5888650, 5912492, 6035564, 6117666, 6304645, 6429351, 6513132, 6613829, 6741444, 6957854, 7124443, 7313173, 7508050, 7659019, 7782346, 7965954, 8201545, 8220105, 8340847, 8457107, 8579909, 8683117]) 

#List of Total Baptized
bap=np.array([300945, 301002, 296004, 314818, 338491, 366579, 375923, 316092, 323439, 288907, 263431, 265469, 258845, 262416, 247631, 248327, 298304, 289678, 276233, 294368, 263131, 268777, 277344, 275581, 260273, 264535, 284212, 281744, 303866])

'''This was a check to test if the lists have equal lengths
print(len(year)==len(ppubs)==len(bap))'''


#Linear Regression

slope,intercept,r,p,std_err=stats.linregress(bap,ppubs)

rbap=bap.reshape(-1,1)
ppubs=ppubs.reshape(-1,1)
model=LinearRegression()
model.fit(rbap,ppubs)
y_pred=model.predict(rbap)


#Method to print Summary Statistics of Linear Regression
def PrintLinReg(): 
	print("Slope: "+ str(slope))
	print("Intercept :"+ str(intercept))
	print("R: "+ str(r))
	print("R-squared: "+ str(r**2))


#Visualizations


#Line chart of Peak Publishers
def PeakLine():
	plt.plot(year,ppubs,color="LightBlue")
	plt.grid(color="Gray",linestyle="-",linewidth=0.5)
	plt.title("Peak Publishers Vs. Time")
	plt.xlabel("Year")
	plt.ylabel("Peak Publishers")
	plt.show()

#Line Chart of Total Number Baptized 
def BapLine():
	plt.plot(year,bap,color="Orange")
	plt.grid(color="Gray",linestyle="-",linewidth=0.5)
	plt.title("Total Number Baptized Vs. Time")
	plt.xlabel("Year")
	plt.ylabel("Number Baptized")
	plt.show()

#Bar Chart of Total Number Baptized
def Bap_Bar():
	index = np.arange(len(year))
	plt.bar(index,bap,color="BlueViolet")
	plt.xlabel("Year")
	plt.ylabel("Number Baptized")
	plt.xticks(index,year,rotation="vertical")
	plt.title("Total Number Baptized Over Time")
	plt.show()

#Scatterplot of Peak Publishers vs. Total Number Baptized (LinReg)
def PVB_Scatter():
	plt.scatter(bap,ppubs,color="dimgray")
	plt.plot(bap,y_pred,color="turquoise")
	plt.grid(color="Gray",linestyle="-",linewidth=0.5)
	plt.title("Peak Publishers vs. Total Number Baptized")
	plt.xlabel("Total Number Baptized")
	plt.ylabel("Peak Publishers")
	plt.show()




#PeakLine()
#BapLine()
#Bap_Bar()
#PVB_Scatter()
