#!/usr/bin/python3
"""10-model_state_my_get

This module connects to a MySQL database and retrieves state object
id with name given from command line
"""
import sys
from model_state import Base, State
from sqlalchemy import create_engine, func
from sqlalchemy.orm import Session

if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
        ),
        pool_pre_ping=True
    )
    Base.metadata.create_all(engine)
    with Session(engine) as session:
        state = (
            session.query(State)
            .filter(State.name == argv[4])
            .order_by(State.id)
            .first()
        )
        if state:
            print(state.id)
        else:
            print("Not found")
