n=int(input())
m=list(map(int, input().split()))
a=int(input())
b=list(map(int, input().split()))

def binary_search(arr, val):
    first, last = 0, len(arr)-1
    while first<=last:
        mid=(first+last)//2
        if arr[mid]==val:
            return mid
        if arr[mid]>val:
            last=mid-1
        else:
            first=mid+1
    return -1