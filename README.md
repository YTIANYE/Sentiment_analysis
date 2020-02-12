# Sentiment_analysis

1.TextBlob基本介绍




TextBlob是一个用Python编写的开源的文本处理库。它可以用来执行很多自然语言处理的任务，比如，词性标注，名词性成分提取，情感分析，文本翻译，等等。你可以在官方文档阅读TextBlog的所有特性。
基本功能
•	Noun phrase extraction                         短语提取           
•	Part-of-speech tagging                            词汇标注
•	Sentiment analysis     情感分析
•	Classification (Naive Bayes, Decision Tree)          分类
•	Language translation and detection powered by Google Translate   语言翻译和检查（谷歌翻译支持）
•	Tokenization (splitting text into words and sentences)   分词、分句
•	Word and phrase frequencies   词、短语频率
•	Parsing                语法分析
•	n-grams               N元标注
•	Word inflection (pluralization and singularization) and lemmatization  词反射及词干提取
•	Spelling correction     拼写准确性
•	Add new models or languages through extensions       添加新模型或语言通过表达
•	WordNet integration       WordNet整合



2.程序运行说明：

如果第一次安装TextBlob，要下载必要的NLTK语料库。命令：
$ curl https://raw.github.com/sloria/TextBlob/master/download_corpora.py | python

如果已经安装TextBlob,需要更新则需要运行：
$ pip install -U textblob nltk

使用此命令下载语料库：
$ >python -m textblob.download_corpora




3.执行过程：

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


 
