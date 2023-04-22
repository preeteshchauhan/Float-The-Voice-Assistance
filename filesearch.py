import requests
from bs4 import BeautifulSoup

# Replace the URL with the product page of your choice
url = 'https://www.amazon.com/dp/B08P3S7P7R'

# Send a GET request to the product page and parse the HTML content
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# Find the add to cart form and extract the necessary data
form = soup.find('form', {'id': 'addToCart'})
data = {
    'session-id': soup.find('input', {'name': 'session-id'})['value'],
    'quantity': 1, # change this to the desired quantity
    'asin': soup.find('input', {'name': 'asin'})['value'],
    'submit.add-to-cart': soup.find('input', {'name': 'submit.add-to-cart'})['value']
}

# Send a POST request to the add to cart URL with the necessary data
response = requests.post('https://www.amazon.com/gp/add-to-cart/process/', data=data)

# Check if the item was successfully added to the cart
if 'Added to Cart' in response.text:
    print('Item successfully added to cart!')
else:
    print('Failed to add item to cart.')
