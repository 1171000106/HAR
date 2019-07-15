import sys

import numpy as np
from math import *
from functools import reduce

sys.path.append('../window')
from window import window


def calc_eucl(x, y):
    return sqrt(np.sum([(xx - yy) ** 2 for xx, yy in zip(x, y)]))


# kNN
def knn(teachers, tests, cal_func, k=3):
    # 记录各种行为在周围k个元素中出现了几次
    result = {}
    tmp = [[cal_func(teacher[:-1], test[:-1]), teacher[-1]] for test in tests for teacher in teachers]
    # 排序选出最近的k个元素
    for kth in sorted(tmp, key=lambda x: x[0])[:k]:
        # print(kth)
        result[kth[1]] = 1 if kth[1] not in result else result[kth[1]] + 1
    # print()
    # 返回这k个元素中出现次数最多的类别
    return sorted(result.items(), key=lambda x: x[1], reverse=True)[0][0]


# 判断预测动作和实际动作是否一致
def is_equal(ans, pre):
    return ans == pre


if __name__ == "__main__":
    # 训练集
    teacher = []
    for i in [1, 2, 3, 4, 5, 6, 8, 10, 11]:
        print(i)
        teacher = [d for d in window("../data/teacher/" + str(i) + "oo.csv", i)]

    # 测试集
    test = [d for d in window("../data/test/1test.csv")]
    # print(test)
    # 测试结果
    cor = reduce(lambda a, b: a + b, [is_equal(i[-1], knn(teacher, i[:-1], calc_eucl)) for i in test])
    # 输出各种结果
    print("Accuracy : " + str(cor / len(test) * 100) + " %")
    print(test[0][-1])
    print(knn(teacher, test[0][:-1], calc_eucl))
