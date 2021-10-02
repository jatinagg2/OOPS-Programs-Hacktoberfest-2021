from sys import stdin

def rotate(arr,a,n,d):
    i=0
    while i<n-d:
        a.append(arr[i+d])
        i+=1
    for j in range(d):
        a.append(arr[j])
        
#Taking Input Using Fats I/O
def takeInput() :
    n = int(stdin.readline().rstrip())
    if n == 0:
        return list(), 0

    arr = list(map(int, stdin.readline().rstrip().split(" ")))
    return arr, n


#to print the array/list 
def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().rstrip())

while t > 0 :
    
    arr, n = takeInput()
    d = int(stdin.readline().rstrip())
    a=[]
    rotate(arr,a, n, d)
    printList(a, n)
    
    t -= 1
