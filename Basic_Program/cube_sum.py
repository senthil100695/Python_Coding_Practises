def cube_sum(n):
    sum = 0
    i=1
    while i <=n:
        sum += i**3
        i+=1
    return sum

if __name__=='__main__':
    n = int(input(' ethe the n value'))
    res = cube_sum(n)
    print(f'The sum of cube of {n} value is {res}'.format(n,res))