t=int(input())

for i in range(t):
    n=int(input())
    arr=[int(x) for x in input().split()]

    for j in range(n):
        for k in range(j+1,n):
            if(arr[j]==arr[k]):
                print("Repeted element is:"+str(arr[j]))
