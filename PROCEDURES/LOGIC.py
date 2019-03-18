#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
'''
Created on 2019年3月2日
@author: Kesking

LOGIC.py 包含了程序的主要逻辑
'''

from DBAPI.DATABASE import db_mysql
from PROCEDURES.DATAOP import json_to_sql
import json

def  __data_to_db(data_dict,tab_name,op_flag):
    sql_str=json_to_sql(data_dict,tab_name,op_flag)
    print(sql_str)
    inst_mysql=db_mysql('dbusername','dbpassword','dbip','dbname')
    print("ok")
    with inst_mysql.connect() as q:
        try:
            q.execute(sql_str)
            print("operation on table {} is completed! ".format(tab_name))
            return 0
        except Exception as e:
            print(str(e))
            return 1

##该函数用于mqtt-clent里的on_message里的回调
def data_process(msg):
    '''
    msg为MQTT订阅返回的 MQTTMessage
    '''
    payload_json=msg.payload
    payload_dict=json.loads(payload_json)
    data_dict={}
    data_dict['topic_name']=msg.topic
    data_dict['data_value']=payload_dict['value']
    data_dict['data_time']=payload_dict['time']
    __data_to_db(data_dict,'sensor_data','insert')
    