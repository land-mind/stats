import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import time
timeSeries = importr("timeSeries")
forecast = importr("forecast")
r = robjects.r

robjects.r('''

MyData <- read.csv(file="data_diana.csv", header = FALSE, sep = ",")
myData <- MyData[100:200,2:3]
t <- as.timeSeries(myData)
plotts <- plot.ts(t, nc = 50)

''')

r_data = robjects.globalenv['t']

#r_sum = robjects.globalenv['t1']
plotts = robjects.r['plotts']

#print(r_sum)
#r.plot(r_data)
plotts
time.sleep(10)
