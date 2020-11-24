import pandas as pd
import numpy as np

fsize = 100
col=['SKU','Branch_CODE','Start_date','end_date','Dept','supp_code','lasttimestamp','Process flags','Indic','Date']
df=pd.DataFrame(columns=col)
df['SKU']= np.random.randint(0,1000,size=fsize)
df['Branch_CODE']= np.random.randint(10,99,size=fsize)
df['Dept']=np.random.randint(10,99,size=fsize)
df['supp_code']=np.random.randint(10000,99999,size=fsize)
df['Process flags']='Y'
df['Indic']='Z'
df['a']=np.random.randint(10,30,size=fsize)
df['b']=np.random.randint(10,12,size=fsize)
df['c']=np.random.randint(2000,2020,size=fsize)
df['Start_date'] = df[df.columns[10:]].apply(
    lambda x: '.'.join(x.dropna().astype(str)),
    axis=1
)
df['end_date'] = df[df.columns[10:]].apply(
    lambda x: '.'.join(x.dropna().astype(str)),
    axis=1
)
df['Date'] = df[df.columns[10:]].apply(
    lambda x: '.'.join(x.dropna().astype(str)),
    axis=1
)
df['lasttimestamp']= '2020-12-09-11.28.06.145020'
del df['a']
del df['b']
del df['c']
df.to_csv('C:\\Users\\Nitish.Reddy\\Downloads\\LINKS_sample.csv', encoding='utf-8',index=False)
