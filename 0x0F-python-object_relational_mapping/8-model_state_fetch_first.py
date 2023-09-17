#!/usr/bin/python3
""" a script that prints the first State object\
        from the database hbtn_0e_6_usa"""
from model_state import Base, State
from sqlalchemy import create_engine
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
        state = session.query(State).order_by(State.id).first()

        if state:
            print("{}: {}".format(state.id, state.name))
        else:
            print("Nothing")

    except Exception as error:
        print(f"An error occurred {error}")

    finally:
        session.close()


if __name__ == "__main__":
    main()
