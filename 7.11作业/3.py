'''
实战三: 根据身高、体重计算BMI指数

创建一个名称为bmiexponent.py文件,然后该文件中定义两个变量：一个用于记录身高（单位：米） 另外一个用于记录体重（单位：千克） 根据公式：‘BMI=体重/(身高X身高)’,计算BMI指数并且使用print()输出
'''
shengao = float(input('请输入您的身高m：'))
tizhong = float(input('请输入你的体重kg：'))
BMI = float(tizhong/(shengao*shengao))
print('您的BMI值为：%.2f' % BMI)
