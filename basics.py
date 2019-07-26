import requests

webpage_response = requests.get ('http://nhl.com')

print(webpage_response.text)

  '''
  The above scrapes the HTML from NHL's website.
  '''
