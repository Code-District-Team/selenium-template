from faker import Faker
class RegistrationTestData:
    fake = Faker()
    email = fake.email()
    username = fake.first_name()
    surname = fake.last_name()
    password = "Test@123"
    address = fake.address()
    zipcode = fake.zipcode_plus4()
    street_address = fake.zipcode_plus4()
    Company_name_search = "Code"
    minimum_project_price = "10000"
    employer_company = "Code District Learn"
    Job_title = fake.job()
    otp = "123456"
