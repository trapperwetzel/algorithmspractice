
'''
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
    Every close bracket has a corresponding open bracket of the same type.

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

'''

s = "([])"



def validParentheses(samplestring):
    
    dict1 = {'}':'{', ']':'[',')':'('}

    stack = [] 

    for i in samplestring:  
        
        if i in dict1.values():
            stack.append(i)
        elif stack and dict1[i] == stack[-1]:
            stack.pop()
        else:
            return False
    
    return True


result = validParentheses(s)

print(result)

        
