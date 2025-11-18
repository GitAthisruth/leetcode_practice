from sys import stdin


def min_refills(distance, tank, stops):
    stops.sort()
    stops = [0]+stops+[distance]
    current = 0
    next_refill = 0
    refills=0
    while current < len(stops)-1:#here  the while loops only moves n times. So time complexity is O(n). But we sue a sorthing algorith here so the time complexity is O(nlogn) asymtotically. 
        next_refill = current
        while (current < len(stops)-1) and (stops[current+1]-stops[next_refill] <=tank):
            current+=1

        if current == next_refill:
            return -1
        
        if current<len(stops)-1:
            refills+=1

    return refills

tank = 400
stop = [200, 375, 550, 750]
distance = 950 


# if __name__ == '__main__':
#     d, m, _, *stops = map(int, stdin.read().split())#ctrl+Z+Enter
#     print(min_refills(d, m, stops))

print(min_refills(distance,tank,stop))
