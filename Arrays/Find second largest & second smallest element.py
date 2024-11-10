'''
Problem statement

You have been given an array 'a' of 'n' unique non-negative integers. 
Find the second largest and second smallest element from the array.
Return the two elements (second largest and second smallest) as another array of size 2.

Example :

Input: n = 5, a = [1, 2, 3, 4, 5]
Output: [4, 2]

Expected Time Complexity:
O(n), Where 'n' is the size of an input array 'a'.

Constraints:

2 <= 'n' <= 10^5
0 <= 'a'[i] <= 10^9

Time limit: 1 sec

'''
def getSecondOrderElements(n: int,  a: [int]) -> [int]:

    # Brute force : O(nlogn + n)
    # Better Solution : O(2n)
    # Optimal Solution : O(n)
    
#*************************************************************************************************

    # Brute force : O(nlogn + n) -> Sort and find the second largest - O(nlogn + n)
    
    # ans = []
    # a.sort(reverse=True)
    # for num in a:
    #     if num != a[0]:
    #         ans.append(num)
    #         break

    # for num in a[::-1]:
    #     if num != a[-1]:
    #         ans.append(num)
    #         break
            
    # return ans       

# **************************************************************************************************

    # Better Solution : O(2n) -> One pass to find largest, one pass to find second largest -O(n+n) = O(2n)
    # ans = []

    # largest = float("-inf")
    # for num in a:
    #     if num>largest:
    #         largest=num
    
    # secondLargest = float("-inf")
    # for num in a:
    #     if num>secondLargest and num<largest:
    #         secondLargest=num
    
    # ans.append(secondLargest)

    # smallest = float("inf")
    # for num in a:
    #     if num<smallest:
    #         smallest=num
    
    # secondsmallest = float("inf")
    # for num in a:
    #     if num<secondsmallest and num>smallest:
    #         secondsmallest=num
    
    # ans.append(secondsmallest)

    # return ans

#***************************************************************************************************

    # Optimal Solution : O(n) -> Single pass, have two variables - larg, secondLar & make comparisons - O(n)

    ans = []
    larg, secondLarg = a[0], float("-inf")
    for num in a:
        if num>larg:
            secondLarg = larg
            larg=num
        if num>secondLarg and num<larg:
            secondLarg = num

    ans.append(secondLarg)

    small, secondsmall = a[0], float("inf")
    for num in a:
        if num<small:
            secondsmall = small
            small=num
        if num<secondsmall and num>small:
            secondsmall = num

    ans.append(secondsmall)

    return ans

#********************************************************************************************************

    

