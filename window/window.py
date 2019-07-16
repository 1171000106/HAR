import numpy as np


# 将文件中的数据分成不同的窗口
# width是窗口宽度
# 1-step/width是窗口重叠度
# TODO 调整以上两项

def cal_window(filename, type, ave, std, width=200, step=77):
    # 特征值(平均值，方差)(使用list储存各个传感器参数) + 实际的运动类型
    argvs = []
    # TODO 更多类型的特征值
    with open(filename, mode="r") as f:
        # 读入一行数据并将其分割后转化为一个float的list(共16个传感器参数)
        lines = [list(map(lambda x: float(x), l.split(",")[4:20]))
                 for l in f.readlines()]

    def ff(line):
        return [(x - x_) / s for x, x_, s in zip(line, ave, std)]

    # print(lines[0])
    for i in range(len(lines)):
        lines[i] = ff(lines[i])
    # print(lines[0])
    for win in [lines[i:i + width] for i in range(0, len(lines) - 1, step)]:
        argv = []
        # 数据去噪
        Qa = [];
        lw = len(win);
        #print(win);
        for i in range(0,lw-2):
            ln = len(win[i]);
            sv = win[i];
            for j in range(0,ln):
                sum = [win[i+1][j],win[i+2][j],win[i][j]];
                sum.sort();
                sv[j] = sum[1];
            Qa.append(sv);
        argv.append(list(np.average(np.array(Qa), axis=0)))
        argv.append(list(np.var(np.array(Qa), axis=0)))
        argv.append(type)
        # print(argv)
        argvs.append(argv)
    return argvs


def normalize():
    teachers = []
    for i in [1, 2, 3, 4, 5, 6, 8, 10, 11]:
        filename = "../data/teacher/" + str(i) + "oo.csv"
        with open(filename, mode="r") as f:
            # 读入一行数据并将其分割后转化为一个float的list(共16个传感器参数)
            lines = [list(map(lambda x: float(x), l.split(",")[4:20]))
                     for l in f.readlines()]
        teachers.extend(lines)
    # print(teachers)
    ave = list(np.average(np.array(teachers), axis=0))
    std = list(np.std(np.array(teachers), axis=0))
    # print(ave, std)
    return ave, std


# just for test
if __name__ == "__main__":
    argvs = cal_window("../data/test/11test.csv", 1)
    print(argvs)
