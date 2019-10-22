import numpy as np

n = list(map(int,input().split()))
arr=[]
arr1=[]
for _ in range(n[0]):
    arr = np.array([np.zeros((n[1],n[1])) for _ in range(n[2])], int)
for _ in range(n[0]):
    arr1 = np.array([np.ones((n[1],n[1])) for _ in range(n[2])], int)


print(arr)
print(arr1)
