###分析两本类型不同的现代小说的词性分布其二

from api import Cut  #从api模块中引入Cut类

novel2 = r"C:\Users\86178\Desktop\Python程序设计\《神雕侠侣》.txt"
cut2 = Cut(novel2)  #实例化对象2
print(cut2[99])
cut2.show_pie()