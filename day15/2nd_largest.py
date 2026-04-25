# arr=[13,27,23,44,56,124,51,76,32,70,99,11]
# i=0
# first_largest_elt = 0
# while(i<len(arr)):
#    if arr[i]>first_largest_elt:
#        first_largest_elt = arr[i]
#    i+=1  
   
# second_largest_element = 0
# i=0
# while(i<len(arr)):
#     if arr[i]>second_largest_element and arr[i] != first_largest_elt :
#         second_largest_element = arr[i]
#     i+=1
    

# print(second_largest_element)           


#------------------------ Optimized code  ------------------------- 

arr=[13,27,23,44,56,124,51,76,32,70,99,11]
i=0
first_largest_elt = 0
second_largest_element = 0

while i < len(arr):
    if arr[i] > first_largest_elt :
        second_largest_element = first_largest_elt
        first_largest_elt = arr[i]
    elif arr[i] > second_largest_element and arr[i] != first_largest_elt :
        second_largest_element = arr[i]
            
    i+=1



print(first_largest_elt)
print(second_largest_element)    