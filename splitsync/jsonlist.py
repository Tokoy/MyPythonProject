import os,sys
import json
import requests

#状态值    0 为可传输   1为已传输  2为正在传输

#可以匹配，一个0和一个1 则开始建立一条线程进行传输，状态都改为2，传输完毕后，状态都改为 1
#死循环检查各个key的value，当全部为1的时候执行完毕脚本。
#查询key并修改value
def change_json_status(filepath,key,value):
	key_ = key
	with open(filepath, 'rb') as f:
		json_data = json.load(f)
		key_length = len(json_data)
		i = 0
		a = json_data
		while i < key_length:
			if a[i]["ip"] == key_:
				a[i]["status"] = value
			i = i + 1
	f.close()
	rewrite_json_file(filepath,json_data)


def rewrite_json_file(filepath, json_data):
	with open(filepath, 'w') as f:
		json.dump(json_data, f)
	f.close()

#读取json数据
def read_json_file(filepath):
	with open(filepath, 'rb') as f:
		json_data = json.load(f)
	f.close()
	return json_data


def change_jdata(jdata,key,value):
    key_length = len(jdata)
    i = 0
    a = jdata
    while i < key_length:
        if a[i]["ip"] == key:
            a[i]["status"] = value
        i = i + 1




