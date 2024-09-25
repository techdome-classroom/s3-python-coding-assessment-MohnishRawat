class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        mapping = {")": "(", "}": "{", "]": "["}
        for ch in s:
            if ch in '({[':
                stack.append(ch)
            elif ch in ')}]':
                if not stack:
                    return False

                top = stack.pop()
                
        pass
