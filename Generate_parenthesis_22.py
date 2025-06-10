'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
'''

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def dfs(o:int,c:int,s:str):
            if o == 0 and c == 0:
                res.append(s)
                return
            
            if o < c:
                dfs(o,c-1,s+')')
            if o > 0:
                dfs(o-1,c,s+'(')
            
            


        dfs(n,n,"")

        return res