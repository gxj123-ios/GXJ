import csv
def readCsv():
    path= r'F:\cs.csv'
    stream=open(path,'r')
    data= csv.reader(stream)
    list =[]
    i=0
    for row in data:
        if i!=0:
            list.append(row)
        i=i+1
    return list
if __name__ == '__main__':
    data=readCsv()
    for row in data:
        print(row)