
def evaluate_expr(stack):
    if not stack or type(stack[-1]) == str:
        stack.append(0)

    last_operation = " "
    lastNum = stack.pop()
    res = lastNum
    while stack and stack[-1] != ")":
        operation = stack.pop()
        if operation == "+":
            last_operation = "+"
            lastNum = stack.pop()
            res += lastNum
        elif operation == "-":
            last_operation = "+"
            lastNum = -stack.pop()
            res += lastNum
        elif operation == "*":
            curr = int(stack.pop())
            if last_operation == "+":
                res = res - lastNum + lastNum * curr
            else:
                res = res * curr
            last_operation = " "
            lastNum = curr
        elif operation == "%":
            curr = int(stack.pop())
            if last_operation == "+":
                res = res - lastNum + lastNum / curr
            else:
                res /= curr
            last_operation = " "
            lastNum = curr

    return res


def calculator(s):
    stack = []
    n, operand = 0, 0

    for i in range(len(s) - 1, -1, -1):
        ch = s[i]
        if ch.isdigit():
            operand = (10**n * int(ch)) + operand
            n += 1

        elif ch != " ":
            if n:
                stack.append(operand)
                n, operand = 0, 0

            if ch == "(":
                res = evaluate_expr(stack)
                stack.pop()
                stack.append(res)
            else:
                stack.append(ch)

    if n:
        stack.append(operand)

    return evaluate_expr(stack)

