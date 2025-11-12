from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)  # make sure db is bound to the app

class Pet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    species = db.Column(db.String(80), nullable=False)

@app.route('/pets')
def get_pets():
    pets = Pet.query.all()
    return jsonify([{'id': p.id, 'name': p.name, 'species': p.species} for p in pets])
if __name__ == '__main__':
    with app.app_context():
        db.create_all()  # creates tables if they don’t exist

        # Only seed if table is empty
        if Pet.query.count() == 0:
            from random import choice as rc
            from faker import Faker

            fake = Faker()
            species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

            pets = [Pet(name=fake.first_name(), species=rc(species)) for _ in range(10)]
            db.session.add_all(pets)
            db.session.commit()
            print("Seeded 10 random pets")

    app.run(port=5000)
