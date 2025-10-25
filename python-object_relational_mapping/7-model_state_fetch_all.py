#!/usr/bin/python3
"""7-model_state_fetch_all

Get all State objects Ordered by their ids in ascending order
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
        for state in session.query(State).order_by(State.id).all():
            print("{}: {}".format(state.id, state.name))
