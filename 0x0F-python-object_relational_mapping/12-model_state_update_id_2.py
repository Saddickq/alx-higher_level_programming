#!/usr/bin/python3
"""a script that changes the name of a State object from\
        the database hbtn_0e_6_usa"""
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
        state = session.query(State).filter(State.id == 2).first()
        if state:
            state.name = 'New Mexico'
            session.commit()
    except Exception as error:
        print(f"An ERROR occurred: {error}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
