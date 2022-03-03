import requests
from bs4 import BeautifulSoup

html_text = requests.get('https://www.delish.com/cooking/recipe-ideas/recipes/a55742/pumpkin-spice-chocolate-chip-cookies-recipe/').text
soup = BeautifulSoup(html_text, 'lxml')
ingredients = soup.find_all('div', class_='ingredient-item')
for ingredient in ingredients:
    ingredient_number = ingredient.find('span', class_='ingredient-amount').text
    ingredient_name = ingredient.find('span', class_='ingredient-description').text
    print(ingredient_number.split(), ingredient_name)
    print("")

