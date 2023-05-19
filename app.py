import streamlit as st
import requests
import config

# Set your API key and application ID
api_id = 'a6ecdfa9'
app_key = '2bc312f48448207959f8b0d99f6487a6'

# Take user input for multiple ingredients
ingredients = input('Enter ingredients (comma-separated): ')

# Split the input into a list of ingredients
query_list = [ingredient.strip() for ingredient in ingredients.split(',')]

# Join the ingredients with 'AND' for the API query
query = ' AND '.join(query_list)

# Make the API request
url = f'https://api.edamam.com/api/recipes/v2?type=public&q={query}&app_id={app_id}&app_key={api_key}'
response = requests.get(url)

# Process the response
if response.status_code == 200:
    data = response.json()
    hits = data['hits']
    
    # Extract recipe information from the response
    for hit in hits:
        recipe = hit['recipe']
        title = recipe['label']
        ingredients = recipe['ingredientLines']
        instructions = recipe['url']
        
        print('Title:', title)
        print('Ingredients:', ingredients)
        print('Instructions:', instructions)
        print('---')
else:
    print('Error:', response.status_code)
