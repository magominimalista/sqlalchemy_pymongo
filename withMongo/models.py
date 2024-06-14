from sqlalchemy import Column, Integer, String, ForeignKey, create_engine, inspect
from sqlalchemy.orm import declarative_base, Session, relationship

Base = declarative_base()


class User(Base):
    __tablename__ = 'user_account'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    address = relationship(
        "Address", back_populates="user", cascade="all, delete-orphan"
    )

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, fullname={self.fullname})"


class Address(Base):
    __tablename__ = "address"
    id = Column(Integer, primary_key=True, autoincrement=True)
    email_address = Column(String(30), unique=True, nullable=False)
    user_id = Column(Integer, ForeignKey('user_account.id'), nullable=False)

    user = relationship("User", back_populates="address")

    def __repr__(self):
        return f"Address(id={self.id}, email_address={self.email_address})"


engine = create_engine("sqlite:///db_with_mongo.sqlite")
Base.metadata.create_all(engine)