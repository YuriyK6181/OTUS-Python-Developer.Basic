from sqlalchemy import Column, Integer, String
from .database import dbase


class DemoItem(dbase.Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(80), unique=True, nullable=False)
    descr = Column(String(300), unique=False, nullable=True)
