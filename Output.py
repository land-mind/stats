import rpy2.robjects as robjects
from rpy2.robjects.packages import importr
import pandas as pd
import time
import pprint
import ast
import csv
from collections import Counter

list_list_keyword = []
with open('data_diana_old.csv','r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        if float(row["3.7845345"]) <= 2.7:
            list_list_keyword.append(ast.literal_eval(row["[{'term': 'pacman', 'relevance': 0.983663}, {'term': 'hola.', 'relevance': 0.323839}]"]))

stopwords = set()
with open("stopwords.txt") as f:
	for line in f:
		stopwords.add(line.lower().rstrip())
list_terms = []
for list_keyword in list_list_keyword:
    for keyword in list_keyword:
        if keyword['term'].lower() not in stopwords:
            list_terms.append(keyword['term'])
            #print(keyword['term'], keyword['relevance'])

x = Counter(list_terms)
print(x)
