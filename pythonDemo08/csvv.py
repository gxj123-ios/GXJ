import csv


def readCsv():
    url = open('testdata.csv', 'r', encoding='utf-8')
    data = csv.reader(url)
    list = []
    i = 0
    for row in data:
        if i != 0:
            list.append(row)
        i += 1
    return list


if __name__ == '__main__':
    data = readCsv()
    for row in data:
        print(row)
