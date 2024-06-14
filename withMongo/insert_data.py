from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session
from models import User, Address

engine = create_engine("sqlite:///db_with_mongo.sqlite")

with Session(engine) as session:
    existing_emails = {email for email, in session.execute(select(Address.email_address)).all()}

    def add_user(name, fullname, email):
        if email in existing_emails:
            print(f"Email {email} already exists, skipping.")
            return
        user = User(name=name, fullname=fullname, address=[Address(email_address=email)])
        session.add(user)
        existing_emails.add(email)

    add_user('philipe', 'Philipe Cairon', 'philipecairon@gmail.com')
    add_user('mike', 'Mike Coben', 'mikecoben@gmail.com')
    add_user('john', 'John Deep', 'johndeep@gmail.com')
    add_user('dexter', 'Dexter Code', 'dextercode@gmail.com')

    session.commit()
