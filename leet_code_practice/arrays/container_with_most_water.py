height = [1,8,6,2,5,4,8,3,7]

def wh(height):
    l,r=0,len(height)-1
    cap=0
    while l<r:
        area = (r-l)*min(height[l],height[r])
        cap = max(cap,area)
        if height[l]<height[r]:
            l+=1
        else:
            r-=1
    return cap

print(wh(height))