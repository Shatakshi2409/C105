import csv
import pandas as pd
import plotly.express as px
import math

with open('class1.csv',newline='')as f:
    reader=csv.reader(f)
    filedata=list(reader)

filedata.pop(0)
totalmarks=0
totalentries=len(filedata)
for marks in filedata:
    totalmarks+=float(marks[1])
mean=totalmarks/totalentries
print(mean)

df=pd.read_csv('class1.csv')
fig=px.scatter(df,x='Student Number',y='Marks')
fig.update_layout(shapes=[dict(
    type='line',y0=mean,y1=mean,
    x0=0,x1=totalentries
)])
fig.show()
data=filedata[1]
squaredlist=[]
for number in data:
    a=int(number)-mean
    a=a**2
    squaredlist.append(a)
sum=0
for i in squaredlist:
    sum=sum+i
result=sum/(len(data)-1)
stdev=math.sqrt(result)
print(stdev)