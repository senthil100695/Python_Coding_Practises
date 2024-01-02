import math
def jump_search(array,key,n):
    step = math.sqrt(n)

    prev = 0
    while array[int(min(step,n)-1)]<key:
        prev = step
        step += math.sqrt(n)
        if  prev >=n:
            return -1
        
    while array[int(prev)] < key:
        prev +=1

        if prev == min(step,n):
            return -1
        
    if array[int(prev)]==key:
        return prev

    return -1

if __name__=='__main__':
    array = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
    34, 55, 89, 144, 233, 377, 610 ,712]

    n = int(input(' enter the value you search '))

    result = jump_search(array=array,key=n,n=len(array))
    if result==-1:
        print(' The number is not present in arrary')
    else:
        print(' The number is present in index of value = ', int(result))
