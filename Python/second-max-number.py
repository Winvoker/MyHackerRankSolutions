if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))

arr.sort(reverse=True)
x=max(arr)

while(max(arr)==x):
    arr.remove(max(arr))
print(max(arr))
