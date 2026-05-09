# Python Calculator

A simple Python calculator with unit tests and Docker support.

**Roll Number:** 2025sl93065
**Lab:** DevOps SCM Lab – Sheet 1

## Project Structure

```
├── calculator.py        # Calculator functions (add, subtract, multiply, divide)
├── test_calculator.py   # Unit tests using pytest
├── Dockerfile           # Docker configuration
├── Jenkinsfile          # Jenkins CI/CD pipeline
└── README.md
```

## Usage

```bash
python3 calculator.py
```

Output:
```
add(10, 3)      = 13
subtract(10, 3) = 7
multiply(10, 3) = 30
divide(10, 3)   = 3.3333333333333335
```

## Running Tests

```bash
pip install pytest
pytest test_calculator.py -v
```

## Docker

Build and run:
```bash
docker build -t calculator .
docker run calculator
```
