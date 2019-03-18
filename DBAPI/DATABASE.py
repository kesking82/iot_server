#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
'''
Created on 2019年3月2日
@author: Kesking
'''
# import time
from contextlib import contextmanager
import mysql.connector
import paho.mqtt.client as mqtt
#from TOOLS.THREAD import thread_create,thread_start
import threading

###mysql连接
class db_mysql():
    def __init__(self,user,password,host,database):
        self.user=user
        self.password=password
        self.host=host
        self.database=database
        print("mysql config")
    
    @contextmanager
    def connect(self):
        try:
            config={'user':self.user,
                    'password':self.password,
                    'host':self.host,
                    'database':self.database,
                    'charset':'utf8'}
            conn=mysql.connector.connect(**config)
            cur=conn.cursor(dictionary=True)
            print("Mysql Connected")
            try:    
                yield cur
            finally:
                conn.commit()
                cur.close()
                conn.close()
                print("Mysql Closed")
        except Exception as e:
            print(e)
            exit()



class mqtt_client():
    def __init__(self,host,port,username,password,func):
        '''
        mqtt-borker收到消息后，开启一个线程处理
        func 为需要处理的流程
        '''
        self.host=host
        self.port=port
        self.username=username
        self.password=password
        self.func=func
        
        
  
    def connect(self):
        def on_connect(client, userdata, flags, rc):
            print("Connected with result code "+str(rc))
            client.subscribe([("weather",1),("test",1)])
        
        def on_message(client, userdata, msg):
            print(str(msg.timestamp))
            mythread=threading.Thread(target=self.func,args=(msg,))
            mythread.start()
        
        client = mqtt.Client()
        client.on_connect = on_connect
        client.on_message = on_message
        client.username_pw_set(self.username, self.password) 
        client.connect(self.host,self.port, 60)
        client.loop_forever()
        
    