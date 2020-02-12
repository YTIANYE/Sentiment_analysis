# -*- coding:utf-8 -*-
#
# f = open(r'dev2.txt','r')
# a=[
#     i for i in f
#
#    ]
# print(a)
# f.close()


# 训练数据
f = open(r'train.txt','r',encoding='UTF-8')
# 按行读出文件内容
sourceInLines = f.readlines()
f.close()
# 定义一个空列表，用来存储结果
new = []
for line in sourceInLines:
    temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
    # print(tuple(temp1.split("\t")), ",")
    temp3 = temp1.split("\t")
    temp3.reverse() # 反向
    # print(temp3)
    # temp2 = temp1.split(',')  # 以','为标志，将每行分割成列表
    # new.append(temp3)  # 将上一步得到的列表添加到new中
    new.append(tuple(temp3))  #tuple(temp3)列表转换为元组
print(new)
# k = dict(new)#转化为字典
# print(k)
# sorted(k.items,key=lambda item:item[1])
# print(k)


