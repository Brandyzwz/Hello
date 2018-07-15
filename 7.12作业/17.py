shengao = 1.75
tizhong = 80.5
BMI=float(tizhong/shengao**2)
print('小明的BMI值为%.2f'%BMI)
if BMI<18.5:
    print('过轻')
elif BMI<25 and BMI>=18.5:
    print('正常')
elif BMI>=25 and BMI<28:  
    print('过重')
elif BMI>=28 and BMI<32:
    print('肥胖')
elif BMI>=32:
    print('严重肥胖')  
