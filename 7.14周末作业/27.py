i = 200
while i <= 200:
    if i%17 != 0:
        i-=1
    else:
        print('200以内能被17整除的最大整数为%d'%i)
        break
