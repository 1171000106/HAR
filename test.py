if __name__ == '__main__':
    with open("./data/2.csv", mode="r") as f:
        lines = [(l.split(",")[4:7]) for l in f.readlines()[1:]]
    i = 1
    for line in lines:
        print(i)
        i += 1
        if line[0] == '':
            continue
        print([float(l) for l in line])
