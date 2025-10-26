def optimal_summands(n):
    summands = []
    k=1
    while n>2*k:
        summands.append(k)
        n-=k
        k+=1
    summands.append(n)
    return summands


if __name__ == '__main__':
    n = int(input())
    summands = optimal_summands(n)
    print(len(summands))
    print(*summands)
