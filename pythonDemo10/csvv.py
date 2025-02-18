import csv

def readCsv():
    url = open('testdata.csv','r',encoding='utf-8')
    reader = csv.reader(url)
    list = []
    i=0
    for row in reader:
        if i!=0:
            list.append(row)
        i+=1
    return list

if __name__ == '__main__':
    url =readCsv()
    for row in url:
        print(row)