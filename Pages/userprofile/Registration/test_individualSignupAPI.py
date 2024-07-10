import requests
import json
import pytest
from faker import Faker

faker = Faker()


class IndividualSignup:
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



    def user_data(self):
        return IndividualSignup.generate_user_data()


    def signup(self):
        base_url = IndividualSignup.base_url

        # Create Cognito user
        cognito_user_payload, create_user_payload, email, password, name = self.generate_user_data()
        cognito_response, message = IndividualSignup.cognition_user(base_url, cognito_user_payload)
        assert cognito_response.status_code == 201, "Failed to create Cognito user"

        # Create user
        user_response = IndividualSignup.create_user(base_url, create_user_payload)
        assert user_response.status_code == 201, "Failed to create user"

        print("User Created Successfully")
        print("Username: ", name)
        print("Password: ", password)
        print("Email: ", email)

        return email, password
