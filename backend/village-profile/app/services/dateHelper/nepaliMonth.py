def month_name(number):
    month = ''
    if number is 1:
        month = 'बैशाख'
    elif number is 2:
        month = 'जेठ'
    elif number is 3:
        month = 'असार'
    elif number is 4:
        month = 'श्रावण'
    elif number is 5:
        month = 'भदौ'
    elif number is 6:
        month = 'आश्विन'
    elif number is 7:
        month = 'कार्तिक'
    elif number is 8:
        month = 'मंसिर'
    elif number is 9:
        month = 'पौष'
    elif number is 10:
        month = 'माघ'
    elif number is 11:
        month = 'फाल्गुन'
    elif number is 12:
        month = 'चैत्र'
    return month


def get_nepali_number(number):
    n_number = ''

    for n in number:
        n_number = n_number + nepali_number(int(n))
        print(n_number)
    return n_number


def nepali_number(number):
    nnum = ''
    if number is 1:
        nnum = '१'
    elif number is 2:
        nnum = '२'
    elif number is 3:
        nnum = '३'
    elif number is 4:
        nnum = '४'
    elif number is 5:
        nnum = '५'
    elif number is 6:
        nnum = '६'
    elif number is 7:
        nnum = '७'
    elif number is 8:
        nnum = '८'
    elif number is 9:
        nnum = '९'
    elif number is 0:
        nnum = '०'
    return nnum


def get_fiscal_year(year=0):
    fiscal_year = ''
    if year == '२०७५':
        fiscal_year = '२०७५/७६'
    elif year == '२०७४':
        fiscal_year = '२०७४/७५'
    elif year == '२०७६':
        fiscal_year = '२०७६/७७'
    elif year == '२०७७':
        fiscal_year = '२०७७/७८'
    elif year == '२०७८':
        fiscal_year = '२०७८/७९'
    return fiscal_year
