from fastapi import FastAPI
from calculations.fibonacci import fibonacci
from calculations.factorial import factorial
from calculations.loan import loan_repayment
app = FastAPI()
@app.get("/fibonacci")
def fibonacci_endpoint(n: int):
    return {"result": fibonacci(n)}
@app.get("/factorial")
def factorial_endpoint(n: int):
    return {"result": factorial(n)}
@app.get("/loan")
def loan_endpoint(principal: float, annual_rate: float, months: int):
    return {"result": loan_repayment(principal,annual_rate,months)}

