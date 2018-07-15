'''
实战十二：输出玫瑰花花语

使用 if---elif---else 多分支语句实现根据用户输入的玫瑰花的朵数输出其代表的含义
'''
flowers = int(input('玫瑰花话语，请输入您想要知道的玫瑰花朵数的含义：\n'))
while True:
    if flowers == 1:
        print('你是我的唯一')
        break
    elif flowers == 3:
        print('I Love You')
        break
    elif flowers == 10:
        print('十全十美')
        break
    elif flowers == 99:
        print('天长地久')
        break
    elif flowers == 108:
        print('求婚')
        break
    elif flowers == 999:
        print('土豪')
        break
    else:
        flowers=int(input('这个不知道，重新输吧！\n'))

