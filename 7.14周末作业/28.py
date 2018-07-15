print('面试资格确认')
a =int(input('输入年龄：\n'))
b = input('输入专业：\n')
c = input('是否为重点大学：\n')
while True:
    if a > 25 and b == '电子信息工程':
        print('通过面试，成功被录取')
        break
    elif b== '电子信息工程' and c == '是':
        print('通过面试，成功被录取')
        break
    elif a < 28 and b == '计算机':
        print('通过面试，成功被录取')
        break
    else:
        print('抱歉，您未达到面试要求')
        break
