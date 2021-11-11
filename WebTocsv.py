import pandas as pd

urls = ["https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdcr-state-totals.csv",
"https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-age.csv",
"https://raw.githubusercontent.com/datadesk/california-coronavirus-data/master/cdph-hospital-patient-county-totals.csv"
]

x = range(0, 3)

for n in x:   
    if(n==0):
        c = pd.read_csv(urls[n],index_col=None)       
    if(n==1):
        d = pd.read_csv(urls[n],index_col=None)        
    if(n==2):
        e = pd.read_csv(urls[n],index_col=None)        
       
c.to_csv('Covid19_C.txt', index=False)
d.to_csv('Covid19_D.txt',index=False)
e.to_csv('Covid19_E.txt', index=False)
