'''
Created on 2017年3月24日

这节课我们上 python 数组的 添加、插入、删除、遍历的操作

@author: bufan
'''
from re import search

# 这个程序我们展示下，如果使用已知固定长度的数组

# 题目是: 已知太阳有7种颜色，请用一个数组对颜色进行存储
# 就在这个 range 后面填写你要的哪个数组 
shuzu = [0 for x in range(7)]
# 这个时候我们就可以通过[这儿填写一个0开始的数字] 来访问需要的变量了
shuzu[0] = "红"
shuzu[1] = "橙"
shuzu[2] = "黄"
shuzu[3] = "绿"
shuzu[4] = "青"
shuzu[5] = "蓝"
shuzu[6] = "紫" 
print("一开始颜色表有%d种颜色，分别是:%s"%(len(shuzu),shuzu))


# 这个时候如果我们发现了有一种其他颜色，比如是 “灰色” 想加入到上述颜色表的最后面
shuzu.append("灰") 
print("加入了灰色后颜色表有%d种颜色，分别是:%s"%(len(shuzu),shuzu))

# 然后，有小朋友，想把“咖啡色” 加入到第二个颜色
shuzu.insert(1,"咖啡")
print("加入了咖啡色颜色表有%d种颜色，分别是:%s"%(len(shuzu),shuzu))

# 然后有小朋友不小心，把“红色”又添加了一遍,加到了最后，注意 －1的用法，看看红色在哪儿？想想为什么
shuzu.insert(-1,"红")
print("红色又被添加后颜色表有%d种颜色，分别是:%s"%(len(shuzu),shuzu))

# 我们这个时候需要把颜色表中最后添加的红色删除 , 请主意观察，哪个红色被删除了
shuzu.remove("红")
print("红色删除后颜色表有%d种颜色，分别是:%s"%(len(shuzu),shuzu))

# 这个时候需要寻找下 “绿”是第几个颜色
i=shuzu.index("绿")
print("绿色排在第%d位"%(i+1))

# 如果我们查找一个不存在的颜色会发生什么事情
i=shuzu.index("x")
