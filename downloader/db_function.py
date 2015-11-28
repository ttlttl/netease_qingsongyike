from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

engine = create_engine('mysql+mysqlconnector://test:hello@192.168.111.163/data', echo=True)
DBSession = sessionmaker(bind=engine)