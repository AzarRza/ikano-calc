def loan_repayment(principal, annual_rate, months):
  if not isinstance(principal,(int,float)) or principal<=0:
    raise ValueError("Invalid input: principal must be a number")
  if not isinstance(annual_rate,(int,float)) or annual_rate<0:
    raise ValueError("Invalid input: annual rate must be a number")
  if not isinstance(months,int) or months<=0:
    raise ValueError("Invalid input: months must be a whole number")
  if annual_rate==0:
    return round(principal/months,2)
  r=(annual_rate/100)/12
  a=(1+r)**months
  M=principal*(r*a)/(a-1)
  return round(M,2)