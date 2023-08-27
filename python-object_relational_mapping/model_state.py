from sqlalchemy import column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
"""
class States
id int NOT NULL AUTO_INCREMENT
name varchar(128)
PRIMARY KEY (`id`)
"""
class States(Base):
    __tablename__ = 'states'
    id = column(Integer(), primary_key=True, nullable=False)
    name = column(String(128), nullable=False)
    