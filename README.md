# Fakestore API Testing Script

This Python script performs automated testing of the [Fakestore API](https://fakestoreapi.com/products) to validate product data according to specific business rules.

## Test Objectives

The script validates the following:
1. HTTP status code of the GET response (must be 200 OK)
2. For each product object in the returned array, validates:
   - Title (product name) must be a non-empty string
   - Price must be a non-negative number
   - Rating must be less than or equal to 5

## Setup

1. Clone the repository:
```bash
git clone https://github.com/YOUR_USERNAME/pythonTestCursorAI.git
cd pythonTestCursorAI
```

2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Usage

Run the script:
```bash
python api_test.py
```

## Output

The script will print:
- Success messages for passed validations (✅)
- Error messages for any validation failures (❌)
- Detailed information about any defects found in the product data

## Error Types

The script identifies the following types of defects:
- Empty or invalid title
- Negative or invalid price
- Rating exceeds maximum value of 5 
