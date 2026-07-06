#!/usr/bin/python3
"""Script that changes the name of the State with id = 2 to
"New Mexico", in the database hbtn_0e_6_usa, using SQLAlchemy.
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

    # Find the state with id = 2 and update its name
    state = session.query(State).filter(State.id == 2).first()
    if state is not None:
        state.name = "New Mexico"
        session.commit()

    session.close()
