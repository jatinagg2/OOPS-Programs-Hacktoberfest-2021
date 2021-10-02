from sys import stdin 
def findDuplicate(arr,n):
    sum = 0
    for i in range(len(arr)):
        sum = sum + arr[i]
    l = len(arr)-2             ## n  - 2  elements ## 
    sum1 = int((l*(l+1))/2)
    
    missingnumber = sum - sum1
    return missingnumber


#Taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().rstrip())

    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#main
t = int(stdin.readline().rstrip()) 

while t > 0 :

    arr, n = takeInput()
    print(findDuplicate(arr, n))

    t -= 1
