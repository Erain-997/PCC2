A = [1, 2, 3, 4, 9, 6, 8, 9, 10]
def findMinAndMax(L):
    n = 0
    for i,value in enumerate(L):
        print(i, value)
    for n in range(len(A)):
        a = L[n]
        b = L[n - 1]
        if a < b:
            Min = a
        else:
            Max = a
        print(a,b)
    n = n + 1
    print('Min', Min, 'Max', Max)
    return Min, Max
findMinAndMax(A)
