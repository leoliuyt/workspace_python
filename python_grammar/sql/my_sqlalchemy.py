from sqlalchemy import Column,String,create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
class User(Base):
    __tablename__ = 'user'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # 一对多:
    books = relationship('Book')

class Book(Base):
    __tablename__ = 'book'
    id = Column(String(20),primary_key=True)
    name = Column(String(20))
    # “多”的一方的book表是通过外键关联到user表的:
    user_id = Column(String(20),ForeignKey('user.id'))


engine = create_engine('mysql+mysqlconnector://root:leoliu1033@localhost:3306/course_db') 
DBSession = sessionmaker(bind=engine)
session = DBSession()
new_user = User(id='2',name='Bob')
# session.add(new_user)
user = session.query(User).filter(User.id=='2').one()
print('type:',type(user))
print('name:',user.name)
session.commit()
session.close()

