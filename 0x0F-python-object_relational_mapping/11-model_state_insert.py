#!/usr/bin/python3
""" a script that adds the State object “Louisiana”\
        to the database hbtn_0e_6_usa"""
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
        new_state = State(name='Louisiana')
        session.add(new_state)
        session.commit()
        print(new_state.id)
    except Exception as error:
        session.rollback()
        print(f"An ERROR occurred {error}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
