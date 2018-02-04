import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd
import time
import pprint
import ast
import csv
from collections import Counter

# list_list_keyword = []
# with open('data_diana_old.csv','r') as csvfile:
#     reader = csv.DictReader(csvfile)
#     for row in reader:
#         if float(row["3.7845345"]) <= 2.7:
#             list_list_keyword.append(ast.literal_eval(row["[{'term': 'pacman', 'relevance': 0.983663}, {'term': 'hola.', 'relevance': 0.323839}]"]))
#
# list_terms = []
# for list_keyword in list_list_keyword:
#     for keyword in list_keyword:
#         list_terms.append(keyword['term'])
#
# x = Counter(list_terms)
#print(list_terms)
qcc = importr("qcc")
r = robjects.r


#R part
robjects.r('''
MyData <- read.csv(file="data_diana.csv", header = FALSE, sep = ",")
myData <- MyData[1:2600,]
myDataMini <- MyData[1801:2200,]
#XBar Charts
a <- myData$V3
b <- myData$V1
V3 <- qcc.groups(myData$V3, myData$V1)
# V3mini <- qcc.groups(myDataMini$V3, myDataMini$V1)
# q1 <- qcc(V3mini, type="xbar")
# pl <- plot(q1, chart.all=FALSE)
# plsum <-summary(q1)
#
# #S chart
# q2 <- qcc(V3mini, type="S")
#
# #cusum
# q3 <- cusum(V3, decision.interval = 4, se.shift = 1 )

#ewma
q4 <- ewma(V3, lambda = 0.3, nsigmas=2)
#
# sizer <- function(x){
#     plot(x, height=2000, width = 10000, units="px")
# }
#
# sizer <- plot(q1, size = n)
#
# filt <- subset(myData, V3 <= 2.7) #based on numerical scale rank
# key <- filt$V5

# q = qcc(V3mini, type="xbar", nsigmas=3, plot=FALSE)
# beta = oc.curves(q)
# beta

PLOTME <- function(q4){
png(filename="EWMA.png")
plot(q4)
dev.off()
}
 ''')

#Look for the outliers for things because they mess up the rest of the model -- very important for cusum
# r_oc = robjects.r['beta']
# r_data = robjects.globalenv['q1']
# r_cusum = robjects.globalenv['q3']
# r_dev = robjects.globalenv['q2']
r_ewma = robjects.globalenv['q4']
r_f = robjects.r['PLOTME']

r_f(r_ewma)
#time.sleep(10)
#r.plot(r_data)
#time.sleep(10)

#r.plot(r_dev)
#time.sleep(10)


#r.plot(r_cusum)
#time.sleep(10)



# r.plot(r_oc)
# time.sleep(5)
#Operating Characterist curves.


#Looking for key words that trigger ptsd points and search for comminatlities in attacks...
#Also check related persons
#basically find out what caused the attack.
