import numpy as np


# 将文件中的数据分成不同的窗口
# width是窗口宽度
# 1-step/width是窗口重叠度
# TODO 调整以上两项

def window(filename, type, width=200, step=75):
    # 特征值(平均值，方差)(使用list储存各个传感器参数) + 实际的运动类型
    argvs = []
    # TODO 更多类型的特征值
    with open(filename, mode="r") as f:
        # 读入一行数据并将其分割后转化为一个float的list(共16个传感器参数)
        lines = [list(map(lambda x: float(x), l.split(",")[4:20]))
                 for l in f.readlines()]
    print(lines)
    for win in [lines[i:i + width] for i in range(0, len(lines) - 1, step)]:
        argv = []
        argv.append(list(np.average(np.array(win), axis=0)))
        argv.append(list(np.var(np.array(win), axis=0)))
        argv.append(type)
        # print(argv)
        argvs.append(argv)
    return argvs


# just for test
if __name__ == "__main__":
    argvs = window("../data/test/11test.csv", 1)
    print(argvs)
