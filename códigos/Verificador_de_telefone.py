import phonenumbers as ph
from phonenumbers import geocoder

phone = input('Digite um telefone no formato +551140028922: ')
phone_number = ph.parse(phone)
print(geocoder.description_for_number(phone_number, 'pt'))
