import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import time
qcc = importr("qcc")
r = robjects.r
x = robjects.FloatVector([5,10,20,30])



#R part
robjects.r('''
  data(pistonrings)
  diameter <- with(pistonrings,qcc.groups(diameter, sample))
  head(diameter)


 q1 <- qcc(diameter[1:25,], type="xbar", newdata=diameter[26:40,])
 y <- plot(q1, chart.all=FALSE)
 ''')

r_y = robjects.globalenv['q1']
r.plot( r_y)
print(r.summary(r_y))
time.sleep(20)


#r_runExample = robjects.globalenv['y']
#print(r_runExample)
