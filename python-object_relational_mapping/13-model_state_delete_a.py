#!/usr/bin/python3
""" Script that deletes all State objects
with a name containins the letter a from the database"""

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_state import Base, State

if __name__ == "__main__":
    mysql_username = sys.argv[1]
    mysql_password = sys.argv[2]
    db_name = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.format(
        mysql_username,
        mysql_password,
        db_name
    ), pool_pre_ping=True)

    Base.metadata.create_all(engine)

    Session = sessionmaker(bind=engine)
    session = Session()

    qr = session.query(State).filter(
        State.name.like('%a%')).delete(synchronize_session='fetch')

    session.commit()

    session.close()
