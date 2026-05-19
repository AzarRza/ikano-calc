def factorial(n):
  if not isinstance(n,int):
    raise ValueError("Invalid input: n must be a whole number, not a decimal")
  if n<0:
    raise ValueError("Invalid input: n must be a positive whole number")
  if n==0:
    return 1
  result=1
  for i in range(1,n+1):
    result=result*i
  return result