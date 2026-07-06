#!/usr/bin/python3
"""Script that lists all City objects along with their state name,
from the database hbtn_0e_14_usa, using SQLAlchemy.
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    # Create the engine and connect to the given database
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)

    # Create a session bound to the engine
    Session = sessionmaker(bind=engine)
    session = Session()

    # Query all cities joined with their state, sorted by city id
    results = session.query(State, City).filter(
        City.state_id == State.id
    ).order_by(City.id).all()

    for state, city in results:
        print("{}: ({}) {}".format(state.name, city.id, city.name))

    session.close()
