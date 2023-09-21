#!/usr/bin/python3
""" a script 14-model_city_fetch_by_state.py that prints all\
        City objects from the database hbtn_0e_14_usa """
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sys import argv
from relationship_state import Base, State
from relationship_city import City


def main():
    """ Main Function """
    try:
        url = 'mysql+mysqldb://{}:{}@localhost:3306/{}'
        engine = create_engine(url.format(argv[1], argv[2],
                                          argv[3]))

        Base.metadata.create_all(engine)
        create_session = sessionmaker(bind=engine)
        session = create_session()

        state = State(name="California")
        city = City(name="San Francisco", state_id=state.id)

        session.add(state, city)
        session.commit()
    except (Exception, IndexError) as e:
        print(e)


if __name__ == "__main__":
    main()
