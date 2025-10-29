# ls =[60,3,45,1,9,0]

def inv(ls):
    if len(ls)<=1:
        return ls,0
    
    mid = len(ls)//2
    l,in_l = inv(ls[:mid])
    r,in_r = inv(ls[mid:])
    merged,in_split = merge_count(l,r)

    return merged,in_l+in_r+in_split

def merge_count(l,r):
    i=j=count = 0
    merged = []
    while i<len(l) and j<len(r):
        if l[i]<=r[j]:
            merged.append(l[i])
            i+=1
        else:
            merged.append(r[j])
            j+=1
            count += len(l)-i

    merged+=l[i:]
    merged+=r[j:]
    return merged,count



if __name__ == '__main__':
    input_n = int(input())
    elements = list(map(int, input().split()))
    assert len(elements) == input_n
    val,count = inv(elements)
    print(count)

