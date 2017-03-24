'''
Created on 2017年3月24日

这节课我们上 python 数组的 添加、插入、删除、遍历的操作

@author: bufan
'''
# 这个程序我们演示, 我们实现不知道有多少个变量的时候，如何用数组存储
# 题目: 请从键盘依次输入你同班同学的名称，以空输入作为结束
shuzu=[]    # 我们先定义一个空数组，因为我们不知道有多少个同学
isInput=True   # 定义一个变量，表示当前是否处于输入同学名称状态,刚开始时候是 True，表示“是的"
name=""   # 定义一个变量，表示当前输入同学的名称

while isInput:
    name=input("请输入你班级同学的名字:")
    if name == "" :
        isInput = False   # 输入为空，表示输入结束了
        print("输入结束")
    else:
        shuzu.append(name)

# 下面我们遍历整个数组，把每个同学的名称显示出来
i=1  # 表示当前是第几个学生
for name in shuzu:
    print("不知道有多少个同学的遍历方法:第%d个同学的名字:%s"%(i,name))
    i=i+1
    
# 如果我们实现就知道数组里有多少个变量，我们也可以这么做
number=len(shuzu)   # 这个获取数组的长度，也就是收集，一共输入了多少个学生

for i in range(number):
    print("直到有多少个同学的遍历方法：第%d个同学的名字:%s"%(i+1,shuzu[i]))
