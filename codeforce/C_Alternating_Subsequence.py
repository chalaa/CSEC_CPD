t = int(input())
while t>0:
    n = int(input())
    arr = [int(i) for i in input().split()]
    i=0
    ans = 0
    while i<n:
        if arr[i]>0:
            j=i
            _max = arr[i]
            while j<n and arr[j]>0:
                _max = max(_max,arr[j])
                j+=1
            i = j
            ans += _max
        else:
            j=i
            _max = arr[i]
            while j<n and arr[j]<0:
                _max = max(_max,arr[j])
                j+=1
            i = j
            ans += _max
    print(ans)     
    t-=1