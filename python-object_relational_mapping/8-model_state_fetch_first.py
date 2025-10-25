#!/usr/bin/python3
"""8-model_state_fetch_first

Get first State
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(
        sys.argv[1], sys.argv[2], sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        first_state = session.query(State).order_by(State.id).first()
        if not first_state:
            print("Nothing")
        else:
            print("{}: {}".format(first_state.id, first_state.name))
