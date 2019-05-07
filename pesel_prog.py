
import peseltools

pesel = input("Podaj PESEL2: ")

print(peseltools.validate(pesel))
print(peseltools.extract_personal_data(pesel))

print("test")
