"""
Factorial of a given number with resursive

"""

def fact_rec(n):
    if n==1:
        return 1
    else:
        return n * fact_rec(n-1)

if __name__=='__main__':
    n = int(input(' Enter the factorial of value ')) 
    result = fact_rec(n)
    print(f"The Factorial of {n} is {result} ".format(n,result))