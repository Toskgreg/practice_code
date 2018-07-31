from datetime import datetime, date


birth_year = datetime.strptime("05 05 1994", "%d %m %Y")

def ageCalculator(birth_year):
    today = date.today()
    return today.year - birth_year.year 

    age = ageCalculator(birth_year)

    return age 