'''
实战五：计算学生成绩的分差及平均分

某学员的成绩如下:
课程 	分数
python 	95
English 	92
c语言 	89

请编写代码实现:

    Python课程和English课程之间的分数差
    三门课程的平均分
'''
print('python课程分数为95\nenglish课程的分数为92\nc课程的分数为89\n')
python = int(95)
english = int(92)
c = int(89)
print('python和english课程之间的分数差为：%d' % (python-english))
print('三个课程的分均分为：%d' % (int(python+english+c)/3))

