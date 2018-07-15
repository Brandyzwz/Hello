'''
实战十四: 简化版:猜数字游戏

编写一个猜数字的小游戏,电脑随机生成一个1到10之间的数字作为一个基准数,玩家输入一个数字,如果玩家的数字和电脑随机生成的基准数一致则输出"胜利",否则输出"失败,你是一个loser"
'''
import random
computer = random.randint(1,10)
player = int(input('请输入1~10中任意一个数：'))
while True:
    if player <= 10:
        if computer == player:
            print('胜利')
            break
        else:
            player=int(input('失败!再来一次:\n'))
    else:
        player=int(input('不好意思只能输入1～10的数字!再试一次吧！\n'))
