from bs4 import BeautifulSoup
import requests
import pandas as pd


wiki_url = 'https://en.wikipedia.org/wiki/Demographics_of_India#:~:text=17.7-,Population,-distribution%20by%20states'

response = requests.get(wiki_url)
soup = BeautifulSoup(response.text, 'html.parser')
state_list = soup.find('Population distribution by states/union territories (2011)', class_='wikitable sortable')
df = pd.read_html(str(state_list))[0]

print(df)
df.to_csv('ic.csv', index=False)



df = pd.read_html('https://en.wikipedia.org/wiki/Demographics_of_India')
df.to_csv('ic.csv')