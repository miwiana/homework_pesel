
def validate(pesel) :

    """ Validate PESEL number (lenght, check sum and correctness of birth date)
    Args:
        PESEL number to validate.
    Returns:
        True when number PESEL is correct otherwise returns False.
    """

    if len(pesel) != 11:
        return False

    check_sum = 0
    waga = 9

    for char in pesel[0:10]:
        check_sum += waga * int(char)

        if waga == 1:
            waga = 9
        elif waga == 7:
            waga = 3
        else:
            waga -= 2

    #check_sum = ((9 * int(pesel[0])) +
    #             (7 * int(pesel[1])) +
    #             (3 * int(pesel[2])) +
    #             (1 * int(pesel[3])) +
    #             (9 * int(pesel[4])) +
     #            (7 * int(pesel[5])) +
     #            (3 * int(pesel[6])) +
      #           (1 * int(pesel[7])) +
       #          (9 * int(pesel[8])) +
        #         (7 * int(pesel[9])))

    modulo = check_sum % 10

    if modulo != int(pesel[10]):
        return False

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])

    if month % 20 < 1 or month %20 > 12 :
        return False

    if 1 <= month <= 12:
        year = 1900 + year
    if 21 <= month <= 32:
        year = 2000 + year
    if 41 <= month <= 52:
        year = 2100 + year
    if 61 <= month <= 72:
        year = 2200 + year
    if 81 <= month <= 92:
        year = 1800 + year

    if month % 20 == 2:
        if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
            max_day = 29
        else:
            max_day = 28
    else:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        ind = (month % 20) - 1
        max_day = days[ind]

    if day > max_day:
        return False

    return True

def extract_personal_data(pesel):
    """Extract personal data (birth date and sex) from PESEL number.
    Args:
        PESEL number

    Returns:
        Personal data if PESEL number is correct, otherwise returns ValueError.
    """

    flag = validate(pesel)

    if flag == False:
        raise ValueError("Podany PESEL jest błędny")

    year = int(pesel[0:2])
    month = int(pesel[2:4])
    day = int(pesel[4:6])
    sex = int(pesel[9]) % 2

    if 1 <= month <= 12:
        year_pr = 1900 + year
    if 21 <= month <= 32:
        year_pr = 2000 + year
    if 41 <= month <= 52:
        year_pr = 2100 + year
    if 61 <= month <= 72:
        year_pr = 2200 + year
    if 81 <= month <= 92:
        year_pr = 1800 + year

    months = ["Styczeń", "Luty", "Marzec", "Kwiecień", "Maj", "Czerwiec", "Lipiec", "Sierpień", "Wrzesień", "Październik", "Listopad", "Grudzień"]

    x = (month % 20) - 1
    month_pr = months[x]


    if sex == 0:
        sex_pr = "Kobieta"
    else:
        sex_pr = "Mężczyzna"

    data_pr = "{} {} {}".format(day, month_pr, year_pr)
    pesel_dict = dict(birth_date=(data_pr), sex=sex_pr)

    return pesel_dict
