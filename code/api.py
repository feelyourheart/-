###利用 Python 数据模型的 API 建立一个数据接口类并实现数据可视化

import jieba                       #引入所需库
import jieba.posseg as pseg
import matplotlib.pyplot as plt

seg_list = []
class Cut():
    """分词并统计类"""

    def __init__(self,name):
        """初始化属性"""
        self.name = name
        self.labels = ['n','v','d','a','p']  #词性标签,主要对名词，动词，副词，形容词及介词进行统计
        self.num_list = [0,0,0,0,0]  #数量列表

    def __getitem__(self,index):
        """实现类对象取索引返回词和词性两项主要信息"""
        with open(self.name,"r",encoding='utf-8') as f:
            for line in f.readlines():
                for w in pseg.cut(line):  #使用jieba对line分词及词性标注
                    seg_list.append(w)
            return seg_list[index] 

    def show_pie(self):
        """运用jieba分词实现词性统计并用饼图可视化"""
        with open (self.name,'r',encoding='utf-8') as f1:
            for line in f1.readlines():
                words = pseg.cut(line)  #使用jieba对line分词及词性标注
                for x in words:
                    if x.flag  in self.labels:  #判断x的词性是否存在词性列表中
                        if x.flag == 'n':
                            index1 = 0
                        if x.flag == 'v':
                            index1 = 1
                        if x.flag == 'd':
                            index1 = 2
                        if x.flag == 'a':
                            index1 = 3
                        if x.flag == 'p':
                            index1 = 4
                        self.num_list[index1] += 1  #统计各类词性总数
        rate = []
        for i in range(len(self.num_list)):
            result = self.num_list[i]/sum(self.num_list)  #获取词性频率
            rate.append(result)
        plt.rcParams['font.sans-serif'] = ['SimHei']  #引入绘图数据
        plt.pie(x=rate,autopct='%1.2f%%',labels=self.labels)
        plt.title(self.name+"主要词性分布统计图")
        plt.show()  #输出饼图