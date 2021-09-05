#生成第一行矩阵的函数
#import numpy as np


tries = 1
a = 1
ny = int(input("请输入Nf:"))
while tries <= ny:
    locals()['a'+str(tries)] = int(input("请输入l%d:"%(tries,)))
    
    #生成列表
    if (tries % 2) == 0:
        locals()['lis'+str(tries)] = [0]*(locals()['a'+str(tries)])
    else:
        locals()['lis'+str(tries)] = [1]*(locals()['a'+str(tries)] )
    print(locals()['lis'+str(tries)])
    
    '''if (tries >= 2):
        locals()['lis'+str(tries)]+=locals()['lis'+str(tries - 1)]'''
    tries+=1
else:
    Sj = input("请输入纱线飞数：")
#合并列表
while a < ny:
    locals()['lis'+str(a)]+=locals()['lis'+str(a+1)]
    a+=1
    print(locals()['lis'+str(a-1)])
