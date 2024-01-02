def interpolation_search(array,low,high,x):
    if ((low<=high) and array[low]<=x and array[high]>=x):
        pos = low +((high-low)//(array[high]-array[low])*(x-array[low]))

        if array[pos] == x:
            return pos
        elif array[pos]>x:
            return interpolation_search(array=array,low=low, high=pos-1,x=x)
        elif array[pos]<x:
            return interpolation_search(array=array,low=pos+1,high=high,x=x)
        
    return -1

if __name__=='__main__':
    array = [10, 12, 13, 16, 18, 19, 20,
       21, 22, 23, 24, 33, 35, 42, 47]
    n = int(input('enter the search number '))

    result = interpolation_search(array=array,low=0,high=len(array)-1,x=n)

    if result==-1:
        print(' The number is not present')
    else:
        print(' The number is present in index of ',result)
        