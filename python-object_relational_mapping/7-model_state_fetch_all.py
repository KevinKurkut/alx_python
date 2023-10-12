#!/usr/bin/python3
"""All states via SQLAlchemy
list all states"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

username= sys.argv[1]
password=sys.argv[2]
db=sys.argv[3]

engine = create_engine(f'myql:/s/{username}:{password}@localhost:3306/{db}')
Base.metadata.bind = engine
DBSession = sessionmaker(bind=engine)
session = DBSession()

states = session.query(State).order_by(State.id).all()
for state in states:
    print(f'{state.id}: {state.name}')
session.close()
