from sys import stdin
def merge(arr1,arr2,arr):
    l1=len(arr1)
    l2=len(arr2)
    i=0 
    j=0
    k=0
    while i<l1 and j<l2:
        if arr1[i]<arr2[j]:
            arr[k]=arr1[i]
            i=i+1
            k=k+1
        else:
            arr[k]=arr2[j]
            j=j+1
            k=k+1
    if i<l1:
        while i<l1:
            arr[k]=arr1[i]
            i=i+1
            k=k+1
    if j<l2:
        while j<l2:
            arr[k]=arr2[j]
            j=j+1
            k=k+1
def mergeSort(arr):
    if len(arr)==0 or len(arr)==1:
        return
    mid=len(arr)//2
    arr1=arr[0:mid]
    arr2=arr[mid:]
    mergeSort(arr1)
    mergeSort(arr2)
    merge(arr1,arr2,arr)
pass
def triplet(arr,n,x):
    mergeSort(arr)
    i=0
    count=0
    while i<n-2:
        j=i+1
        k=n-1
        while j<k:
            z=arr[i]+arr[j]+arr[k]
            if z<x:
                j=j+1
            elif z>x:
                k=k-1
            else:
                b=j
                c=k
                c1=1
                c2=1
                while b<k and arr[b]==arr[b+1] :
                    c1=c1+1
                    b=b+1
                if c>b:
                    while c>b and arr[c]==arr[c-1]:
                        c2=c2+1
                        c=c-1
                    v=c1*c2
                elif c==b:
                    h=c1-1
                    v=0
                    for q in range(h):
                        v=v+h
                        h=h-1
                count+=v
                j=b+1
                k=c-1
        i=i+1
    return count
#taking input using fast I/O method
def takeInput() :
    n = int(stdin.readline().strip())
    if n == 0 :
        return list(), 0

    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n


def printList(arr, n) : 
    for i in range(n) :
        print(arr[i], end = " ")
    print()


#main
t = int(stdin.readline().strip())

while t > 0 :
    
    arr, n = takeInput()
    num = int(stdin.readline().strip())
    print(triplet(arr, n, num))

    t -= 1
