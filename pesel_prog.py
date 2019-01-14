
import peseltools

pesel = input("Podaj swoj PESEL2: ")

print(peseltools.validate(pesel))
print(peseltools.extract_personal_data(pesel))

print("test")