capacity = 9



saffron_value = 5000
vanilla_value = 200
cinnamon_value = 10

saffron_weights = 4
vanilla_weights = 3
cinnamon_weights = 5 

class max_Loot:
    def __init__(self,value,weight):
        self.weight = weight
        self.value = value
        self.ratio = value / weight 


item_saffron = max_Loot(saffron_value,saffron_weights)
item_vanilla = max_Loot(vanilla_value,vanilla_weights)
item_cinnamon = max_Loot(cinnamon_value,cinnamon_weights)



items = [max_Loot(saffron_value,saffron_weights),
         max_Loot(vanilla_value,vanilla_weights),
         max_Loot(cinnamon_value,cinnamon_weights)] 


def Maximum_Loot(items,capacity):
    items.sort(key=lambda x:x.ratio,reverse=True)
    max_value = 0.0
    for item in items:
        if capacity>item.weight:
            capacity-=item.weight
            max_value+=item.value
        else:
            max_value+=capacity*item.ratio
            capacity-=item.weight
            print(f"max_value:{max_value},{capacity}")
    return max_value


# print(Maximum_Loot(items,capacity))





from sys import stdin



def maximum_loot(weights, values, capacity):
    items = [(weights[i], values[i], values[i] / weights[i]) for i in range(len(weights))]
    items.sort(key=lambda x: x[2], reverse=True)

    value = 0

    for wei, val, rat in items:
        if capacity >= wei: 
            value += val
            capacity -= wei
        else:
            value += capacity * rat
            break  # Stop because capacity is full

    return value



if __name__ == "__main__":
    data = list(map(int,input().split()))
    capacity = 9
    values = data[::2]
    weights = data[1::2]
    opt_value = maximum_loot(capacity, weights, values)
    print("{:.10f}".format(opt_value))


