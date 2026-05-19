def fibonacci(n):
  if not isinstance(n,int):
    raise ValueError("Invalid input: n must be a whole number, not a decimal")
  if n<0:
    raise ValueError("Invalid input: n must be a positive whole number")
  if n==0:
    return 0
  if n==1:
    return 1
  a = 0
  b = 1
  for i in range(n-1):
    c = a + b
    a = b
    b = c
  return b