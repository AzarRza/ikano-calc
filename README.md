# Ikano Calculation Service

A REST API that performs three calculations: Fibonacci sequence, Factorial, and Loan Repayment. Built with Python and FastAPI as part of the Ikano Graduate Developer Assignment.

## Requirements
- Python 3.12
- pip
- Docker (optional)

## Installation

Clone the repository:

git clone https://github.com/AzarRza/ikano-calc.git
cd ikano-calc

Install dependencies:

pip install -r requirements.txt

## Running the API

uvicorn main:app --reload

Open http://localhost:8000/docs to use the interactive interface.

## Running tests

pytest tests/

## API endpoints

GET /fibonacci?n=5
Returns the nth Fibonacci number.

GET /factorial?n=5
Returns n factorial.

GET /loan?principal=100000&annual_rate=6&months=12
Returns monthly loan repayment amount.

## Running with Docker

docker build -t ikano-calc .
docker run -p 8000:8000 ikano-calc

## Limitations
- Fibonacci and Factorial accept positive integers only
- Principal and months must be positive numbers
- Annual rate cannot be negative (zero is allowed for interest-free loans)
- No authentication or rate limiting implemented
## Assumptions
- Annual rate is provided as a percentage (e.g. 6 for 6%, not 0.06)
- Months must be a whole number, partial months are not supported
- Fibonacci sequence starts at position 0
- The loan calculator works with whatever numbers you give it, no currency conversion is done