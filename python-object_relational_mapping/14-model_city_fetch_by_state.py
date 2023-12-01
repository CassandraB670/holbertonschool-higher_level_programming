#!/usr/bin/python3
""" pyhton file that contains the class definition of a state
and an instance """

import sys
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from model_city import City
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

    qr = session.query(City, State).filter(
        State.id == City.state_id).order_by(City.id).all()

    for city, state in qr:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
