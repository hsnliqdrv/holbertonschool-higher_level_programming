#!/usr/bin/python3
"""13-model_state_delete_a

This module connects to a MySQL database and deletes a State Object
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
        states = session.query(State).filter(State.name.like("%a%")).all()
        for state in states:
            session.delete(state)
        session.commit()
