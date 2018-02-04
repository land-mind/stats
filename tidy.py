import pandas
from collections import Counter
import numpy as np
import csv, ast

#calculate tf
bad_list = []
good_list = []
with open('data_diana.csv','r') as csvfile:
    reader = csv.reader(csvfile)
    count = 0
    for row in reader:
        # words = row[4]
        try:
            words = ast.literal_eval(row[4])
            if float(row[2]) <= 2.7:
                for word in words:
                    bad_list.append(word)
            else:
                for word in words:
                    good_list.append(word)
        except:
            count += 1
    print(count)

#group by score <-- this will put into dictionary
n1 = len(good_list)
n2 = len(bad_list)

good_count = Counter(good_list)
bad_count = Counter(bad_list)

print(type(bad_count))

good_freq = dict((item, num / (len(good_count)+len(bad_count))) for item, num in good_count.most_common())
bad_freq = dict((item, num / len(bad_count)) for item, num in bad_count.most_common())


#for each word. that is in both good and bad. ln(bad prop/ good prop ) * bad proportion
#seperate all words only found in the bad proportion
diff = {}
for key, good_value in good_freq.items():
    if key in bad_freq:
        diff[key] = np.log(bad_freq[key]/good_value)*bad_freq[key]

tfidf = sorted(list(diff.items()), key = lambda x: -x[1])

for tup in tfidf:
    print(tup[0])
