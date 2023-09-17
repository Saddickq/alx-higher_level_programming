#!/usr/bin/python3
""" a script that deletes all State objects with a name containing\
        the letter a from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State


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
        states = session.query(State).filter(State.name.like('%a%')).all()
        if states:
            for state in states:
                session.delete(state)
            session.commit()
    except Exception as error:
        session.rollback()
        print(f"An ERROR occurred: {errot}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
