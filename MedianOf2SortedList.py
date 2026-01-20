import math

#
#This method if of time complexity of  O((m+n) log(m+n) . We need to do optimized version of binary search to reduce the complexity
#
def median_of_sortedLists(num1:list[int],num2:list[int])->float:
    num3=num1+num2
    num3=sorted(num3)
    length=len(num3)

    if not length%2 ==0:
        return num3[math.ceil(length/2)-1]
    elif length%2==0:
        median=(num3[int(length/2)]+num3[int(length/2)-1])/2
        return median


# Logic to use Binary Search and partition both lists to find the right balance to append to form the sorted arrays. This is to optimize using.sorted function and still go ahead an dsort using binary search
# Logic : Use the minimum array as the base and starting list to optimize
# nums1 = [1, 3, | 8]
# nums2 = [7 | 9, 10, 11]
#
# max_left1 = 3
# min_right1 = 8
# max_left2 = 7
# min_right2 = 9
#partition1 = (left + right) // 2
#partition2 = (len1 + len2 + 1) // 2 - partition1

#partition1: The number of elements on the left side of nums1
#partition2: The number of elements on the left side of nums2
#len1: The length of nums1
#len2: The length of nums2

# if max_left1<=min_right2 and max_left2<=min_right1
#if max_left1 <= min_right2 and max_left2 <= min_right1
#= 3 <= 9 and 7 <= 8
#= true → array is correctly partitioned
#
def optimizedmedian_sorterlist(num1:list[int],num2:list[int])->float:
    len1=len(num1)
    len2=len(num2)
    if len(num2)<len(num1):
        optimizedmedian_sorterlist(num2,num1)

    left=0
    right=len1

    while left <= right:
        part1=(left+right) //2
        part2=(len1+len2 +1) //2 -part1

        max_left1=float('-inf') if part1==0 else  num1[part1-1]
        min_right1 = float('+inf') if part1 == len1 else  num1[part1]
        max_left2=float('-inf') if part2==0 else num2[part2-1]
        min_right2=float('+inf') if part2==len2 else num2[part2]


        if max_left1<=min_right2 and max_left2<=min_right1:
            if((len1+len2) %2 ==0):
                return (max(max_left1, max_left2) + min(min_right1, min_right2))/2
            else:
                return max(max_left1, max_left2)
        elif max_left1>min_right2:
            right=part1-1
        else:
            left=part1+1
    return None


list1=[1,2,3]
list2=[4,5,6]
print(median_of_sortedLists(list1,list2))
print(optimizedmedian_sorterlist(list1,list2))
