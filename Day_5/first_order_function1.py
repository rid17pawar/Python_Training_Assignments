#higher order function accepting another functions as parameters

patients_dob_data = ['10-02-1945', '26-01-1985', '01-10-2010', '10-02-2005']
CURRENT_YEAR = 2022

def get_dob_year(dob_data):
    years = [int(date.split('-')[2]) for date in dob_data]
    return years

def get_age(years_data):
    ages = [CURRENT_YEAR-date for date in years_data]
    return ages 

def get_adult_patient_ages(get_dob_year, get_age, dob_data):
    years = get_dob_year(dob_data)
    ages = get_age(years)
    adults = [ age for age in ages if age>18]
    return adults

#driver code
result = get_adult_patient_ages(get_dob_year, get_age, patients_dob_data) #higher order function
print(result)