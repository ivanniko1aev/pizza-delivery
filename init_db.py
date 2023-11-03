from database import Base, engine
from models import User, Order

Base.metadata.create_all(bind=engine) # This creates the tables in the database 


# So we ran this file using python init_db.py to init the database