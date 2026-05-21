from fastapi import FastAPI, HTTPException, Query
from calculations.fibonacci import fibonacci
from calculations.factorial import factorial
from calculations.loan import loan_repayment
app = FastAPI()
@app.get("/health")
def health():
    return {"status": "ok"}
@app.get("/fibonacci")
def fibonacci_endpoint(n: int = Query(description="Position in the Fibonacci sequence, must be a positive whole number")):
    try:
        return {"result": fibonacci(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/factorial")
def factorial_endpoint(n: int = Query(description="The number to calculate factorial for, must be a positive whole number")):
    try:
        return {"result": factorial(n)}
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
@app.get("/loan")
def loan_endpoint(
    principal: float = Query(description="Loan amount, must be greater than zero"),
    annual_rate: float = Query(description="Annual interest rate as a percentage, e.g. 6 for 6%"),
    months: int = Query(description="Loan duration in whole months, must be greater than zero")
):
    try:
       return loan_repayment(principal, annual_rate, months)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))


