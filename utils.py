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

def request_data(url:str,login_payload):
  with requests.Session() as session:
    try:
      # Get token:
      csrf_token = get_csrf_token(session, url)
      payload = login_payload.copy()
      payload['csrfmiddlewaretoken'] = csrf_token

      # Get Response:
      response = session.post(url, data = payload, headers={'Referer': url})
      status = response.raise_for_status()
      return response.json()
    
    except requests.RequestException as e:
      print(e)