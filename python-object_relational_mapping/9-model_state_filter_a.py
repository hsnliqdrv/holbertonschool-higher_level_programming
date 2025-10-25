#!/usr/bin/python3
"""9-model_state_filter_a

This module connects to a MySQL database and retrieves all State objects
from the states table whose name contains the letter 'a', sorted by id.
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
        states = (
            session.query(State)
            .filter(func.binary(State.name).like("%a%"))
            .order_by(State.id)
            .all()
        )
        for state in states:
            print(f"{state.id}: {state.name}")
