"""
find a the Max number in two numbrs
"""

def max_num(a,b):
    if a>b:
        return a
    else:
        return b

if __name__=='__main__':
    a,b = input('enter the two number with space ').split()
    result = max_num(int(a),int(b))
    print(f" The max Number is {result}".format(result))
    
