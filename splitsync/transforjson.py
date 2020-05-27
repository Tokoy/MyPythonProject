import os
import sys
import codecs
import xlrd
import xdrlib
import json


def open_ecxcel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(str(e))

#根据名称获取Excel表格中的数据   参数:file：Excel文件路径     colnameindex：表头列名所在行的所以  ，by_name：Sheet1名称
def excel_table_byname(file,colnameindex=0,by_name=u'Sheet1'):
    data = open_ecxcel(file)
    table = data.sheet_by_name(by_name)
    nrows = table.nrows
    colnames = table.row_values(colnameindex)
    records = []
    for rownum in range(1,nrows):
        row = table.row_values(rownum)
        if row:
            record = {}
            for i in range(len(colnames)):
                #excel 默认float ,强制类型转换
                if type(row[i]) == float:
                    row[i] = int(row[i])
                    row[i] = str(row[i])
                record[colnames[i]] = row[i]
        records.append(record)
    return records

recodes = excel_table_byname('data.xlsx')
encodedjson = json.dumps(recodes, ensure_ascii=False, indent=2).encode('utf-8')
with open('ips.json', 'wb') as d:
    d.write(encodedjson)
d.close()
