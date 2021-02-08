import requests
from requests.exceptions import RequestException
import re
import xml.sax
import pandas as pd
from lxml import etree
import chardet
import csv
import numpy as np

# !/usr/bin/python
# -*- coding: UTF-8 -*-

from xml.dom.minidom import parse

import xml.dom.minidom
dom1=xml.dom.minidom.parse('file.xml')
root=dom1.documentElement
book={}
booknode=root.getElementsByTagName('T308')
print("INSERT INTO TABLE  DW.E_DLXD_REPAY_DETAIL")
for booklist in booknode:
    # print( 'id:' + booklist.getAttribute('T30801'))
    repayment_1 = booklist.getElementsByTagName('T30801')[0].childNodes[0].nodeValue.strip()
    repayment_2 = booklist.getElementsByTagName('T30802')[0].childNodes[0].nodeValue.strip()
    repayment_3 = booklist.getElementsByTagName('T30803')[0].childNodes[0].nodeValue.strip()
    repayment_4 = booklist.getElementsByTagName('T30804')[0].childNodes[0].nodeValue.strip()
    repayment_5 = booklist.getElementsByTagName('T30805')[0].childNodes[0].nodeValue.strip()
    repayment_6 = booklist.getElementsByTagName('T30806')[0].childNodes[0].nodeValue.strip()
    repayment_7 = booklist.getElementsByTagName('T30807')[0].childNodes[0].nodeValue.strip()
    repayment_8 = booklist.getElementsByTagName('T30808')[0].childNodes[0].nodeValue.strip()
    repayment_9 = booklist.getElementsByTagName('T30809')[0].childNodes[0].nodeValue.strip()
    repayment_10 = booklist.getElementsByTagName('T30810')[0].childNodes[0].nodeValue.strip()
    repayment_11 = booklist.getElementsByTagName('T30811')[0].childNodes[0].nodeValue.strip()
    repayment_12 = booklist.getElementsByTagName('T30812')[0].childNodes[0].nodeValue.strip()
    repayment_13 = booklist.getElementsByTagName('T30813')[0].childNodes[0].nodeValue.strip()
    # repayment_1 = booklist.getElementsByTagName('T30802')[0].childNodes[0].nodeValue.strip()

    print("select  '" + repayment_1 + "'," + repayment_2 +  ",'" + repayment_3 +  "'," + repayment_4  + "," + repayment_5  + "," + repayment_6 + "," + repayment_7 + "," + repayment_8 + ","  + repayment_9 + "," + repayment_10  + "," + repayment_11 +  ",'" + repayment_12 +   "'," + repayment_13 + "  union all")

    # print("INSERT INTO TABLE  DW.E_DLXD_REPAY_DETAIL (" + repayment_1 + "," + repayment_2 +  "," + repayment_3 +  "," + repayment_4  + "," + repayment_5  + "," + repayment_6 + "," + repayment_7 + "," + repayment_8 + ","  + repayment_9 + "," + repayment_10  + "," + repayment_11 +  "," + repayment_12 +   "," + repayment_13 +")")

    # print(booklist)
    # # print ('id:'+booklist.getAttribute('T30801'))
    # for nodelist in  booklist.childNodes:
    #     # print(nodelist)
    #     if nodelist.nodeType ==1:
    #         print (nodelist.nodeName+':',)
    #     for node in nodelist.childNodes:
    #         print (node.data)

#
# #minidom解析器打开xml文档并将其解析为内存中的一棵树
# DOMTree=parse(r'file.xml')
# print(DOMTree)
# # 获取xml文档对象，就是拿到树的根
# booklist=DOMTree.documentElement
# print(booklist)
# #获取booklist对象中所有book节点的list集合
# books=booklist.getElementsByTagName('T308')
#
# # print (type(books))
#
# print('第一个book节点%s'%booklist.getElementsByTagName('T30802')[0])




# from xml.dom.minidom import parse
# import xml.dom.minidom
#
# # 使用minidom解析器打开 XML 文档
# DOMTree = xml.dom.minidom.parse("file.xml")
# collection = DOMTree.documentElement
#
# # # 在集合中获取所有电影
# movies = collection.getElementsByTagName("T308")
#
# print(movies)
#
# # # 打印每部电影的详细信息
# for movie in movies:
#     type = movie.getElementsByTagName('T30801')[0]
#     print(type)
#     print("Type: %s" % type.childNodes[0].data)
#     format = movie.getElementsByTagName('format')[0]
#     print("Format: %s" % format.childNodes[0].data)
#     rating = movie.getElementsByTagName('rating')[0]
#     print("Rating: %s" % rating.childNodes[0].data)
#     description = movie.getElementsByTagName('description')[0]
#     print("Description: %s" % description.childNodes[0].data)

# from xml.dom.minidom import parse
# import xml.dom.minidom
# DOMTree = xml.dom.minidom.parse("file.xml")
# collection = DOMTree.documentElement
# movies = collection.getElementsByTagName("T308")
#  # 打印每部电影的详细信息
# for movie in movies:
#     type = movie.getElementsByTagName('T30801')[1]
#     print(type)


