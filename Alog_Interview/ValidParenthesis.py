class solution:
    def isValid(self,s:str)-> bool:

        close_to_open = {

            '}':'{',
            ']':'[',
            ')':'('
        }

        stack = []

        for bracket in s:
            if bracket in close_to_open:
                #Closing Bracket
                if not stack:
                    return False
                top = stack.pop()
                if close_to_open[bracket] != top:
                    return False

            else:
                #opening bracket
                stack.append(bracket)
        if stack:
            return False
        else:
            return True

T = solution()
s = '{}]'
print(T.isValid(s=s))