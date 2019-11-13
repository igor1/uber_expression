def is_int(e):
    try:
        int(e)
        return True
    except:
        return False

def is_op(e):
    return e in "+-"
    
def compute(op1, op, op2):
    if op == '+':
        return int(op1) + int(op2)
    elif op == '-':
        return int(op1) - int(op2)
    else:
        assert False, "Unknown operator: {op}"

def stack_compute(stack, op2):
    assert is_op(stack[-1]), f"Bad input - not an op: {stack[-1]}, stack: {stack}, e: {e}"
    assert is_int(stack[-2]), f"Bad input - not an int: {stack[-2]}"
    op1 = stack[-2]
    op = stack[-1]
    val = compute(op1, op, op2)
    stack = stack[:-2]
    stack.append(val)

def calculate(expr):
    stack = []
    for e in expr:
        if e in " \t":
            continue
        if is_int(e):
            if not stack or stack[-1] == '(':
                stack.append(int(e))
            else:
                stack_compute(stack, int(e))
#                assert is_op(stack[-1]), f"Bad input - not an op: {stack[-1]}, stack: {stack}, e: {e}"
#                assert is_int(stack[-2]), f"Bad input - not an int: {stack[-2]}"
#                op1 = stack[-2]
#                op2 = int(e)
#                op = stack[-1]
#                val = compute(op1, op, op2)
#                stack = stack[:-2]
#                stack.append(val)
        elif is_op(e):
            stack.append(e)
        elif e == "(":
            stack.append(e)
        elif e == ")":
            val = stack[-1]
            assert is_int(val), f"Bad input - not an in {val}, stack: {stack}, e: {e}"
            assert stack[-2] == "(", f"Bad input - expected (, got {stack[-2]}"
            stack = stack[:-2]
            if stack:
                stack_compute(stack, val)
            else:
                stack.append(val)
        else:
            assert False, "Bad input"
            
    assert len(stack) == 1, f"Weird stuff left in stack: {stack}"
    return stack[0]
            
            
if __name__ == "__main__":
    result = calculate("1 + (2 + 3)")
    print(f"result: {result}")
    
    
