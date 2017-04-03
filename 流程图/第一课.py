'''
Created on 2017年4月3日

@author: bufan
'''
num_1=int(input("请输入第一个数字:"))
num_2=int(input("请输入第二个数字:"))

if num_1 == 0  and num_2 == 0:
    print("两个数字都是0")
else:
    sum_num = num_1+num_2
    if sum_num % 2 == 0:
        print("他们的和是偶数")
    else:
        print("他们的和是奇数")   