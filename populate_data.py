import random
from faker import Faker
from django.contrib.auth.models import User as AuthUser
from users.models import User, Contact

fake = Faker()

# Create users
for _ in range(10):
    auth_user = AuthUser.objects.create_user(
        username=fake.user_name(),
        password='password'  # Set a default password for testing
    )
    User.objects.create(
        name=fake.name(),
        phone_number=fake.phone_number(),
        email=fake.email(),
        password=auth_user.password,
    )

# Create contacts
users = User.objects.all()
for user in users:
    for _ in range(random.randint(0, 10)):
        Contact.objects.create(
            user=user,
            name=fake.name(),
            phone_number=fake.phone_number()
        )
