'''3. Longest Substring Without Repeating Characters
Solved
Medium
Topics
conpanies icon
Companies
Hint
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.'''

def longestSubString( s: str) -> int:
    seen = set() #Using this set to spot repeating characters w/ 0(1) lookup
    max = 0
    res = ""
    l = 0

    #r is going to represent the current letter we are on. 
    #l on the other hand will represent the INDEX of the leftmost letter w/o a repeating character
    for i, r in enumerate(s):
        if r in seen:
            while r in seen:
                seen.remove(s[l])
                l += 1
        seen.add(r)
        if len(seen) > max:
            max = len(seen)
            res = s[l:i+1]

    return max

print(longestSubString("pwwkew"))