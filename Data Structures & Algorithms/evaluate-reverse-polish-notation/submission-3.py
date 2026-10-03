class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num = 0
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(n2 - n1)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                n1 = stack.pop()
                n2 = stack.pop()
                stack.append(int(n2/n1))
            else:
                stack.append(int(c))
        return stack.pop()