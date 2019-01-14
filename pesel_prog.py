
import peseltools

pesel = input("Podaj swoj PESEL34343434343434: ")

print(peseltools.validate(pesel))
print(peseltools.extract_personal_data(pesel))

print("test")