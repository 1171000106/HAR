import sys
import os

# 用来将所有test组合成一个的

if (__name__ == "__main__"):
    lplp = [1,2,3,4,5,6,8,10,11];
    lines = [];
    
    for i in lplp:
        f_name = str(i) + "test.csv"
        with open(f_name, mode="r") as f:
            for l in f.readlines()[1:]:
                lines.append(l);
    f = open("testall.csv","w");
    for o in lines:
        f.write(o);
    f.close();

                   
