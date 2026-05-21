from calculations.fibonacci import fibonacci
from calculations.factorial import factorial
from calculations.loan import loan_repayment

def test_fibonacci():
    assert fibonacci(5) == 5
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    try:
        fibonacci(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("Should have raised ValueError")

def test_factorial():
    assert factorial(5) == 120
    assert factorial(0) == 1
    try:
        factorial(-3)
    except ValueError:
        pass
    else:
        raise AssertionError("Should have raised ValueError")

def test_loan_repayment():
    assert loan_repayment(100000, 6, 12)["monthly_payment"] == 8606.64
    assert loan_repayment(12000, 0, 12)["monthly_payment"] == 1000.0          
    try:
        loan_repayment(-1000, 6, 12)
    except ValueError:
        pass
    else:
        raise AssertionError("Should have raised ValueError")
