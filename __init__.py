from API.utils import *

class ARTapi:

  def __init__(self,user_name: str, password: str) -> None:
    '''
    Log into alpharhotech.com
    '''

    self.login_payload = {
    'login': user_name,
    'password': password,
    }
  
  def sp(self, strategy: str, engine: str) -> dict:
    """
    Strategy Portfolio (sp): Retrive the current portfolio allocation of a given 
    investment strategy powered by Alpha Rho Technologies algorithims.

    Args:
    - strategy (str): The specific strategy for which allocation details are to be fetched.
    - engine (str): The engine powering the strategy, either 'NeuralQ' or 'NeuralS'.

    Returns:
    - dict: A dictionary containing the JSON response with strategy information.

    Raises:
    - ValueError: If the engine is not 'NeuralQ' or 'NeuralS'.
    - HTTPError: If the POST request for login fails.
    """
    if engine not in ['NeuralQ', 'NeuralS']:
        raise ValueError("Engine must be 'NeuralQ' or 'NeuralS'")

    url = f'https://www.alpharhotech.com/accounts/login/?next=/{engine}/{strategy}/sp/'

    data = request_data(url=url,login_payload=self.login_payload)
    return data
  
  def shpd(self, strategy: str, engine: str) -> dict:
    '''
    Strategy Historical Price Data (shpd)
    '''
    if engine not in ['NeuralQ', 'NeuralS']:
        raise ValueError("Engine must be 'NeuralQ' or 'NeuralS'")

    url = f'https://www.alpharhotech.com/accounts/login/?next=/{engine}/{strategy}/shpd/'

    data = request_data(url=url,login_payload=self.login_payload)
    return data
  
  def shp(self, strategy: str, engine: str) -> dict:
    '''
    Strategy Historical Portfolios (shp):
    '''
    if engine not in ['NeuralQ', 'NeuralS']:
        raise ValueError("Engine must be 'NeuralQ' or 'NeuralS'")

    url = f'https://www.alpharhotech.com/accounts/login/?next=/{engine}/{strategy}/shp/'

    data = request_data(url=url,login_payload=self.login_payload)
    return data


