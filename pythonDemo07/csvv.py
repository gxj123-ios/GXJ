import csv
def readCsv():
    url = open('testdata.csv','r',encoding='utf-8')
    reader = csv.reader(url)
    list=[]
    i=0
    for row in reader:
        if i!=0:
            list.append(row)
        i+=1
    return list

if __name__ == '__main__':
    reader = readCsv()
    for row in reader:
        print(row)