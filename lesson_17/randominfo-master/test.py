import randominfo

person = randominfo.Person()

# Виводимо основну інформацію
print("Ім’я:", person.full_name)
print("Стать:", person.gender)
print("Країна:", person.country)

# Форматуємо адресу: виводимо тільки непорожні частини
address = person.address
formatted_address = ', '.join([v for v in address.values() if v.strip() != ''])

print("Адреса:", formatted_address)
