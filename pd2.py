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
data={'A':{'a':1,'b':6,'c':11},
      'B':{'a':2,'b':7,'c':12},                         
      'C':{'a':3,'b':8,'c':13},  
      'D':{'a':4,'b':9,'c':14},                        
      'E':{'a':5,'b':10,'c':15}}
c=pd.DataFrame(data)
print(c)
#    A   B   C   D   E
#a   1   2   3   4   5
#b   6   7   8   9  10
#c  11  12  13  14  15

#3. using series to build the dataframe
se1=pd.Series({'a':1,'b':6,'c':11})
se2=pd.Series({'a':2,'b':7,'c':12})
se3=pd.Series({'a':3,'b':8,'c':13})
se4=pd.Series({'a':4,'b':9,'c':14})
se5=pd.Series({'a':5,'b':10,'c':15})
d=pd.DataFrame({'A':se1,'B':se2,'C':se3,'D':se4,'E':se5})
print(d)
#    A   B   C   D   E
#a   1   2   3   4   5
#b   6   7   8   9  10
#c  11  12  13  14  15

#4.using concat function
e=pd.concat([se1,se2,se3,se4,se5],axis=1)
e.columns=['A','B','C','D','E']
print(e)
#    A   B   C   D   E
#a   1   2   3   4   5
#b   6   7   8   9  10
#c  11  12  13  14  15

#5. get the value of the dataframe

print(e['A'])
#a     1
#b     6
#c    11
#Name: A, dtype: int64

print(e[['A','C']])
#    A   C
#a   1   3
#b   6   8
#c  11  13

print(e[e['A']>5])  #取得A這欄大於五的所有數據
#    A   B   C   D   E
#b   6   7   8   9  10
#c  11  12  13  14  15

print(e.values)
#[[ 1  2  3  4  5]
# [ 6  7  8  9 10]
# [11 12 13 14 15]]

print(e.values[0]) #a那列的數據
#[1 2 3 4 5]
