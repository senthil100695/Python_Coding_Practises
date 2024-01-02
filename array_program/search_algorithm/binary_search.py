def binary_search(array,low,high,key):
    while low <=high:
        mid = low+ (high-low)//2

        if array[mid]== key:
            return mid
        elif array[mid]<key:
            low = mid+1
        elif array[mid]>key:
            high= mid-1
    return -1

def binary_search_resursive(array,low,high,key):
    if high>=low:
        mid = low + (high-low)//2
        if array[mid]==key:
            return mid

        if array[mid]<key:
            return binary_search_resursive(array=array,low=mid+1,high=high,key=key)
        elif array[mid]>key:
            return binary_search_resursive(array=array,low=low,high=mid-1,key=key)
    else:
            return -1

        



if __name__=='__main__':
    array = [1,2,3,4,5,6,7,8,9,10]
    key = int(input(' enter the search number ' ))
    result = binary_search_resursive(array=sorted(array), low=0,high=len(array)-1,key=key)
    if result ==-1:
        print('The number not present in array')
    else:
        print('The number present in index of = ',result)
