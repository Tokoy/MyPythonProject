import jsonlist
import sync
import check
import json
import control
import transforjson
import time
import threading
from concurrent.futures import  ThreadPoolExecutor,as_completed
import paramiko

file = "/work/test"
source = {"ip": "", "status": "", "password": ""}
target = {"ip": "", "status": "", "password": ""}
jsondata = jsonlist.read_json_file('ips.json')


if __name__ == '__main__':
    executor = ThreadPoolExecutor(5)
    while check.checkexit(jsondata):
        source = {"ip": "", "status": "", "password": ""}
        target = {"ip": "", "status": "", "password": ""}
        i = 0
        while i < len(jsondata):
            if jsondata[i]["status"] == "1":
                 source = jsondata[i]
            elif jsondata[i]["status"] == "0":
                 target = jsondata[i]
            i = i + 1
            if source["ip"] != "" and target["ip"] != "":
                jsonlist.change_jdata(jsondata, source["ip"], "2")
                jsonlist.change_jdata(jsondata, target["ip"], "2")
                executor.submit(sync.sync_data,source["ip"], source["password"], target["ip"], target["password"], file, jsondata)
                source = {"ip": "", "status": "", "password": ""}
                target = {"ip": "", "status": "", "password": ""}





