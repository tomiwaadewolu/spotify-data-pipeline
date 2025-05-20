# scripts/init_db.py

from db import get_engine # for connecting to postgresql
from models import Base # for getting base class structure

# function to initialize the database
def initialize_db():
    engine = get_engine() # connect sqlachemy engine to database
    Base.metadata.create_all(engine) # create all defined tables
    print("Tables created successfully") # print confirmation message

# calling the function in main
if __name__ == "__main__":
    initialize_db()