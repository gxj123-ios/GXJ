import csv
def readCsvv():
    path = 'testdata.csv'
    stream = open(path, 'r')
    data = csv.reader(stream)
    list = []
    i = 0
    for row in data:
        if i != 0:
            list.append(row)
        i = i + 1
    return list


if __name__ == '__main__':
    data = readCsvv()
    for row in data:
        print(row)