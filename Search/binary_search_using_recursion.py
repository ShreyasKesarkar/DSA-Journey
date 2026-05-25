def binary_search_using_recursion(arr,target):
    return helper(arr,target,0,len(arr)-1)


def helper(arr,target,l,r):
    
    if l > r:
       return -1
    
    mid = (l+r)//2
    mid_element = arr[mid]
    
    if mid_element == target:
        return mid
    
    elif(target < mid_element):
        return helper(arr,target,l,mid - 1)
    
    else:
        return helper(arr,target,mid + 1,r)


#Time complexity = log(n)
#space complexity = log(n) Extra stack is use
print(binary_search_using_recursion([1,2,3,4,5,6],5))