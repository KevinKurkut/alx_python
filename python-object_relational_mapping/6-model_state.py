from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

Base = declarative_base()
"""First state model
table name is states"""
class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)

engine = create_engine('mysql://root:root@localhost:3306/hbtn_0e_6_usa')

if __name__ == '__main__':
    Base.metadata.create_all(engine)
