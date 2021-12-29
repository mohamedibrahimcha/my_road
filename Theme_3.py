"""
A2
-----------------------------------------------------------------------------------------
1) since each postion in a dynamic array is known as well as the size and because of that the last position should be 
size-1 

2)

"""

"""
A3
----------------------------------------------------------------------------------------- 
    
"""
#complex implementation 
def findsim_complex(): 
    list =[]
    simlarity = 0
    for i1 in list: # 0(n)
        for i2 in list : # 0(n) 
            if list[i1] == list[i2]: 
                simlarity += 1 
            # assymptotic complexity of 0(n^2) 

#better implementation
def findsim(): 
    list =[]
    simlarity = 0
    list = list.sort()
    for i in range(len(list)-1): # 0(n)
        if list[i] == list[i+1]:
            simlarity += 1
            # assymptotic complexity of 0(n) 
 
"""
A4
----------------------------------------------------------------------------------------- 
1) linear search with O(n)
2) Binary search with O(n^2)
3) ammortized complexth of O(1)
4) O(n) as a worst case complexity if the element is placed in the first position 
"""

"""
A5
-----------------------------------------------------------------------------------------  
"""
def print_sorted(list1,list2):
    l1 = 0
    l2 = 0
    while l1<len(list1)-1 and l2<len(list2)-1  : 
        if list1[l1] < list2[l2]: 
            print(list1[l1])
            l1 += 1 
            
        elif list1[l1] > list2[l2]:  
            print(list2[l2])
            l2 += 1
            
        else:
            print(list1[l1])
            print(list2[l2])
            l1 += 1
            l2 += 1 
    if l1==len(list1)-1: 
        for i in range(len(list2[l2:])-1): 
            print (list2[i])
    if l2==len(list2)-1: 
        print(list1[l1:])

#sorted list test 
list1, list2 = [1,3,5,7,9,11,15,16],[2,4,6,8,10]
print_sorted(list1,list2)