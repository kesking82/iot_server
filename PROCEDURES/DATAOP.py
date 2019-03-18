#!/usr/bin/env  python
# -*- coding: UTF-8 -*-
'''
Created on 2019年3月4日
@author: Kesking
'''

import json

def json_to_sql(data_dict,tab_name,op_flag):
    '''
    json数据转转成sql语句
    json: json格式的数据源
    tab_name: 操作的表名
    op_flag:"insert" 为insert操作，
            "update" 为update操作
            "delete" 为delete操作
    '''
    
    len_dict=len(data_dict)
    print(data_dict)
    if op_flag=="insert":
        column_name=""
        data_value=""
        n=1  #用于判读数据字典
        
        for key in data_dict.keys():
            if n==len_dict:
                column_name += key
                data_value  += "\""+data_dict[key]+"\""
                n += 1
            else:
                column_name += key+","
                data_value  += "\""+str(data_dict[key])+"\","
                n += 1
                
        sql_str='insert into {}({}) values ({})'.format(tab_name,column_name,data_value)
    elif op_flag=="update":
        pass
    elif op_flag=="delete":
        pass
    return sql_str
