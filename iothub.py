#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
'''
Created on 2019年3月3日
@author: Kesking
'''



import time
import contextlib
from multiprocessing import Process
from DBAPI.DATABASE import mqtt_client
from PROCEDURES.LOGIC import data_process

if __name__ == '__main__':
    my_mqtt=mqtt_client("web_url", port_num,"username", "password",data_process)  
    #启动一个后台进程用于执行mqtt-client
    p=Process(target=my_mqtt.connect)
    p.start()
    print("process started")
    while 1:
        time.sleep(1)
        print(time.ctime(time.time()))

    