import numpy as np


# 将文件中的数据分成不同的窗口
def window(filename, type, width=100, step=50):
    # 特征值
    argvs = []
    with open(filename, mode="r") as f:
        # 读入一行数据并将其分割后转化为一个float的list
        lines = [list(map(lambda x: float(x), l.split(",")[4:20]))
                 for l in f.readlines()]
    for wl in [lines[i:i + width] for i in range(0, len(lines) - 1, step)]:
        argv = []
        argv.append(list(np.average(np.array(wl), axis=0)))
        argv.append(list(np.var(np.array(wl), axis=0)))
        argv.append(np.median(np.array(type)))
        # print(argv)
        argvs.append(argv)
    return argvs


if __name__ == "__main__":
    argvs = window("../data/teacher/1oo.csv", 1)
