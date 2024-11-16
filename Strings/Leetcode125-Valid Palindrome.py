'''

Comparison of the Approaches

Approach	            | Time Complexity	|  Explanation Efficiency
------------------------|-------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Two Pointer Method	    | O(n)	            |  Iterates through the string twice (once to clean and once to compare) with two pointers moving toward each other. Good for simple use cases but involves explicit indexing.
String Slicing Method	| O(n)	            |  Uses slicing for reversing the string and compares it with the original string. Efficient but requires creating a reversed string. Better for readability and simplicity.
Regex Method	        | O(n)	            |  Uses regex substitution to remove non-alphanumeric characters and then compares the cleaned string with its reverse.	Best for performance, especially with larger strings, due to built-in optimizations.

'''

import re

class Solution:
    def isPalindrome(self, s: str) -> bool:

# *******************************************************************************************************************************************************************

    # Two pointer method O(n)
        # s = ''.join(char for char in s if char.isalnum()).lower()
        # print(s)
        # i, j = 0, len(s)-1
        # while(i<=j):
        #     if s[i]!=s[j]:
        #         return False
        #     i+=1
        #     j-=1
        # return True

# *******************************************************************************************************************************************************************

    # Better time complexity - Utilizing Python's built in optimizations for String slicing, which is faster than string indexing
        # s = ''.join(char for char in s if char.isalnum()).lower()
        # return (s==s[::-1])

# *******************************************************************************************************************************************************************

    # Best time complexity - Regex implements the same faster, working with the string in bulk for string substitutions, without iterating through individual characters
        s = re.sub(r'[^a-zA-Z0-9]','',s).lower()
        return (s==s[::-1])

# *******************************************************************************************************************************************************************