import re

# ret_greed= re.findall(r'<T30805>(.*?)</T30805>',a)
# re = str(ret_greed).replace("['","").replace("',","\n").replace("'","").replace("]","")
# print("%s \r\n" % re)
# 本金为0.00的计算
f_in = open("file.xml",'r')
list_all = []

for movie in f_in:
    ret_greed_principal_0 = re.findall(r'<T30805>(.*?)</T30805>', movie)

    principal_re = str(ret_greed_principal_0).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")

    if principal_re  !="":
        print(principal_re)










    # tag_a = movie.find('<T308>')
    # print(tag_a)
    # name = tag_a.text.replace(' ', '').replace('\n', '')

#
# for b in  f_in.readlines():
#
#        print(c)
    #
    # ret_greed_principal_0= re.findall(r'<T308>(.*?)</T308>',b)
    # print(ret_greed_principal_0)

    #     print("%s \r \n" % ret_greed_principal_0)
    #  print( (b))
    # principal_re = str(ret_greed_principal_0).replace("['","").replace("',","\n").replace("'","").replace("]","").replace("[ ","").replace("[","")
    # ret_greed_principal_1 = re.findall(r'<T30803>(.*?)</T30803>', b)
    # principal_re1 = str(ret_greed_principal_1).replace("['", "").replace("',", "\n").replace("'", "").replace("]","").replace("[ ", "").replace("[", "")
    # if principal_re == "0.00":
    #     print(principal_re)
    # else:
    #     print( principal_re1)
    # print( "%s \r \n" % principal_re)
    # ret_greed_principal_1 = re.findall(r'<T30803>(.*?)</T30803>', b)
    # principal_re = str(ret_greed_principal_1).replace("['", "").replace("',", "\n").replace("'", "").replace("]","").replace("[ ", "").replace("[", "")
    # print( ret_greed_principal_1)
    # ret_greed_principal_2 = re.findall(r'<T30812>(.*?)</T30812>', b)
    # principal_re = str(ret_greed_principal_2).replace("['", "").replace("',", "\n").replace("'", "").replace("]","").replace("[ ", "").replace("[", "")
    # print( ret_greed_principal_2)
