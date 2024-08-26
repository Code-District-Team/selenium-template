from faker import Faker
import time
import random
class RegistrationTestData:
    def generate_uuid():
        timestamp = int(time.time() * 1000)
        microseconds = int((time.time() % 1) * 1_000_000)

        def random_hex_char(char):
            nonlocal timestamp, microseconds
            rand = random.randint(0, 15)
            if timestamp > 0:
                rand = (timestamp + rand) % 16
                timestamp //= 16
            else:
                rand = (microseconds + rand) % 16
                microseconds //= 16
            if char == 'x':
                return format(rand, 'x')
            else:
                return format((rand&0x3)|0x8, 'x')

        uuid_pattern = 'xxxx-xxxx-4xxx-yxxx-xxxxxxxxx'
        uuid = ''.join(random_hex_char(char) if char in 'xy' else char for char in uuid_pattern)
        return uuid
    fake = Faker()

    email = f"{generate_uuid()}{fake.email()}"
    username = fake.first_name()
    surname = fake.last_name()
    password = "Test@123"
    address = fake.address()
    zipcode = fake.zipcode_plus4()
    street_address = fake.street_address()
    Company_name_search = "Code"
    minimum_project_price = "10000"
    employer_company = "Code District Learn"
    Job_title = fake.job()
    otp = "123456"
