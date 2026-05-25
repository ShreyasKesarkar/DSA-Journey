def binary_search(arr,target):
    l = 0
    h = len(arr) -1
    
    while(l<=h):
        mid = (l+h)//2
        
        if arr[mid] == target:
            return mid
        elif(target>arr[mid]):
            l = mid + 1
        else:
            h = mid - 1
    return -1

#Time complexity = log(n)
print(binary_search([1,2,3,4,5],5))            
    