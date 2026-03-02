hh= [2,7,11,15] 

def nn(hh,target=9):
    dd = {}
    for index,val in enumerate(hh):
        rm = target - val
        if rm in dd:
            return [dd[rm],index]
        else:
            dd[val] = index

print(nn(hh,target=9))