A = [2,3,4]
B = [5,0,1]

def poly_multi(A,B):
    C = [0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        for j in range(len(B)):
            C[i+j] += A[i]*B[j]
    return C

print(poly_multi(A,B))