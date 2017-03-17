'''
Created on 2017年2月14日

@author: bufan
'''

import random

# 产生一个随机数，在1-99之间
secret=random.randint(1,99)
print(secret)
#secret=random.randint(1,99)
#print(secret)
#exit()

# 猜测的数字
guess=0

# 猜测的次数
tries=0

print("AHoY!i'm the darad pirate roberts, and i have a secret!") 
print("it is a number from 1 to 99. i'11 give you 6 tries. ")

while guess!=secret and tries<6 :
    guess = int(input("what's yer guess?"))  
    if guess<secret:
        print("太小"  )
    elif guess >secret:
        print("太大")
    tries=tries+1

if guess==secret: 
    print("AVast! Ye got it! found my secret, Ye did!")
print("no more guesses! better luck next time, mateey!   ")
print("the secret number was"), secret
