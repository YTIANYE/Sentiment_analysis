from textblob.classifiers import NaiveBayesClassifier

# 训练数据
f_train = open(r'train1.txt','r', encoding='UTF-8')
# 按行读出文件内容
sourceInLines = f_train.readlines()
f_train.close()
# 定义一个空列表，用来存储结果
train = []
for line in sourceInLines:
    temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
    # print(temp1.split("\t"))
    temp3 = temp1.split("\t")
    temp3.reverse() # 反向
    train.append(tuple(temp3))  #tuple(temp3)列表转换为元组
print(train)

# 验证数据
f_test = open(r'dev.txt','r', encoding='UTF-8')
# 按行读出文件内容
sourceInLines = f_test.readlines()
f_test.close()
# 定义一个空列表，用来存储结果
test = []
for line in sourceInLines:
    temp1 = line.strip('\n')  # 去掉每行最后的换行符'\n'
    # print(temp1.split("\t"))
    temp3 = temp1.split("\t")
    temp3.reverse() # 反向
    test.append(tuple(temp3))  #tuple(temp3)列表转换为元组
print(test)

# 通过将训练数据传递给NaiveBayesClassifier的构造函数来创建一个新的分类器。
cl = NaiveBayesClassifier(train)

#举例验证
# 选自dev.txt
# 0	exactly what you'd expect from a guy named kaos .
# 1	ryan gosling . . . is at 22 a powerful young actor .
# 0	rock's stand-up magic wanes . hopkins , squarely fills the screen . action - mechanical .
# 可以使用NaiveBayesClassifier.classify（text）方法对任意文本进行分类。
a = cl.classify("exactly what you'd expect from a guy named kaos . ")  # 结果为 0
print(a)
b = cl.classify("ryan gosling . . . is at 22 a powerful young actor .")  # 结果为 1
print(b)
c = cl.classify("rock's stand-up magic wanes . hopkins , squarely fills the screen . action - mechanical . ")  # 结果为0
print(c)

# 检查测试集的准确性。
z = cl.accuracy(test) #  结果为 0.648217636022514
print(z)

