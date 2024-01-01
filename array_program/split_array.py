def split_array(array,k):
    array[:] = array[k:len(array)]+ array[0:k] 
    return array

if __name__=='__main__':
    arr = [1,2,3,4,5,5,6,7,6]
    k = int(input(' enter the k Value '))
    print(arr)
    result = split_array(arr,k)
    print(result)