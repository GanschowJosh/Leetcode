
def evalRPN(tokens) -> int:
  out = 0
  stack = [tokens[0]]
  for token in tokens[1:]:
    if token in ["+", "-", "*", "/"]:
      op1 = stack.pop()
      op2 = stack.pop()
      print(f"{op2} {token} {op1}")
      out = int(eval(str(op2)+str(token)+str(op1)))
      stack.append(out)
    else:
      stack.append(token)
  return out

print(evalRPN(["4","13","5","/","+"]))