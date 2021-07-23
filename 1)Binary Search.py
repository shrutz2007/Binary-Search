def BinarySearch(list1,key):
    start=0
    end=len(list1)-1
    while start<=end:
        mid=start+(end-start)//2
        mid_val=list1[mid]
        if mid_val==key:
            return mid
        elif key<mid_val:
            end=mid-1
        else:
            start=mid+1
    return None
list1=list(map(int,input().split( )))
list1.sort()
key=int(input("Enter the key value : "))
print(BinarySearch(list1,key))