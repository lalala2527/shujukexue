# -*- coding: utf-8 -*
import re
from openpyxl import Workbook

# 向sheet中写入一行数据
def insertOne(value, sheet):
    row = [value] * 1
    sheet.append(row)

# 新建excel，并创建多个sheet
book = Workbook()
# 新建1个自定义的sheet
sheet = book.create_sheet("sheet" + str(1), 0)
# 每个sheet里设置列标题
sheet.append(["评论" + str(1)])
sheets = book.get_sheet_names()
    
with open("test.txt","r",encoding="utf-8")as f:
    content=f.read()
rawResults = re.findall(">.*?<",content,re.S)
firstStepResults  = []
for result in rawResults:
    #print(result)
    if ">\'][\'<"  in result:
        continue
    if ">:<"  in result:
        continue
    if ">回复<"  in result:
        continue
    if "><"  in result:
        continue
    if ">\', \'<"  in result:
        continue
    if "@"  in result:
        continue
    if "> <"  in result:
        continue
    else:
        firstStepResults.append(result)
subTextHead = re.compile(">")
subTextFoot = re.compile("<")
i = 1
for lastResult in firstStepResults:
    resultExcel1 = re.sub(subTextHead, '', lastResult)
    resultExcel = re.sub(subTextFoot, '', resultExcel1)
    print(i,resultExcel)
     # 向sheet中插入数据
    insertOne(str(resultExcel),book.get_sheet_by_name(sheets[0]))
    i+=1

# 保存数据到.xlsx文件
book.save("test30.xlsx")
