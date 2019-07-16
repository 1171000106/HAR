import sys

import numpy as np
from math import *
from functools import reduce

sys.path.append('../window')
from window import window


# TODO 正规化数据
def calc_eucl(x, y):
    dis = []
    for i in range(len(x)):
        # print(len(x[i]), len(y[i]))
        # print(len([(xx - yy) ** 2 for xx, yy in zip(x[i], y[i])]))
        dis.append(sqrt(np.sum([(xx - yy) ** 2 for xx, yy in zip(x[i], y[i])])))
    return dis


# TODO 其他的距离计算方式


# TODO 不同的k
# kNN
def knn(teachers, test, cal_dis, k=3):
    # 记录各种行为在周围k个元素中出现了几次
    result = {}
    tmp = [[cal_dis(teacher[:-1], test), teacher[-1]] for teacher in teachers]
    # 排序选出最近的k个元素
    for kth in sorted(tmp, key=lambda x: np.sum([xx**2 for xx in x[0]]))[:k]:
        # print(kth)
        result[kth[1]] = 1 if kth[1] not in result else result[kth[1]] + 1
    # print()
    # 返回这k个元素中出现次数最多的类别
    return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]


# 判断预测动作和实际动作是否一致
def is_equal(ans, pre):
    return ans == pre


if __name__ == "__main__":
    # TODO 数据去噪
    # 训练集
    teacher = []
    for i in [1, 2, 3, 4, 5, 6, 8, 10, 11]:
        print(i)
        teacher.extend([d for d in window("../data/teacher/" + str(i) + "oo.csv", i)])

    # 测试集
    test = []
    for i in [1, 2, 3, 4, 5, 6, 8, 10, 11]:
        print(i)
        test.extend([d for d in window("../data/test/" + str(i) + "test.csv", i)])
    # print(test)
    # TODO 混淆矩阵
    # 测试结果
    cor = reduce(lambda a, b: a + b, [is_equal(i[-1], knn(teacher, i[:-1], calc_eucl)) for i in test])
    # TODO 其他表征结果的参数
    # 输出各种结果
    print("Accuracy : " + str(cor / len(test) * 100) + " %")
