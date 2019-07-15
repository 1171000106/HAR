import sys
import os
from math import *

# 用来预处理数据的
if (__name__ == "__main__"):
    p = 5000;
    lplp = [1,2,3,4,5,6,8,10,11];
    
    for i in lplp:
        cnt=0;
        lines = []
        tests = []
        f_name = str(i) + ".csv"
        with open(f_name, mode="r") as f:
            for l in f.readlines()[1:]:
                ql = l.split(",");
                g = True;
                for t in ql:
                    if(t.isdigit()):
                        g = False;
                if(g == True):
                    continue;
                if(cnt < p ):
                    cnt+=1;
                    tests.append(ql);
                else:
                    lines.append(ql);
                    
                    
        new_f_name = str(i)+"oo.csv";
        f = open(new_f_name, "w");
        for l in lines:
            for w in l:
                f.write(w);
                if(w!="\n" and w!="/r"):f.write(",");
            #f.write("\n");
        f.close();
        nf = str(i)+"test.csv";      
        f = open(nf,"w");
        for l in tests:
            for w in l:
                f.write(w);  
                if(w!="\n" and w!="/r"):f.write(",");
            #f.write("\n");
        f.close();
        