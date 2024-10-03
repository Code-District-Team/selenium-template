from datetime import datetime, date  # Importing date class rom datetime module

import requests
import json
from faker import Faker

faker = Faker()


class BusinessBasicSignup:
    base_url = "https://3m07x4g7pe.execute-api.us-west-2.amazonaws.com/dev/api/v1/account"

    @staticmethod
    def generate_user_data():
        email = faker.email()
        first_name = faker.first_name()
        last_name = faker.last_name()
        password = "Test@123"
        city = faker.city()
        region = "034"
        start_date = datetime(2020, 1, 1).date()
        end_date = datetime(2024, 12, 31).date()
        date_ = faker.date_between_dates(start_date, end_date).isoformat()
        businessUrl = faker.url()
        company = faker.company()
        address1 = faker.street_address()
        zip_code = faker.postcode()
        primary_industry = "541110-01"
        area_of_interest = "171113"
        country = "AF"
        name = f"{first_name} {last_name}"

        cognito_user_payload = json.dumps({
            "firstName": first_name,
            "lastName": last_name,
            "password": password,
            "username": email
        })

        create_user_payload = json.dumps({
            "country": country,
            "username": email,
            "confirmationCode": "123456",
            "membershipType": "businessPlus",
            "opsNotificationConsent": True,
            "opportunitiesConsent": False,
            "province": "Badakhshān",
            "startDate": date_,
            "jobTitle": "Senior Software Engineer",
            "industryIds": [
                primary_industry
            ],
            "areaOfInterests": [
                area_of_interest
            ],
            "region": region,
            "city": city,
            "addressZip": zip_code,
            "address1": address1,
            "experience": {
                "businessEmail": email,
                "businessUrl": businessUrl,
                "address1": address1,
                "addressType": "REG",
                "addressZip": zip_code,
                "city": city,
                "company": company,
                "country": country,
                "region": region,
                "unit": "Software",
                "industries": [
                    {
                        "industryId": area_of_interest,
                        "primary": True
                    },
                    {
                        "industryId": primary_industry,
                        "primary": False
                    }
                ]
            },
            "noOfSeats": 10,
            "business": {
                "businessEmail": email,
                "businessUrl": businessUrl,
                "address1": address1,
                "addressType": "REG",
                "addressZip": zip_code,
                "city": city,
                "company": company,
                "country": country,
                "region": region,
                "unit": "Software",
                "industries": [
                    {
                        "industryId": area_of_interest,
                        "primary": True
                    },
                    {
                        "industryId": primary_industry,
                        "primary": False
                    }
                ]
            }
        })

        return cognito_user_payload, create_user_payload, email, password, name

    @staticmethod
    def cognition_user(base_url, cognito_user_payload):
        response = requests.post(base_url + "/create-cognito-user", data=cognito_user_payload)
        message = response.json().get("message")
        print(message)
        print(response.status_code)
        return response, message

    @staticmethod
    def create_user(base_url, create_user_payload):
        response = requests.post(base_url, data=create_user_payload)
        message = response.json().get("message")
        print(message)
        print(response.status_code)
        return response



    def user_data(self):
       return BusinessBasicSignup.generate_user_data()


    def signup(self):
        base_url = BusinessBasicSignup.base_url

    # Create Cognito user
        cognito_user_payload, create_user_payload, email, password, name = self.user_data()
        cognito_response, message = BusinessBasicSignup.cognition_user(base_url, cognito_user_payload)
        assert cognito_response.status_code == 201, "Failed to create Cognito user"

    # Create user
        user_response = BusinessBasicSignup.create_user(base_url, create_user_payload)
        response_dict = json.loads(user_response.text)  # Convert the JSON response to a dictionary

        # Print the status code and a specific message from the response
        print("Status Code:", user_response.status_code)
        print("Response Message:", response_dict.get("message"))
        assert user_response.status_code == 201, "Failed to create user"

        print("User Created Successfully")
        print("Username: ", name)
        print("Password: ", password)
        print("Email: ", email)

        return email, password
