import pandas as pd

#1. build the dataframe
a=pd.DataFrame([[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]])
print(a)
#    0   1   2   3   4
#0   1   2   3   4   5
#1   6   7   8   9  10
#2  11  12  13  14  15
#直的是index,橫的是column

#setting index and column
b=pd.DataFrame(a.values,index=['a','b','c'],columns=['A','B','C','D','E'])
print(b)
#    A   B   C   D   E
#a   1   2   3   4   5
#b   6   7   8   9  10
#c  11  12  13  14  15

#2. using dict to build the dataframe
