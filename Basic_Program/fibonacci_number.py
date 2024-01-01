def fibnocacci(n):
    a, b = 0,1
    if n==1:
        print(1)
    else:
        for i in range(n):
            print(a, end=' ')
            c = a+b
            a = b
            b = c

if __name__ == '__main__':
    n = int(input('enter the n fibonacci number'))
    fibnocacci(n)