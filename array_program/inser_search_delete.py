def search_element(array,n,key):
    if n<=0:
        return None
    for i in range(n):
        if array[i]== key:
            return i
    return -1

def insert_end(array,n,val):
    if n<=0:
        array[0] = val
    else:
        array.append(val)

def insert_pos(array,n, pos,val):
    for i in range(n-1,pos-1,-1):
        array[i+1] = array[i]
    
    array[pos] = val

def delete_array(array,val):
    array.remove(val)


if __name__=='__main__':
    array = [10, 50, 30, 40, 20]
    val = int(input(' enter the valye to insert att end : '))
    insert_end(array=array,n=len(array),val=val)

    print('The array is after insert ', array)

    val= int(input('enter the value to insert '))
    pos = int(input(' enter the pos to be insert '))

    insert_pos(array=array,n=len(array),pos=pos,val=val)

    print(' The after insert in particular postioj the array is ==', array)

    val = int(input('  ether the valu you will delete '))
    delete_array(array=array,val=val)

    print(' after deletion the array will be = ',array)

    val = int(input(' Eter the value to be search in array'))

    print(' The value is present in a array at index of  = ',search_element(array=array,n=len(array),key=val))

