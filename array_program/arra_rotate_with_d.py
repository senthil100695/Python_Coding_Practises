def array_rotate(array,n,d):
    temp = []
    i = 0
    while i<d:
        temp.append(array[i])
        i+=1
    i=0
    while d<n:
        array[i] = array[d]
        d+=1
        i+=1

    #array[:] = arr[:i]+ temp
    return array

def arr_rotate(arr,n,d):
     arr[:] = arr[d:n] +arr[0:d]
     return arr


if __name__=='__main__':
        arr = [1,2,3,4,5,6,7,8,9]
        n = 9
        d=2
        print(arr)
        #result = array_rotate(arr,n,d)
        result = arr_rotate(arr,n,d)
        print(result)