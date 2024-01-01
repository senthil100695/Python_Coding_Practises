def rotate_array(arr):
    last = len(arr)-1
    for i in range(int(len(arr)/2)):
        arr[i],arr[last] = arr[last],arr[i]
        last -=1
    
    return arr

if __name__=='__main__':
    n = int(input('enter n element in array'))
    array = []
    for i in range(n):
        array.append(int(input('enter the list values : ')))
    print(f'The array before rotate = ',array) 
    result = rotate_array(array) 
    print(f'The array after rotate = ',result) 
