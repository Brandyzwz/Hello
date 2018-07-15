nu = 10086
mi = 000
money = 100897.79
a=int(input('欢迎使用iii提款机，请输入您的帐号：\n'))
b=int(input('请输入您的密码:\n'))
if a==nu and b==mi:
    print('密码正确')        
    c=int(input('请输入您的取款金额'))
    if c<money: 
        print('本次取走%d元,账户余额为%.2f'%(c,money-c))
    else:
        print('余额不足')
else:
   print('非法账户')
