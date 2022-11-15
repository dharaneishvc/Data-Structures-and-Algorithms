## Program to take rows and columns within values less than 500

ele = []
filelink = open("D:\Btech\SEM5\Design and Analysis of Algorithms\Project\Data-Structures-and-Algorithms\Graph based Email suggestion\Email-EuAll.txt","r")
#V = len(filelink.readlines())
V = 420045
file_line = filelink.readline()
# use the readline() method to read further.
# If the file is not empty keep reading one line at a time, till the file is empty
while file_line:
    #str.split() method is used split the string into a list of strings.
    numlist = [int(ele) for ele in file_line.split('\t')]
    ele.append([numlist[0],numlist[1]])
    #print(numlist)
    #use realine() to read next line
    file_line = filelink.readline()
filelink.close()

import numpy as np
import pandas as pd
df = pd.DataFrame(ele)
print(df.head(10))
df.columns = ['src', 'dst']
print(df.dtypes)

df2 = df[(df['src'] < 500)]
df3 = df2[(df2['dst'] < 500)]
print(len(df2), len(df3))
df3.to_csv("D:\Btech\SEM5\Design and Analysis of Algorithms\Project\Data-Structures-and-Algorithms\Graph based Email suggestion\email500.csv")