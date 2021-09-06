'''=======生成第一行矩阵的函数======='''
#调用库函数
import numpy as np

# 循环移位函数
def move(ls: list, offset):
    """
    元素原索引+位移数（正为右移，负为左移）之和就关于数组长度（数组的模）的余数，即为位移后的元素索引。
    再对新索引升序排序，去除索引，即为位移后的新数组
    ：param ls
    ：param offset
    ：return:
    """
    
    mod  = len(ls)
    ids = [[(item[0]+offset)%mod,item[1]] for item in enumerate(ls)]
    ids.sort(key=lambda item: item[0])
    return [item[1] for item in ids]


#定义全局变量
global b
global c
#
tries = 1
#a = 1
ny = int(input("请输入交织次数Nf:"))
while tries <= ny:
    locals()['a'+str(tries)] = int(input("请输入第%d次交叉浮长l%d:"%(tries,tries)))
    
    #生成列表
    if (tries % 2) == 0:
        locals()['lis'+str(tries)] = [0]*(locals()['a'+str(tries)])
    else:
        locals()['lis'+str(tries)] = [1]*(locals()['a'+str(tries)] )
    print(locals()['lis'+str(tries)])
    #合并列表
    if tries >= 2:
        b=b+locals()['lis'+str(tries)]
    else:
        b=locals()['lis'+str(tries)]
    tries+=1
else:
    Sj = int(input("请输入纱线飞数："))
    
#print(b)
#移动数组
i = 1
locals()['b'+str(0)] = []
while b != locals()['b'+str(i-1)]:
    locals()['b'+str(i)] = move(b,Sj*i)#b不变b2,b3永远一样，卡死。乘循环的次数可解决
    i+=1

#数组转为矩阵
else:
    for j in range(1,i):
       locals()['arr'+str(j)] = np.array(locals()['b'+str(j)])
       print(locals()['arr'+str(j)])

#矩阵的合并
#for d in range(1,i):
    


#取出a(x,y)绘制表格

