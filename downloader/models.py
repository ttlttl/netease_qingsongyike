#-*- coding: utf-8 -*-

from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Qingsongyike(Base):
    __tablename__ = 'qingsongyike'
    id = Column(Integer(), primary_key=True, autoincrement=True)
    title = Column(String(32))
    docid = Column(String(32), unique=True)
    ptime = Column(String(32))
    body = Column(Text)