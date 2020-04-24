'''This is a project to explore the growth of Jehovah's Witnesses'''

# import necessary libraries
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

#import data
df=pd.read_csv("/Users/opokujames/Desktop/JW-Stats/data.csv")

year=df["Year"]
bap=df["Total Number Baptized"]
ppubs=df["Peak of Publishers"]

bap=bap.values.reshape(-1,1)
ppubs=ppubs.values.reshape(-1,1)

#Peak Pubs, Average Pubs, Average Bible Studies
def one_plot():
	plt.plot(year, ppubs, label="Peak of Publishers")
	plt.plot(year, df["Average Publishers Preaching Each Month"], label="Average Publishers Preaching Each Month")
	plt.plot(year, df["Average Bible Studies Each Month"], label="Average Bible Studies Each Month")
	plt.grid(color="Gray", linestyle="-", linewidth=0.5)
	plt.legend()
	plt.show()

#Separate plots of Total Congregations, 
def sub_plots():
	fig, axes = plt.subplots(nrows=1, ncols=3)
	df.plot(x="Year", y="Total Congregations", title="Total Congregations", ax=axes[0], grid=True, legend=False, color='skyblue')
	df.plot(x="Year", y="Worldwide Memorial Attendance", title="Worldwide Memorial Attendance", ax=axes[1], grid=True, legend=False, color='darkseagreen')
	df.plot(x="Year", y="Total Hours Spent in Field", title="Total Hours Spent in Field", ax=axes[2], grid=True, legend=False, color='thistle')
	plt.show()

#Line chart of Memorial Partakers 
def mem_partakers():
	plt.plot(year, df["Memorial Partakers Worldwide"], label="Memorial Partakers Worldwide")
	plt.title("Memorial Partakers Worldwide")
	plt.xlabel("Year")
	plt.grid(color="Gray", linestyle="-", linewidth=0.5)
	plt.show()

#Line Chart of Total Number Baptized 
def bap_line():
	plt.plot(year, bap, color="Orange")
	plt.grid(color="Gray", linestyle="-", linewidth=0.5)
	plt.title("Total Number Baptized")
	plt.xlabel("Year")
	plt.show()

#Bar Chart of Total Number Baptized
def bap_bar():
	index = np.arange(len(year))
	plt.bar(index, bap, color="BlueViolet")
	plt.xlabel("Year")
	plt.ylabel("Number Baptized")
	plt.xticks(index, year, rotation="vertical")
	plt.title("Total Number Baptized Over Time")
	plt.show()

#Scatterplot of Peak Publishers vs. Total Number Baptized (Linear Regression)
def pvb_scatter():
	model=LinearRegression()
	model.fit(bap, ppubs)
	y_pred=model.predict(bap)

	plt.scatter(bap, ppubs, color="dimgray")
	plt.plot(bap, y_pred, color="turquoise")
	plt.grid(color="Gray", linestyle="-", linewidth=0.5)
	plt.title("Peak Publishers vs. Total Number Baptized")
	plt.xlabel("Total Number Baptized")
	plt.ylabel("Peak Publishers")
	plt.show()


pvb_scatter()


