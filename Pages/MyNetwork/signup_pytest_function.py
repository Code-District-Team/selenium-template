
import requests
import json
from faker import Faker

faker = Faker()

class MyNetwork:
    email1, password1, name1, userId1 = None, None, None, None
    email2, password2, name2, userId2 = None, None, None, None
    base_url = "https://3m07x4g7pe.execute-api.us-west-2.amazonaws.com/dev/api/v1/account"

    @staticmethod
    def generate_user_data():
        email = faker.email()
        first_name = faker.first_name()
        last_name = faker.last_name()
        password = "Test@123"
        city = faker.city()
        job_title = faker.job()
        address1 = faker.street_address()
        zip_code = faker.postcode()
        primary_industry = "541110-01"
        area_of_interest = "171113"
        country = "LS"
        name = f"{first_name} {last_name}"

        cognito_user_payload = json.dumps({
            "firstName": first_name,
            "lastName": last_name,
            "password": password,
            "username": email
        })

        create_user_payload = json.dumps({
            "confirmationCode": "343333",
            "username": email,
            "jobTitle": job_title,
            "opsNotificationConsent": "true",
            "opportunitiesConsent": "false",
            "membershipType": "individual",
            "city": city,
            "address1": address1,
            "addressZip": zip_code,
            "country": country,
            "industryIds": [
                primary_industry
            ],
            "areaOfInterests": [
                area_of_interest
            ],
            "selfEmployed": "true",
            "region": "202",
            "pp": 2
        })

        return cognito_user_payload, create_user_payload, email, password, name

    @staticmethod
    def cognition_user(base_url, cognito_user_payload):
        response = requests.post(base_url + "/create-cognito-user", data=cognito_user_payload)
        message = response.json().get("message")
        print(response.status_code)
        return response, message

    @staticmethod
    def create_user(base_url, create_user_payload):
        response = requests.post(base_url, data=create_user_payload)
        print(response.status_code)
        return response

    def signup_test(self):
        user_data = [self.generate_user_data() for _ in range(2)]
        for index, data in enumerate(user_data):
            base_url = self.base_url

            # Create Cognito user
            cognito_user_payload, create_user_payload, email, password, name = data
            cognito_response, message = MyNetwork.cognition_user(base_url, cognito_user_payload)
            assert cognito_response.status_code == 201, "Failed to create Cognito user"

            # Create user
            user_response = MyNetwork.create_user(base_url, create_user_payload)
            assert user_response.status_code == 201, "Failed to create user"

            print("User Created Successfully")

            if index == 0:
                MyNetwork.email1, MyNetwork.password1, MyNetwork.name1, MyNetwork.userId1 = email, password, name, message
                print(f"First User: Email - {MyNetwork.email1}, Password - {MyNetwork.password1}, Name - {MyNetwork.name1}, UserId - {MyNetwork.userId1}")
            else:
                MyNetwork.email2, MyNetwork.password2, MyNetwork.name2, MyNetwork.userId2 = email, password, name, message
                print(f"Second User: Email - {MyNetwork.email2}, Password - {MyNetwork.password2}, Name - {MyNetwork.name2}, UserId - {MyNetwork.userId2}")

