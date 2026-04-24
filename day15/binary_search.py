arr=[10,20,30,40,50,60]
key = int(input("Please enter An elemet to search -->"))
st = 0
end = len(arr)-1
flag = False
while(st<=end):
    mid = (st + end)//2
    if arr[mid] == key :
        flag  = True
        break
    elif arr[mid] < key :
        st = mid+1
    else :
        end = mid-1     

if flag ==  True :
    print ("Element Found at index ->",mid)
else:
    print("Please enter a valid element ")    