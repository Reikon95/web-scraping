import requests

webpage_response = requests.get ('http://nhl.com')

print(webpage_response.text)

  '''
  The above scrapes the src from NHL's website.
  '''

webpage = webpage_response.content

print(webpage)
  '''
  This builds on the above, delivering the content from the page
  '''
from bs4 import BeautifulSoup
soup = BeautifulSoup(webpage, "html.parser")

print(soup)
