# 输入直角三角形的两个直角边的长度a、b 求斜边c的长度并且使用print()输出
a = int(input('输入直角边a的值：'))
b = int(input('输入直角边b的值：'))
print('斜边c为：%d' % int((a**2+b**2)**0.5))
