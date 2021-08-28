from faker import Faker
from random import randrange
from server import User, BlogPost, db

faker = Faker()

for i in range(200):
    name = faker.name()
    address = faker.address()
    phone = faker.msisdn()
    email = f'{name.replace(" ", "_")}@email.com'
    new_user = User(
        name=name,
        address=address,
        phone=phone,
        email=email
    )

    db.session.add(new_user)
    db.session.commit()

for i in range(200):
    title = faker.sentence()
    body = faker.paragraph()
    date = faker.date_time()
    user_id = randrange(1, 200)

    new_blog = BlogPost(
        title=title,
        body=body,
        date=date,
        user_id=user_id
    )

    db.session.add(new_blog)
    db.session.commit()