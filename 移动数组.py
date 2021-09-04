def move(ls: list, offset):
    
    
    mod  = len(ls)
    ids = [[(item[0]+offset)%mod,item[1]] for item in enumerate(ls)]
    ids.sort(key=lambda item: item[0])
    return [item[1] for item in ids]

def move2(ls: list, offset):
    
    mod = len(ls)
    offset = offset % mod
    tail = list(reversed(ls[mod-offset:]))
    head = list(reversed(ls[:mod-offset]))
    return list(reversed(head+tail))



if __name__ =='__main__':
    nums = [8,9,10,11]
    print(move(nums,1))
    print(move2(nums,1))
    
    print(move(nums,-1))
    print(move2(nums,-1))
    
    