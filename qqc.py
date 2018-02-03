import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import time

qcc = importr("qcc")
r = robjects.r


#R part
robjects.r('''
MyData <- read.csv(file="data_diana.csv", header = FALSE, sep = ",")
myData <- MyData[1:2180,]

#XBar Charts
a <- myData$V3
b <- myData$V1
V3 <- qcc.groups(myData$V3, myData$V1)
q1 <- qcc(V3, type="xbar")
pl <- plot(q1, chart.all=FALSE)
plsum <- summary(q1)

#S chart
q2 <- qcc(V3, type="S")


 ''')

r_data = robjects.globalenv['q1']
r.plot(r_data)
time.sleep(5)

r_dev = robjects.globalenv['q2']
r.plot(r_dev)
time.sleep(10)
