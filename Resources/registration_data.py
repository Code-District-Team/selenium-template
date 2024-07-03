from faker import Faker
class RegistrationTestData:
    fake = Faker()
    email = "anything@8pyk8lj3.mailosaur.net"
    username = fake.first_name()
    surname = fake.last_name()
    password = "Code@4180"
    address = fake.address()
    zipcode = fake.zipcode_plus4()
    street_address = fake.zipcode_plus4()
    compnay_name_search = "Code"
    minmum_project_price = "10000"
    freelance_company = "Code"