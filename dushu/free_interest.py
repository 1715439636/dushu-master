import re

# ret_greed= re.findall(r'<T30805>(.*?)</T30805>',a)
# re = str(ret_greed).replace("['","").replace("',","\n").replace("'","").replace("]","")
# print("%s \r\n" % re)
# 本金为0.00的计算
f_in = open("file.xml",'r')
list_all = []
# 计算免息
for movie in f_in:
    ret_greed_principal_0 = re.findall(r'<T30811>(.*?)</T30811>', movie)

    principal_re = str(ret_greed_principal_0).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")

    if principal_re  !="":
        print(principal_re)