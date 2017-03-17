'''
Created on 2017年3月11日

@author: bufan
'''

# 假设  第一天工资 1粒米，第二天给我前一天的2倍， 请问工作一个月30天后，收到了多少元工资
# 已知 4元 可以购买1 1公斤大米，  而每一公斤大米含有 50000 颗米粒

# 在本节课里，我们使用此前学习过的 定义变量 的方式来解决

wage0=1
wage1=wage0*2
wage2=wage1*2
wage3=wage2*2
wage4=wage3*2
wage5=wage4*2
wage6=wage5*2
wage7=wage6*2
wage8=wage7*2
wage9=wage8*2
wage10=wage9*2
wage11=wage10*2
wage12=wage11*2
wage13=wage12*2
wage14=wage13*2
wage15=wage14*2
wage16=wage15*2
wage17=wage16*2
wage18=wage17*2
wage19=wage18*2
wage20=wage19*2
wage21=wage20*2
wage22=wage21*2
wage23=wage22*2
wage24=wage23*2
wage25=wage24*2
wage26=wage25*2
wage27=wage26*2
wage28=wage27*2
wage29=wage28*2

total_wage=wage0+wage1+wage2+wage3+wage4+wage5+wage6+wage7+wage8+wage9+\
            wage10+wage11+wage12+wage13+wage14+wage15+wage16+wage17+wage18+wage19+\
            wage20+wage21+wage22+wage23+wage24+wage25+wage26+wage27+wage28+wage29
print("第一种方法:一共赚了%d颗大米，相当于%d元人民币"%(total_wage,total_wage/50000*4))

'''
课后思考1: 如果让你计算365天的工资总收入，按照上面那个方法，能做吗？你愿意吗？
'''
