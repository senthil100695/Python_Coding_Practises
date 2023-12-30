"""
create a function for calculate simple interest 

simple interest = pnr/100

"""

def simple_interest(p,n,r):
    return (p*n*r)/100

if __name__=='__main__':
    P = int(input(' Enter the Principal Amount'))
    N = int(input(' Enter the Total Year'))
    R = int(input(' Enter the Interest'))

    result = simple_interest(P,N,R)
    print(f" The Principal {P} with {R} percentage interest for {N} year is {result}".format(P,N,R,result))
    print(f"The Total Amount is {P+result}")


