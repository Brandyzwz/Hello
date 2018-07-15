'''
实战二十九: 鸡兔同笼问题
假设共有鸡、兔30只，脚90只，求鸡、兔各有多少只?
'''
i = 0
j = 0
while i <= 30:
    if i == (90-2*30)/(4-2):
        print('兔子数为%d'%i)
        if True:
            j=30-i
            print('鸡数为%d'%j)
            break
    else:
        i+=1 
