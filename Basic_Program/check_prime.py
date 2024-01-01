'''
Check the given number is Prime or Not

'''
def is_prime(n):
    count = 0
    for i in range(2,n):
        if n%i==0:
            count+=1
    if count==0:
        print(f'The given number {n} is Prime '.format(n))
    else:
        print(f'The given number {n} is Not Prime '.format(n))

if __name__=='__main__':
    n = int(input('Enter the number'))
    is_prime(n)
    
