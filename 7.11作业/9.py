'''
实战九： 交换两个数

编写一个程序，用于实现两个数的交换
'''
a = int(input('请输入一个数a:\n'))
b = int(input('请输入一个数b:\n'))
a,b = b,a
print('a='+str(a),'b='+str(b))
