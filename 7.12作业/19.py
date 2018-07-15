print('颜值大比拼')
g = int(input('请输入身高：\n'))
j = int(input('请输入身价：\n'))
y = int(input('请输入颜值分：\n'))
if g>180 and j>1000000 and y>99:
    print('高富帅')
elif j>1000000 and y>99:
    print('富帅')
elif y>99:
    print('帅')
elif g<160 and j<100 and y<60:
    print('矮穷挫')
else:
    print('不知道你是神码鬼东西')
