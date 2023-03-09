def linear_search(lst,target):
    for i in range(0,len(lst)):
        if lst[i]== target:
            return i
    return None

def prnt(index):
    if result is not None:
        print("result is found at Index: ",index)
    else:
        print("not found")

result=linear_search([1,2,3,4,5,6,7,8,9,10],3)
prnt(result)



####################################################
def binary_search(lst,target):
    first=0
    last=len(lst)-1 #zaradi index

    while first<=last:
        midpoint=(first+last)//2
        if lst[midpoint]==target:
            return midpoint
        elif lst[midpoint]<target:
            first=midpoint+1
        else:
            last=midpoint-1


def prnt(index):
    if result is not None:
        print("result is found at Index: ",index)
    else:
        print("not found")

result=binary_search([1,2,3,4,5,6,7,8,9,10],4)
prnt(result)

#########################################################################3

def recursive_binary(list,target):
    midpoint=len(list)//2
    if len(list)==0:
        return False
    else:
        if list[midpoint]==target:
            return True
        elif list[midpoint]<target:
            return recursive_binary(list[midpoint+1:],target)
        else:
            return recursive_binary(list[:midpoint],target)

result=recursive_binary([i for i in range(0,10)],11)
def prnt(index):
    print("Result found: ",index)
prnt(result)
