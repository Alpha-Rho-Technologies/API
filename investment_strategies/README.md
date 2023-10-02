# Documentation for Requesting Investment Strategy Allocation

Easily fetch your subscribed investment strategy allocation from AlpharhoTech using a Python script.

## Overview

The provided Python script automates the login process to [Alpha Rho Technologies](https://www.alpharhotech.com) and fetches the specific investment strategy allocation for a user. The returned data is in a JSON format.

## **Prerequisites**

- **Python Environment**: Ensure you're running Python 3.6 or higher.
  
- **Dependencies**: Install the required Python module by running:
  ```bash
  pip install requests
  ```

## How to Fetch Strategy Allocation:
### Setup:

First, ensure you have the functions get_csrf_token and get_strategy_info correctly defined in your Python script or environment.

### Provide Credentials:

Replace "your_username" and "your_password" with your actual Alpha Rho Technologies account's username and password.

### Available Strategies:
```python
['us_equity_macro','global_macro','regional_equity_macro']
```

### Execute:
Run the function with the desired strategy name:

```python
data = get_strategy_info("your_username", "your_password", "strategy_name_here")

print(strategy_data)
```

### Review:
The output should be a dictionary with details about the specified strategy. If there's an error, the function will print an error message and return an empty dictionary.