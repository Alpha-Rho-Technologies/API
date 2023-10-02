import requests

def get_csrf_token(session: requests.Session, url: str) -> str:
    """
    Retrieve the CSRF token from the provided URL.

    Args:
    - session (requests.Session): The active session to use for the request.
    - url (str): The URL from which to fetch the CSRF token.

    Returns:
    - str: The retrieved CSRF token.
    
    Raises:
    - HTTPError: If the GET request to the URL fails.
    """
    response = session.get(url)
    response.raise_for_status()
    return response.cookies.get('csrftoken')

def get_strategy_info(user_name: str, password: str, strategy: str) -> dict:
    """
    Log into alpharhotech.com and retrieve the specified investment strategy allocation.

    Args:
    - user_name (str): The username for login.
    - password (str): The password for login.
    - strategy (str): The specific strategy for which allocation details are to be fetched.

    Returns:
    - dict: A dictionary containing the JSON response with strategy information.

    Raises:
    - HTTPError: If the POST request for login fails.
    """
    login_url = f'https://www.alpharhotech.com/accounts/login/?next=/strategy_allocations/{strategy}/'
    
    with requests.Session() as session:
        try:
            csrf_token = get_csrf_token(session, login_url)
            login_payload = {
                'login': user_name,
                'password': password,
                'csrfmiddlewaretoken': csrf_token
            }
            response = session.post(login_url, data=login_payload, headers={'Referer': login_url})
            response.raise_for_status()
            return response.json()
        except requests.RequestException as e:
            print(f"An error occurred: {e}")
            return {}