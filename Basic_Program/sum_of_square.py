def square_sum(n):
    if n==0:
        return 0
    sum = 0
    for i in range(1,n+1):
        sum += i**2
    return sum

if __name__=='__main__':
    n = int(input('enter the n th nmber'))
    res = square_sum(n)
    print(f'The sum of {n} square is {res}'.format(n,res))