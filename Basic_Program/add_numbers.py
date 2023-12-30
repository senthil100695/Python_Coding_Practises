"""
Create a function for add two numbers with one single input

"""

def add_num(a,b):
    return a+b

if __name__=='__main__':
    a,b = input('enter the 2 number with spaces').split(' ')
    result = add_num(int(a),int(b))
    print(f"the summ of {a} + {b} is eqal {result}".format(a,b,result))


