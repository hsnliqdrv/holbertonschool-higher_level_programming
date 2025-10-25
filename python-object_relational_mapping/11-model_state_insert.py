#!/usr/bin/python3
"""11-model_state_insert.py

This module connects to a MySQL database and adds new State Object
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
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(state.id)
