from functools import reduce


patients_dob_data = ['10-02-1945', '26-01-1985', '01-10-2010', '10-02-2005']
CURRENT_YEAR = 2022

def get_dob_year(date):
    return int(date.split('-')[2])

def get_age(dob_year):
    return CURRENT_YEAR-dob_year 

years_data = list(map(get_dob_year, patients_dob_data)) #convert map() o/p into list
print(years_data)
ages_data = list(map(get_age, years_data)) #convert map() o/p into list
print(ages_data)
#using lambda function : as we need it only once.No need to store function logic
adult_patients_data = list(filter(lambda age: age>=18, ages_data))
print(adult_patients_data)
age_avg = reduce(lambda age1, age2 : age1 + age2, adult_patients_data) / len(adult_patients_data)
print(int(age_avg))