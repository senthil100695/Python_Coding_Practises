def linear_search(array,n,k):
    if n<=0:
        return None
    else:
        for i in range(n):
            if array[i] == k:
                return i
        
    return -1

if __name__=='__main__':
    array = [1,3,5,31,34,421,21,2]
    k = int(input(' enter the search number = '))
    result = linear_search(array=array, n=len(array),k=k)
    if result== None:
        print('array is empty')
    elif result==-1:
        print('The number is not in the  array')
    else:
        print( ' The given is at position number of ', result)
