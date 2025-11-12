# server/seed.py
from random import choice as rc
from faker import Faker
from app import app, db
from models import Pet

with app.app_context():  # Ensure app context for DB operations

    # Initialize Faker
    fake = Faker()

    # Clear the table first
    Pet.query.delete()

    # Species options
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Generate 10 random pets
    pets = [Pet(name=fake.first_name(), species=rc(species)) for _ in range(10)]

    # Insert and commit
    db.session.add_all(pets)
    db.session.commit()

    print("Database seeded with 10 random pets.")
