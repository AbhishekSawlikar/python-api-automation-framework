from faker import Faker

fake = Faker()

class UserPayloads:
    @staticmethod
    def create_user_payload(name: str = None, username: str = None, email: str = None) -> dict:
        return {
            "name": name or fake.name(),
            "username": username or fake.user_name(),
            "email": email or fake.email(),
            "address": {
                "street": fake.street_name(),
                "suite": fake.building_number(),
                "city": fake.city(),
                "zipcode": fake.zipcode(),
                "geo": {
                    "lat": str(fake.latitude()),
                    "lng": str(fake.longitude())
                }
            },
            "phone": fake.phone_number(),
            "website": fake.domain_name(),
            "company": {
                "name": fake.company(),
                "catchPhrase": fake.catch_phrase(),
                "bs": fake.bs()
            }
        }