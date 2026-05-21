def loan_repayment(principal, annual_rate, months):
  if not isinstance(principal,(int,float)) or principal<=0:
    raise ValueError("Invalid input: principal must be a number")
  if not isinstance(annual_rate,(int,float)) or annual_rate<0:
    raise ValueError("Invalid input: annual rate must be a number")
  if not isinstance(months,int) or months<=0:
    raise ValueError("Invalid input: months must be a whole number")
  if annual_rate==0:
    monthly = round(principal / months, 2)
    return {"monthly_payment": monthly, "total_paid": principal, "total_interest": 0.0}
  r=(annual_rate/100)/12
  a=(1+r)**months
  M=principal*(r*a)/(a-1)
  total_paid = round(M * months, 2)
  total_interest = round(total_paid - principal, 2)
  return {"monthly_payment": round(M, 2), "total_paid": total_paid, "total_interest": total_interest}
