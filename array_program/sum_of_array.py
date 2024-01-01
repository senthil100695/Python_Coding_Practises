def sum_array(n):
    if len(n)==0:
        return 0
    else:
        sum = 0
        for i in n:
            sum +=i
        return sum

if __name__=='__main__':
    n = int(input('enter n element in array'))
    list1 = []
    for i in range(n):
        list1.append(int(input('enter the list values')))
    result = sum_array(list1)
    print(f'The sum of given array {list1} is = {result}'.format(list1,result)) 
