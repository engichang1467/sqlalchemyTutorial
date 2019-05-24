from sqlalchemy import create_engine, Column, Integer, String, Sequence
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///:memory:', echo=True)
Base = declarative_base()

class User(Base):
    __tablename__= 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    fullname = Column(String(50))
    nickname = Column(String(50))

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s')>" % (self.name, self.fullname, self.nickname)

print(Base.metadata.create_all(engine))


# Create an Instance of the Mapped Class
# from DeclareMapping import User
mike_user = User(name='mike', fullname='Michael Chan', nickname='Vsause, Michael here!')
mike_user.name
mike_user.nickname
str(mike_user.id)

# Creating a Session
# from sqlalchemy.orm import sessionmaker
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

'''
from DeclareMapping import User
from sqlalchemy.orm import sessionmaker

Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

mike_user = User(name='mike', fullname='Michael Chan', nickname='Vsause, Michael here!')

'''
# https://docs.sqlalchemy.org/en/13/orm/tutorial.html
