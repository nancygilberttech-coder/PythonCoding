# Rotate an array for K times
#Option 1: Brute force Use pop() and insert()
#Option 2: More Optimized way is to reverse the complete list and then reverse it , call it again again ti indivudually reverese the first half and the second ha;f

def reverseList_bruteforce(nums:list, k:int):
    n = len(nums)
    # Optimize k to be within the bounds of array length
    k = k % n

    for _ in range(k):
        last_element = nums.pop()
        nums.insert(0, last_element)
    return nums


def reverseList_optimized(nums:list, k:int):
    n=len(nums)
    k=k%n # optimize the number of iterations we want to do

    def reverseList(arr,startindex, endindex):
        while startindex<endindex:
            #temp=arr[startindex]
            #arr[startindex]=arr[endindex]
            #arr[endindex]=temp
            arr[startindex],arr[endindex]=arr[endindex],arr[startindex]
            startindex+=1
            endindex-=1

    reverseList(nums,0,n-1)
    reverseList(nums,0,k-1)
    reverseList(nums,k,n-1)
    return nums


# Example usage
arr = [1, 2, 3, 4, 5]
k_rotations = 2
rotated_arr = reverseList_bruteforce(arr, k_rotations)
rotated_arr_optimized=reverseList_optimized(arr,k_rotations)
print(f"Rotated array: {rotated_arr}")
print(f"Rotated array: {rotated_arr_optimized}")