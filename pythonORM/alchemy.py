from sqlalchemy.orm import sessionmaker
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine

# Corrected database URL
engine = create_engine(
    'mysql://root:tormtorm@localhost:3306/employees'
)


Base = declarative_base()


class User(Base):
    __tablename__ = 'employees'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)

    def __repr__(self):
        return f"<User(name='{self.name}', fullname='{self.fullname}')>"


User.__table__
Session = sessionmaker(bind=engine)
session = Session()

myUser = User(name='Shaza', fullname='Shaza Ali')
session.add(myUser)
session.commit()
# Query the User table to check if 'Shaza' exists
user = session.query(User).filter_by(name='Shaza').first()

print(myUser)
