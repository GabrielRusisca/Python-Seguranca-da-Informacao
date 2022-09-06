from bs4 import BeautifulSoup
import requests

site = requests.get('https://www.climatempo.com.br/').content # site recebendo o conteudo da requisição do site ...

soup = BeautifulSoup(site,'html.parser') # baixando do site o html

print(soup.prettify()) # transforma o html em string e o print vai exibir o html

temperatura = soup.find('span', class_="-bold -gray-dark-2 -uppercase -font-12 _padding-5")

print('\n\n\n\n\n\n\n\n')

print(temperatura.string)

print(soup.title.string)
print(soup.a)
print(soup.p.string)
print(soup.find('Temperatura'))