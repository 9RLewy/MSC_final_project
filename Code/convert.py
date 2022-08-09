
import csv


csv_file = csv.reader(open('testset-levelc.csv', 'r', encoding='UTF-8'))
csv_file1 = csv.reader(open('labels-levelc.csv', 'r', encoding='UTF-8'))
fo = open("testset-levelc.txt", "w", encoding='UTF-8')

record = []
lewy ={}
count = 0
t=0
a=0
s=0
for row1 in csv_file1:
    lewy[t]=row1[1]
    t=t+1
for row in csv_file:
    count1=0
    if(s==0):
        fo.write(row[0]+","+row[1]+"\n")
        s=s+1
    else:
        list2=[]
        for i in range(len(row[1])):
            if row[1][i] == '"':
                list2.insert(count,i)
                count1 = count1+1
                print(count1)
        x=len(row[1])
        list1=list(row[1])
        print(list1)
        list1.insert( 0, '"')
        list1.insert( x+1, '"')
        q=1
        print(len(list2))
        if(len(list2)!=0):
            for m in range(0,count1):  
                print(list2[m])
                list1.insert( list2[m]+q, '\\')
                q=q+1
        s="".join(list1) 
        fo.write(row[0]+","+s+","+lewy[a]+"\n")
        a=a+1
        if count < 100:
            print(row)
        count += 1