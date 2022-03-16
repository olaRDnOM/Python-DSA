if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr.sort()
    for i in range(n, 0, -1):
        if arr[i-1] != arr[n-1]:
            print(arr[i-1])
            break