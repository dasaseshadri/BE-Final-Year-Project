import os
import numpy as np
import pandas as pd

list_dir = os.listdir('/home/prateek/GR_CODE/Cleaned_data')

print(list_dir)

#d=os.chdir(list_dir[0])
featurefile = open('updated_features','a+')

for l in list_dir:
    if(l=='features.py' or l =='updated_features'):
        continue
    d=os.chdir(l)
    #print(l)
    #print('\nChanging directory to'+str(d))
    list_files = os.listdir(d)
    print(l)
    for f in list_files:
        #print("\nFor File"+f)
        dataset = np.loadtxt(f)
        x = dataset[1:,1]
        y = dataset[1:,2]
        z = dataset[1:,3]
        #print(x,y,z)
        print("\n",x.mean(),y.mean(),z.mean(),"\n",x.var(),y.var(),z.var(),"\n",x.std(),y.std(),z.std(),"\n")
        #s = l+","+str(x.mean())+","+str(y.mean())+","+str(z.mean())+","+str(x.var())+","+str(y.var())+","+str(z.var())+","+str(x.std())+","+str(y.std())+","+str(z.std())+"\n"
        #featurefile.write(s)
    os.chdir('..')

featurefile.close()
