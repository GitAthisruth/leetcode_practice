from itertools import permutations

def TSP(dist,start=0):
    n = len(dist)
    city = list(range(n))
    minimum_cost = float("inf")
    min_path = None

    for perm in permutations([c for c in city if c!=start]):
        path = [start]+list(perm)+[start]
        cost=0
        for i in range(len(path)-1):
            cost += dist[path[i]][path[i+1]]
        if cost<minimum_cost:
            minimum_cost=cost
            min_path = path[:]
    return minimum_cost,min_path

        

# dist_matrix = [
#     [0, 10, 15, 20],
#     [10, 0, 35, 25],
#     [15, 35, 0, 30],
#     [20, 25, 30, 0]
# ]

dist = [[0,10,15,25],
        [5,45,65,70],
        [20,35,50,80],
        [35,45,55,0]]

print(TSP(dist))