#
# def get_html(f_in):
#     a = []
#     for movie in f_in:
#         loan_number = str(re.findall(r'<T30801>(.*?)</T30801>', str(movie))).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#贷款编号
#         a = loan_number
#         loan_voucher_No = str(re.findall(r'<T30802>(.*?)</T30802>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #借款凭证号
#         # lpy_date = str(re.findall(r'<T30803>(.*?)</T30803>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款日期(实收日)
#         # repayment_1 = str(re.findall(r'<T30804>(.*?)</T30804>', movie )).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款方式
#         # repayment_2 = str(re.findall(r'<T30805>(.*?)</T30805>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款本金
#         # repayment_3 = str(re.findall(r'<T30806>(.*?)</T30806>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #实收利息
#         # repayment_4 = str(re.findall(r'<T30807>(.*?)</T30807>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #罚息金额
#         # repayment_5 = str(re.findall(r'<T30808>(.*?)</T30808>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#还款序号
#         # repayment_6 = str(re.findall(r'<T30809>(.*?)</T30809>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#费用
#         # repayment_7 = str(re.findall(r'<T308010>(.*?)</T308010>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #应收利息
#         # repayment_8 = str(re.findall(r'<T308011>(.*?)</T308011>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#免息结息时间
#         # repayment_9 = str(re.findall(r'<T308012>(.*?)</T308012>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#还款方式
#         # repayment_10 =str( re.findall(r'<T308013>(.*?)</T308013>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #对应技术是否逾期
#         # item = [loan_number +","+loan_voucher_No]
#         print(a)
#         # df = pd.concat( [loan_number, loan_voucher_No], axis=1 )
#         # print(df)
#         pass
#     # return df
#
#
#
#
#
#
#
#
# def main():
#     items = []
#     f_in = open(r"file.xml",'r',encoding='UTF-8')
#     url = get_html(f_in)
#     items.append(url)
#     save_csv(items)
#
#
#
#
# def save_csv(items):
#      for i in items:
#         print(items)
#
#
#     # with open("招聘信息.csv", 'w', newline='', encoding='utf-8') as csvfile:
#     #     csv_tags = ['职位名称', '公司名称', '工作地点', '工作经验', '学历', '招聘人数', '发布时间', '公司性质', '公司规模',
#     #                   '所属行业', '工资']
#     #     writer = csv.writer(csvfile)
#     #     writer.writerow(csv_tags)
#     #     for item in items:
#     #         if item != None:
#     #             writer.writerow(item)
#
#
# if __name__ == '__main__':
#     main()
#
#
#
# # import re
# #
# # # ret_greed= re.findall(r'<T30805>(.*?)</T30805>',a)
# # # re = str(ret_greed).replace("['","").replace("',","\n").replace("'","").replace("]","")
# # # print("%s \r\n" % re)
# # # 本金为0.00的计算
# #
# #
# #
# # def movie_list(movie_s):
# #
# #     for movie in movie_s:
# #         loan_number = str(re.findall(r'<T30801>(.*?)</T30801>', str(movie))).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#贷款编号
# #         print(loan_number)
# #
# #
# #
# #
# #
# #
# # def main():
# #     f_in = open("file.xml", 'r')
# #     movie_s=movie_list(f_in)
# #     return movie_s
# #
# #
# # # def movie_list(f_in):
# # #     for movie in f_in:
# # #         loan_number = str(re.findall(r'<T30801>(.*?)</T30801>', str(movie))).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#贷款编号
# # #         # loan_number_1 = loan_number[0]
# # #         # loan_voucher_No = str(re.findall(r'<T30802>(.*?)</T30802>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #借款凭证号
# # #         # lpy_date = str(re.findall(r'<T30803>(.*?)</T30803>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款日期(实收日)
# # #         # repayment_1 = str(re.findall(r'<T30804>(.*?)</T30804>', movie )).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款方式
# # #         # repayment_2 = str(re.findall(r'<T30805>(.*?)</T30805>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #还款本金
# # #         # repayment_3 = str(re.findall(r'<T30806>(.*?)</T30806>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #实收利息
# # #         # repayment_4 = str(re.findall(r'<T30807>(.*?)</T30807>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #罚息金额
# # #         # repayment_5 = str(re.findall(r'<T30808>(.*?)</T30808>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#还款序号
# # #         # repayment_6 = str(re.findall(r'<T30809>(.*?)</T30809>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#费用
# # #         # repayment_7 = str(re.findall(r'<T308010>(.*?)</T308010>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #应收利息
# # #         # repayment_8 = str(re.findall(r'<T308011>(.*?)</T308011>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#免息结息时间
# # #         # repayment_9 = str(re.findall(r'<T308012>(.*?)</T308012>', movie) ).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")#还款方式
# # #         # repayment_10 =str( re.findall(r'<T308013>(.*?)</T308013>', movie)).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","") #对应技术是否逾期
# # #         print(loan_number)
# #
# #
# #     # print("INSERT INTO TABLE  DW.E_DLXD_REPAY_DETAIL (" + loan_number  + "," + loan_voucher_No + "," +lpy_date + "," +repayment_1 + "," +repayment_2 + "," +repayment_3 + "," +repayment_4 + "," +repayment_5 + "," +repayment_6 + "," +repayment_7 + "," +repayment_8 + "," +repayment_9 + "," +repayment_10)
# #
# #
# #     # ret_greed_principal_0 = re.findall(r'<T30806>(.*?)</T30806>', movie)
# #     # ret_greed_principal_1 = re.findall(r'<T30805>(.*?)</T30805>', movie)
# #     # principal_re = str(ret_greed_principal_0).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")
# #     # principal_re_1 = str(movie).replace("['", "").replace("',", "\n").replace("'", "").replace("]","").replace("[ ", "").replace("[", "")
# #     # if principal_re_1  !="":
# #     #     print(principal_re_1)
# #         # print( "INSERT INTO TABLE  DW.E_DLXD_REPAY_DETAIL (" + principal_re + "," + principal_re_1 + ")" )
# #         # # print(principal_re)