""""
Check the given number is armstrong number

153 = 1**3 + 5**3 + 3**3

"""

def armstong(n):
    num = n
    result = 0
    for i in str(n):
        result += int(i)**3
    if result==n:
        print(f"The Given number {n} is Armstrong number".format(n))
    else:
        print(f"The Given number {n} is not a Armstrong number".format(n))

if __name__=='__main__':
    n = int(input('Enter the  number'))
    armstong(n)
