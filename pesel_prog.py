
import peseltools

pesel = input("Podaj swoj PESEL: ")

print(peseltools.validate(pesel))
print(peseltools.extract_personal_data(pesel))