import json
import os , sys
import jsonlist

def checkexit(jsondata):    #如果判断全部都为1的情况，那就返回false 跳出检查 结束脚本
	result = True
	i = 0
	leng = len(jsondata)
	while i < leng:
		if jsondata[i]["status"] == "1":
			result = False
		else:
			result = True
			break
		i = i + 1
	return  result

