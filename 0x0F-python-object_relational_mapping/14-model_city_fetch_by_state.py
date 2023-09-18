#!/usr/bin/python3
""" a script 14-model_city_fetch_by_state.py that prints all\
        City objects from the database hbtn_0e_14_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from model_state import Base, State
from model_city import City


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
        cities = session.query(City).order_by(City.id).all()
        if cities:
            for city in cities:
                print(f"{city.state.name}: ({city.id}) {city.name}")
    except Exception as error:
        print(f"An ERROR occurred: {error}")
    finally:
        session.close()


if __name__ == "__main__":
    main()
