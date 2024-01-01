import math

def perfersquare(x):
    val = int(math.sqrt(x))
    return val* val == x

def check_fibonacci(n):
    return perfersquare(5*n*n + 4) or perfersquare(5*n*n - 4)

if __name__=='__main__':
    n = int(input('enter the number'))
    res = check_fibonacci(n)
    print(res)
    if res== True:
        print(f' The Number {n} is fibonacci number'.format(n))
    else:
        print(f' The Number {n} is not fibonacci number'.format(n))

