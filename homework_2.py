
RECORDS = """test_user_login,2.0,success
test_user_login,3.0,success
test_display_devices,1.3,failure
test_display_devices,2.1,success,
test_user_logout,1.2,success,
test_show_alerts,10.0,failure,
test_display_devices,13,success"""


tablica_recordów = RECORDS.split("\n")
tablica_recordów_podzielonych = []

dict_of_dicts = {}

for record in tablica_recordów:
    lista = record.split(",")
    nazwa = lista[0]

    if nazwa not in dict_of_dicts:
        dict_of_dicts[nazwa] = dict(succes = 0, failure = 0, time = 0)

    if lista[2] == "success":
        dict_of_dicts[nazwa]["succes"] += 1

        if dict_of_dicts[nazwa]["time"] < float(lista[1]):
           dict_of_dicts[nazwa]["time"] = float(lista[1])

    if lista[2] == "failure":
        dict_of_dicts[nazwa]["failure"] += 1

nazwa_najdluzej_dzialajacego_testu = ''
czas_najdluzej_dzialajacego_testu = 0

for name, value in dict_of_dicts.items():

    czas_testu = (value["time"])

    if czas_testu >= czas_najdluzej_dzialajacego_testu:
        czas_najdluzej_dzialajacego_testu = czas_testu
        nazwa_najdluzej_dzialajacego_testu = name


print(dict_of_dicts)
print("Najdłużej działający test to: ", nazwa_najdluzej_dzialajacego_testu)







