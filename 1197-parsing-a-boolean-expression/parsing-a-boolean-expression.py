class Solution:
    def parseBoolExpr(self, exp: str) -> bool:
        n=len(exp)
        stack=[]
        def solve(val, op):
            if op=="!":
                if val[0]=="t":
                    return "f"
                else:
                    return "t"
            if op=="&":
                for ele in val:
                    if ele=="f":
                        return "f"
                return "t"

            if op=="|":
                for ele in val:
                    if ele=="t":
                        return "t"
                return "f"
            return "f"

        for i in range(n):
            if exp[i]==",": continue
            if exp[i]==")":
                val=[]
                while stack[-1]!="(":
                    val.append(stack.pop())
                stack.pop()
                op=stack.pop()
                stack.append(solve(val, op))
            else:
                stack.append(exp[i])
        if stack[-1]=="t": return True
        return False
