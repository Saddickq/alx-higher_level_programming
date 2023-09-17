#!/usr/bin/python3
""" a script that prints the State object with the name passed\
        as argument from the database hbtn_0e_6_usa"""
from sqlalchemy import create_engine
from sys import argv
from model_state import Base, State
from sqlalchemy.orm import sessionmaker


def main():
    """ Main Function """
    user = argv[1]
    passwd = argv[2]
    database = argv[3]
    state = argv[4]

    url = "mysql://{}:{}@localhost/{}".format(user, passwd, database)
    engine = create_engine(url, pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    try:
        gotten_states = session.query(State).filter(State.name == state).all()
        if gotten_states:
            for gotten_state in gotten_states:
                print(gotten_state.id)
        else:
            print("Not found")

    except Exception as error:
        print(f"An ERROR occurred {error}")

    finally:
        session.close()


if __name__ == "__main__":
    main()
