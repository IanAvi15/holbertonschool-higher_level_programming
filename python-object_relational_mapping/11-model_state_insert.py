#!/usr/bin/python3
"""Script that adds the State object "Louisiana" to the database
hbtn_0e_6_usa, using SQLAlchemy.
"""
import sys
from model_state import Base, State
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

    # Create and insert the new state
    new_state = State(name="Louisiana")
    session.add(new_state)
    session.commit()

    # Print the new state's auto-generated id
    print(new_state.id)

    session.close()
