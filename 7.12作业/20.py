a = int(input('请输入查询年份：\n'))
if a%4==0 and a%100!=0:
    print('%d年是闰年'%a)
elif a%400==0:
    print('%d年是闰年'%a)
else:
    print('这是平年')
