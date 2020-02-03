import numpy as np
import pandas as pd

f1 = open("g1","r")
f2 = open("tmp","w+")

for row in f1:
    list_of_columns = row.split("\t")
    if len(list_of_columns)!=4:
        print(row)
    else:
        f2.write(row)
