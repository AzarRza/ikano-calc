def loan_repayment(principal, annual_rate, months):
  if not isinstance(principal,(int,float)) or principal<=0:
    raise ValueError("Invalid input: principal must be a number")
  if not isinstance(annual_rate,(int,float)) or annual_rate<0:
    raise ValueError("Invalid input: annual rate must be a number")
  if not isinstance(months,int) or months<=0:
    raise ValueError("Invalid input: months must be a whole number")
  if annual_rate==0:
    monthly = round(principal / months, 2)
    schedule = []
    balance = principal
    for i in range(1, months+1):
      balance = round(balance - monthly, 2)
      schedule.append({"month": i, "payment": monthly, "principal": monthly, "interest": 0.0, "balance": balance})
    return {"monthly_payment": monthly, "total_paid": principal, "total_interest": 0.0, "schedule": schedule}
  r=(annual_rate/100)/12
  a=(1+r)**months
  M=round(principal*(r*a)/(a-1), 2)
  total_paid = round(M * months, 2)
  total_interest = round(total_paid - principal, 2)
  schedule = []
  balance = principal
  for i in range(1, months+1):
    interest = round(balance * r, 2)
    principal_paid = round(M - interest, 2)
    balance = round(balance - principal_paid, 2)
    schedule.append({"month": i, "payment": M, "principal": principal_paid, "interest": interest, "balance": balance})
  return {"monthly_payment": M, "total_paid": total_paid, "total_interest": total_interest, "schedule": schedule}