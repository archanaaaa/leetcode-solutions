class Solution:
    def sumOfSeries(self,n):

# RECURSION O(n)

        # def recurs(i,result):
            
        #     if i>n:
        #         return result
        #     result+=(i**3)
        #     return recurs(i+1,result)

        # return recurs(1,0)

# FOR LOOP O(n)
        
        # sum = 0
        # for i in range(1,n+1):
        #     sum+=i**3
        # return sum
        
# OPTIMAL SOLUTION O(1)
# Sum of cubes=(n(n+1)/2)^2

        return (((n*(n+1))//2)**2)
        