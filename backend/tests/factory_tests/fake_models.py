import factory
from werkzeug.security import generate_password_hash

from models import User, Mentee, University


class UserFactory(factory.Factory):
    class Meta:
        model = User

    username = factory.Faker('name')
    email = factory.Sequence(lambda n: 'person{0}@example.com'.format(n))
    password_hash = generate_password_hash('got')

class MenteeFactory(factory.Factory):
    class Meta:
        model = Mentee


    #mentor_id = db.Column(db.Integer, db.ForeignKey('mentors.id'))
    user = factory.SubFactory(UserFactory)
    city = factory.Faker('city')

class UniversityFactory(factory.Factory):
    class Meta:
        model = University

    name = factory.Sequence(lambda n: 'university{0}'.format(n))
    city = factory.Faker('city')
    country = factory.Faker('country')
