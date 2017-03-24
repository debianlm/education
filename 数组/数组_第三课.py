'''
Created on 2017年3月24日

@author: bufan
'''

# 我们定义一个空数组
shuzu=[]
print(shuzu)
print(len(shuzu))
# 下面这句话是不对的，因为这个时候数组是空的，而下面的程序试图使用 数组的第一个变量就会出现错误
# print(shuzu[0])

# 我们定义一个有 数字，变量 的数组
shuzu1=[1,"duoduo","大白"]
print(shuzu1)
print(len(shuzu1))
print("shuzu1的第一个变量值:",shuzu1[0])
print("shuzu1的第二个变量值:",shuzu1[1])
print("shuzu1的第三个变量值:",shuzu1[2])
print("shuzu1的倒数第一个变量值:",shuzu1[-1])
print("shuzu1的倒数第二个变量值:",shuzu1[-2])
print("shuzu1的倒数第三个变量值:",shuzu1[-3])
# 下面这句话是错误的，因为这个时候数组中只有3个变量，而［3］试图使用第四个变量，所以会出错
# print("shuzu1的第四个变量值:",shuzu1[3])
# print("shuzu1的倒数第四个变量值:",shuzu1[-4])

shuzu2=[1,shuzu1]
print(shuzu2)
print(len(shuzu2))
print("shuzu2的第一个变量值:",shuzu2[0])
print("shuzu2的第二个变量值:",shuzu2[1])
# 下面这句话是错误的，因为数组只有2个变量，第一个是数字1，第二个是一个数组，因此试图使用第三个变量就会出错
# print("shuzu1的第三个变量值:",shuzu2[2])

# 我们仔细看下面这个用法
print("shuzu2的第二个变量代表的数组，它的第一个变量值:",shuzu2[1][0])
print("shuzu2的第二个变量代表的数组，它的第二个变量值:",shuzu2[1][1])
print("shuzu2的第二个变量代表的数组，它的第三个变量值:",shuzu2[1][2])
# 下面这句话是错误的，因为shuzu2的第二个变量代表的数组只有3个变量，没有第四个变量
# print("shuzu2的第二个变量代表的数组，它的第三个变量值:",shuzu2[1][3])

# 相比较于上面的shuzu2［1］［0］这个用法，下面的用法更值得推荐
xiaoshuzu=shuzu2[1];
print("小数组它的第一个变量值:",xiaoshuzu[0])
print("小数组它的第二个变量值:",xiaoshuzu[1])
print("小数组它的第三个变量值:",xiaoshuzu[2])


