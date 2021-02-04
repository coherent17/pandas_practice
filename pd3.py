import pandas as pd

se1=pd.Series({'a':1,'b':6,'c':11})
se2=pd.Series({'a':2,'b':7,'c':12})
se3=pd.Series({'a':3,'b':8,'c':13})
se4=pd.Series({'a':4,'b':9,'c':14})
se5=pd.Series({'a':5,'b':10,'c':15})
e=pd.concat([se1,se2,se3,se4,se5],axis=1)
e.columns=['A','B','C','D','E']
print(e)