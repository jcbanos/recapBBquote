import requests

def get_quote():
     url = "https://breaking-bad-quotes.herokuapp.com/v1/quotes"
     response = requests.get(url).json()
     quote_dict = response[0]
     return f'{quote_dict["quote"]} by {quote_dict["author"]}'