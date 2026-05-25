def linear_search(arr,target):
    
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1 

# Space complexity = O(1)
# Time complexity  = O(n) 
print(linear_search([2,7,3,9,1],9))   