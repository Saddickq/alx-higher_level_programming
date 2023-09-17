#!/usr/bin/python3
""" Write a script that lists all State objects that contain\
        the letter a from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from model_state import Base, State
from sys import argv
from sqlalchemy.orm import sessionmaker


def main():
    """ Main Function """
    user = argv[1]
    passwd = argv[2]
    database = argv[3]

    url = "mysql://{}:{}@localhost/{}".format(user, passwd, database)
    engine = create_engine(url, pool_pre_ping=True)

    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        states = session.query(State).order_by(State.id)\
                .filter(State.name.like('%a%'))
        if states:
            for state in states:
                print(f"{state.id}: {state.name}")
    except Exception as error:
        print(f"An ERROR occurred {error}")

    finally:
        session.close()


if __name__ == "__main__":
    main()
