#!/usr/bin/python3
"""14-model_city_fetch_by_state

This module connects to a MySQL database and gets all cities with states
"""
import sys
from model_state import Base, State
from model_city import City
from sqlalchemy import create_engine
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
        sc = (
                session.query(City, State)
                .join(State, State.id == City.state_id, isouter=True)
                .order_by(City.id)
                .all()
        )
        for city, state in sc:
            print("{}: ({}) {}".format(state.name, city.id, city.name))
