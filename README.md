# Alpha Rho Technologies LLC API Documentation

This repository contains Python utilities for interfacing with AlpharhoTech's various APIs. With these utilities, users can retrieve investment strategy allocations and more.

## Table of Contents

- [Introduction](#introduction)

- [Setup](#setup)

- [Available APIs](#available-apis)
    - [Strategy Portfolio](#strategy-portfolio)
    - [Strategy Historical Price Data](#strategy-historical-price-data)
    - [Strategy Historical Portfolios](#strategy-historical-portfolios)

- [Support](#support)

## Introduction

Alpha Rho Technologies LLC provides a suite of APIs designed for investors seeking detailed analytics and data on various investment strategies. This repository is aimed at simplifying and streamlining the process of accessing that data.

## Setup

1. **Prerequisites**:

    - Python 3.6 or higher.
    - `requests` module:
    ```bash
    pip install requests
    ```

2. **Clone the Repository**:

    ```bash
    git clone https://github.com/Alpha-Rho-Technologies/API
    ```

3. Navigate to the cloned directory:

    ```bash
    cd path_to_directory
    ```

4. Provide Credentials:
Replace "your_username" and "your_password" with your actual Alpha Rho Technologies account's username and password.
    ```python
    from API import ARTapi

    ART_API = ARTapi(user_name = your_username, password = your_password)
    ```

## Available APIs
**Only users with authorised credentials can access the API information.**
Authorization is given on a product basis. We currently have two algorithms powering our strategies: Neural Q and Neural S. When fetching a strategy information, reference must be made to the algorithm powering the strategy.

Link to notebook with code examples: [example.ipynb](notebooks/example.ipynb)

### Strategy Portfolio
Fetches the current investment strategy allocation a user is subscribed to from Alpha Rho Technologies. 

#### Example:
```python
from API import ARTapi

ART_API = ARTapi(user_name = your_username, password = your_password)

data = ART_API.sp(strategy = 'global_macro', engine = 'NeuralQ')
```
Portfolio data is returned in JSON format by our API and parsed to dictionary format in python.

### Strategy Historical Price Data
Retrieves the historical price data for the investment strategy that a user is subscribed to from Alpha Rho Technologies.

#### Example:
```python
from API import ARTapi

ART_API = ARTapi(user_name = your_username, password = your_password)

data = ART_API.shpd(strategy = 'global_macro', engine = 'NeuralQ')
```
Portfolio data is returned in JSON format by our API and parsed to dictionary format in python.

### Strategy Historical Portfolios:
Retrieves the historical portfolios for the investment strategy that a user is subscribed to from Alpha Rho Technologies.

#### Example:
```python
from API import ARTapi

ART_API = ARTapi(user_name = your_username, password = your_password)

data = ART_API.shp(strategy = 'global_macro', engine = 'NeuralQ')
```
Portfolio data is returned in JSON format by our API and parsed to dictionary format in python.

## Support
For any queries or issues related to the API utilities, please raise an issue in this repository or contact contact@alpharhotech.com.

