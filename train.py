import numpy as np
import csv
import pandas as pd
import jieba
import jieba.analyse
import matplotlib as mpl
from gensim import corpora,models,similarities
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt

all_real = []
all_fake = []
all_real_list = []
all_fake_list = []
data1 = pd.read_csv('train.csv', usecols = ['title1_zh'])
data2 = pd.read_csv('train.csv', usecols = ['title2_zh'])

num = int(data1.describe().iloc[0,0])
for i in range(0, 1):
    real_data = data1.iloc[i,0]
    fake_data = data2.iloc[i,0]
    all_real.append(real_data)
    all_fake.append(fake_data)

for real in all_real:
    real_list = [word for word in jieba.cut(real)]
    all_real_list.append(real_list)

for fake in all_fake:
    fake_list = [word for word in jieba.cut(fake)]
    all_fake_list.append(fake_list)


print(all_real_list)
print(all_fake_list)

    
with open("real.txt", 'w') as output:
    for row in real:
        output.write(str(row))


