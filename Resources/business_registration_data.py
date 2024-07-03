import random
import string
from faker import Faker


class business_registrationTestData:
    faker = Faker()

    business_email = faker.email()

    business_name = faker.company()
    business_unit_name = "Automation"
    business_url = "https://codedistrict.com"
    revenue = "10000"
    company_size = "100"
    country_name = "Afghanistan"
    city_name = faker.city()
    postalcode = faker.zipcode_plus4()
    street_address = faker.street_address()

