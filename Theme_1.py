# binary search on sorted list in ascending order  

from typing import Iterator, Text

'''
TASK 1 
---------------------------------------------------------------------------------------------------------------
'''

def binarySearch_ascending(item, array):
    lo = 0 
    hi = len(array)-1
    
    while lo <= hi :
        # modular divison with two to find the mid in int
        mid = (lo+hi)//2 
        if item < array[mid]:
            #item must be in the first halv of the array 
            hi=mid-1 
        elif item > array[mid]:
            #item must be in the second halv of the array 
            lo=mid+1   
        else:
            #we found the item
            print(f'found the item : {array[mid]}')
            return mid 

    
    return -1 # if item is not found

# Task1:binary search on sorted list in ascending order 
def binarySearch_descending(item, array):
    lo = 0 
    hi = len(array)-1
    
    while lo <= hi :
        # modular divison with two to find the mid in int
        mid = (lo+hi)//2 
        if item < array[mid]:
            #item must be in the first halv of the array 
            lo=mid+1 
        elif item > array[mid]:
            #item must be in the second halv of the array 
            hi=mid-1   
        else:
            #we found the item
            print(f'found the item : {array[mid]}')
            return mid 
   
    return -1 # if item is not found


#function that returns a reversed array 
def reverse_array(array): 
    '''reversed_array = [] 
    array_len=len(array) 
    for i in range(array_len) :
        x = -1
        reversed_array.append(array[x-i])
    return reversed_array
    '''


    return array[::-1]  #faster way of returning a reversed array or a list 



test_array= [1,3,4,6,7,9,10,12,13,15]
#x = reverse_array(test_array)    
#print(x)
#binarySearch_descending(7,x) 

'''
TASK 1 
---------------------------------------------------------------------------------------------------------------
'''
#binary search using a recursive version that uses a helper method: 

def binarySearch_recursive(array,item, lo, hi):

        
        while lo <= hi:
            mid = (hi + lo)//2 
            if item < array[mid]: 
                hi = mid - 1
            elif item > array[mid]: 
                lo = mid + 1 
            else: 
                print(f"we have found the item : {array[mid]}")
                return mid 

    


#binarySearch_recursive(test_array, 3,0,4)

'''
TASK 3  
---------------------------------------------------------------------------------------------------------------
'''
# function that finds the integer square root, ex. integer square of 105 is 10 
def int_squareRoot(sq_int):
    '''
    for i in range(sq_int): 
        if  (i*i <= sq_int) & (sq_int < ((i+1)*(i+1))): 
            print(i)
            return i 
        elif (i*i < sq_int) & (sq_int <= ((i+1)*(i+1))): 
            print(i+1)
            return i+1 
    '''

    for i in range(sq_int): 
        if  (i*i <= sq_int < ((i+1)*(i+1))): 
            print(i)
            return i 
        elif (i*i < sq_int <= ((i+1)*(i+1))): 
            print(i+1)
            return i+1

#int_squareRoot(64)                      #test int_squareRoot 


'''
TASK 4
---------------------------------------------------------------------------------------------------------------
'''

'''
def inplace_insertion_sort(array):
    index=0 
    
    for element in range(len(array[index:])):
        
            if array[index]>array[element]: 
                temp = array[element]
                array[element] = array[index]
                array[index] = temp 
                index+=1
    
    
    while(index < len(array)):
        index=0 
        for element in range(len(array)-1):
            if array[index] <= array[element]: 
                array.insert(index,array[element])
                index+=1
            
      
    print(f"our sorted array is:{array}")
    return array

inplace_insertion_sort([4,6,8,2,9,5,1]) 


# insertion sort with an output array 
def insertion_sort(unsorted_array):  
    sorted_array = [] 
    for element in unsorted_array:
        if len(sorted_array)==0 or sorted_array[-1] <= element: 
            sorted_array.append(element)  
        else: 
            for i in range(len(sorted_array)): 
                if sorted_array[i] >= element: 
                    sorted_array.insert(i,element)
                    break                    
    print(f"our sorted array is:{sorted_array}")
    return sorted_array 
insertion_sort([4,6,8,2,9,5,1])
'''
# not implemented yet
#-------------------------------------------


'''
TASK 5
---------------------------------------------------------------------------------------------------------------
'''


def minimum(array): 
    min_int = array[0]
    for element in array: 
        if min_int >= element: 
            min_int = element 

    print(f'the smallest element in the array is {min_int}')

    return min_int 

#minimum([4,6,8,2,9,5,1]) 

def insert(array,x):
    for i in range(len(array)): 
        if array[i]<=x<=array[i+1]: 
            array.insert(i,x)
            break
    print(f"our array with the iserted item {x} is:{array}")
    return array 

insert([1,2,3,4,5,6,8,9,10],7) 

def merge(array1,array2):
    i1 = 0
    i2 = 0
    merged_array=[]
    while(i1<len(array1) and i2 < len(array2)): 
        if i1 == len(array1)-1: 
            for i in range(i2,len(array2)): 
                merged_array.append(array2[i])
                i2+=1
            break

        elif i2 == len(array2)-1: 
            for i in range(i2,len(array1)): 
                merged_array.append(array1[i])
                i1+=1 
            break

        elif array1[i1] == array2[i2]: 
            merged_array.append(array1[i1])
            merged_array.append(array2[i2])
            i1+=1
            i2+=1
        elif array1[i1] < array2[i2]: 
            merged_array.append(array1[i1])
            i1+=1
        elif array2[i2] < array1[i1]: 
            merged_array.append(array2[i2])
            i2+=1
    print(f"our merged array is {merged_array}")
    return merged_array

    

merge([1,3,5,7,9,11,12,14,15,17],[2,4,6,8,10])

'''
Bonus exercises 
---------------------------------------------------------------------------------------------------------------
'''




















        



    




    




        




 

            