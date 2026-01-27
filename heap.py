#Find the kth largest number in a list using Heap

import heapq


def nth_largest(nums,n):
    uniquelist=set(nums)
    if len(nums) < n:
        return None

    # nlargest(n, iterable) returns a list with the n largest elements
    # The result is sorted in descending order [largest, second_largest]
    largest_two = heapq.nlargest(n, uniquelist)

    return largest_two[n-1]


# Test
numbers = [10, 20, 4, 45, 99, 99, 21]
result = nth_largest(numbers,5)
print(f"The second largest number is: {result}")