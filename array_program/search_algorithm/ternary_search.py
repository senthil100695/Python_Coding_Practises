"""
divide the array in three parts

mid1 = low +(hig-low)/3
mid2 = high -(high-low)/3
Three array [low,mid1] [mid1,mid2], [mid2,high]
"""

def ternary_search(array,low,high,key):
    if low<=high:
        mid1 = low+ (high-low)//3
        mid2 = high - (high-low)//3

        if array[mid1] == key:
            return mid1 
        if array[mid2]==key:
            return mid2
        
        if array[mid1]>key:
            return ternary_search(array=array,low=low,high=mid1-1,key=key)
        elif array[mid2]<key:
            return ternary_search(array=array, low=mid2+1,high=high,key=key)
        else:
            return ternary_search(array=array,low=mid1+1,high=mid2-1,key=key)
    return -1

if __name__=='__main__':
    array = [1,2,3,4,5,6,7,8,9,10,11,12,14,15,16,17,18,19]
    key = int(input(' enter the key numver'))
    result = ternary_search(array=array,low=0,high=len(array)-1,key=key)
    if result ==-1:
        print('The number is not present')
    else:
        print(' The number is present in index of = ', result)
