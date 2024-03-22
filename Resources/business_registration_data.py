import random
import string


class buisness_registrationTestData:
    def generate_random_letters(length=8):
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(length))

    business_email = "test@codedistrict.com"
    business_name = generate_random_letters()
    business_unit_name = "Automation"
    business_url = "https://codedistrict.com"
    revenue = "10000"
    company_size = "100"
    country_name = "Afghanistan"
    city_name = "Lahore"
    postalcode = "50000"
    street_address = "Queens road"
    basic_user_email = "asad.hafeez+909@codedistrict.com"

