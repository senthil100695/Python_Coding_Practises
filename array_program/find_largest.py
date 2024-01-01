def find_largest(n):
    largest = 0
    for i in n:
        if i>=largest:
            largest = i
    
    return largest


if __name__=='__main__':
    n = int(input('enter n element in array'))
    list1 = []
    for i in range(n):
        list1.append(int(input('enter the list values ')))
    result = find_largest(list1)
    print(f'The largest element of given array {list1} is = {result}'.format(list1,result)) 
