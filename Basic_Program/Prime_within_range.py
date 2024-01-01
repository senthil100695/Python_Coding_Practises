"""
Print all the Prime Number between the range

"""

def is_prime(n):
    count = 0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        print(f'The Number {n} is prime number'.format(n))
        return 1
    
if __name__=='__main__':
    start = int(input(' Enter the Starting number'))
    end = int(input(' Enter the last number'))
    count = 0
    for i in range(start,end):
        out = is_prime(i)
        if out==1:
            count+=1
    print(f'Total Prime Number Between {start}  and  {end} is {count}'.format(start,end,count))

