import os
import csv
import os.path
import re

outputdir = os.getcwd()+"\\yyyyyyyyy\\"
zzzzzzzzzdir  = os.chdir(os.getcwd()+"\\zzzzzzzzz\\")
dailyreports = os.listdir(os.getcwd())
filecount = len(dailyreports)
rownumber = 5 
writestartindex = 5
haba = 3

def add(row,row1,row2):
    if row == '' and row1 == '' and row2 == '':
        return ''
    else:
        if row == '':
            hour2 = 0
        else:
            hour2 = int(row)
        if row1 == '':
            hour1 = 0
        else:
            hour1 = int(row1)
        if row2 == '':
            redelivery = 0
        else:
            redelivery = int(row2)
    return hour2+hour1+redelivery

for day in range(1,filecount+1):
    filename = str(day) + "日.csv" 
    index = dailyreports.index(filename)
    #ファイル読み込み
    with open(dailyreports[index],'r') as f1:
        dataReader = csv.reader(f1)

        #ファイル書き込む
        for row in dataReader:
            writeendindex = len(row)
            result = []
            result.append(rownumber)
            with open(outputdir+str(row[0])+".csv",'a') as f2:
                for num in range(writestartindex,writeendindex-1,haba):
                    dda = re.match('^M\+\d+$',row[num])
                    dda1 = re.match('^M\+\d+$',row[num+1])
                    dda2 = re.match('^M\+\d+$',row[num+2])

                    if dda:
                        hour2Obj = re.search('\d+',dda.group())
                        hour1Obj = re.search('\d+',dda1.group())
                        redeliveryObj = re.search('\d+',dda2.group())
                        slotcount = "M" +  "+" +  str(add(hour2Obj.group(),hour1Obj.group(),redeliveryObj.group()))
                    elif row[num] != "M":
                        slotcount = add(row[num],row[num+1],row[num+2])
                    else:
                        slotcount = row[num]
                    result.append(slotcount)
                writer = csv.writer(f2,lineterminator='\n')
                writer.writerow(result)
    rownumber = rownumber+1