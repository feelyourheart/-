###分析两本类型不同的现代小说的词性分布其一

from api import Cut  #从api模块中引入Cut类

novel1 = r"C:\Users\86178\Desktop\Python程序设计\《活着》.txt"
cut1 = Cut(novel1)  #实例化对象1
print(cut1[99])  #类对象取索引
cut1.show_pie()  #获取词性分布统计饼图