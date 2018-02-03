import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import time

qcc = importr("qcc")
r = robjects.r


#R part
robjects.r('''
MyData <- read.csv(file="data_sample.csv", header = FALSE, sep = ",")
myData <- MyData[1:30,]

a <- myData$V3
b <- myData$V1
V3 <- qcc.groups(myData$V3, myData$V1)
q1 <- qcc(V3, type="xbar")


 ''')

r_data = robjects.globalenv['q1']
r.plot(r_data)

time.sleep(20)
