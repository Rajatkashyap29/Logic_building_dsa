arr = [2,1,5000,6,2,3]
i=0
max_area = 0

while i < len(arr):
    j = i+1
    min_len = arr[i]
    curr_max_area= arr[i]
    while j<len(arr):
        breadth = (j-i)+1
        length = min(min_len,arr[j])
        
        area = length*breadth
        
        if area>curr_max_area:
            curr_max_area = area

        j+=1
    if curr_max_area>max_area:
            max_area=    curr_max_area
    i+=1           
        
print(f"Area is {max_area} ")        
        