def sentinel_search(array,n,k):
    if n==0:
        return 0
    else:
        last = array[n-1]
        array[n-1] = k

        i = 0
        while array[i]!=k:
            i+=1
        
        array[n-1] = last
        if (i<n-1) or array[n-1] == k:
            return i
        else:
            return -1
        
if __name__=='__main__':
    array = [1,2,3,4,5,6,75,52,31,2432,3412,23]
    k = int(input(' ente the search key'))
    result = sentinel_search(array=array,n=len(array),k=k)
    if result==-1:
        print(' The number not in list')
    else:
        print('This number present in index of = ',result)
    print(5//2)
