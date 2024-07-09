from bs4 import BeautifulSoup as bs
import requests
import json
import re

# best-sellers url
#website = 'https://www.cremedelamer.com/bestsellers/best-skincare'

# all face products url
website = 'https://www.cremedelamer.com/face/skincare-makeup-for-face'
response = requests.get(website)
soup = bs(response.content, 'html.parser')

results = soup.find("div", class_="product-grid-wrapper")


product_names = results.find_all("div", class_="product-name")


prices = results.find_all("div", class_="product-price")

relevant_classes = [
    'product-image product-image--med product-image--default js-product-image--default product-image--has-hover',
    'product-image product-image--med product-image--default js-product-image--default'   
]

images = results.find_all('img', class_=lambda x: x in relevant_classes)

data = []

for product_name, price, image in zip(product_names, prices, images):
    
    price_transformation = price.get_text().strip()
    match = re.search(r'\$\d+', price_transformation)
    if match:
        price_transformation = match.group(0)    
    
    items = {
        "product_name": product_name.get_text().strip(),
        "price": price_transformation,
        "image": "https://www.cremedelamer.com" + image.get('src', '') 
        }
    data.append(items)
    
    with open('lamer_face_products.json', 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=4)