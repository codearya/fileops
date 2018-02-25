'''
import os
import datetime

files = os.listdir("merg_files")
#print(files)
fname = datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt"
for i in files:
    #print(i)
    f=open("merg_files/"+i,'r')
    for j in f:
        print(j)
        nf=open(fname,"a+")
        nf.write(j)
'''

import glob2
import datetime

filenames=glob2.glob("*.txt")

with open(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")+".txt",'w') as file:
    for filename in filenames:
        with open(filename,"r") as f:
            file.write(f.read()+"\n")
