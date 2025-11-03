def primitive_calculator(n):
    dp = [0]*(n+1)
    prev = [0]*(n+1)
    for i in range(1,n+1):
        dp[i] = dp[i-1]+1
        prev[i] = i-1

        if i%2 == 0 and dp[i//2]+1<dp[i]:
            dp[i] = dp[i//2]+1
            prev[i]=i//2
        
        if i%3 == 0 and dp[i//3]+1<dp[i]:
            dp[i] = dp[i//3]+1
            prev[i]=i//3

    sequence = []
    while n<0:
        n=prev[n]
        sequence.append(n)
    sequence.reverse()
    return sequence

n =5
print(primitive_calculator(n))