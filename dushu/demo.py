#-*- coding: utf-8 -*-

from impala.dbapi import connect
from impala.util import as_pandas
import pandas as pd
import numpy as np
#连接数据
conn=connect(host='10.18.19.218',port=21050)
cur=conn.cursor()
cur.execute('show databases;')
print(cur.fetchall())




# from impala.dbapi import connect
#
# conn = connect(host='10.18.19.217', port=21050)
# #conn = connect(host=host, port=prot_impala, user='', password='', auth_mechanism='')
# cur = conn.cursor()
# # cur.execute('select * from DW.E_DLXD_REPAY_DETAIL ')
# data_list=cur.fetchall()
#
# for data in data_list:
#     print("用户名称:" + str(data[0]))


# import sys
# from pyhive import hive
# conn = hive.Connection(host='10.18.19.217', port=10000, username='hdfs', database='default')
# cursor = conn.cursor()
# cursor.execute('show tables')
#
# for result in cursor.fetchall():
#     print(result)