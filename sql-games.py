from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///cjinook")
base = declarative_base()

Session = sessionmaker(db)
session = Session()

class Games(base):
    __tablename__ = "Games"
    id = Column(Integer, primary_key = True)
    name = Column(String)
    year = Column(Integer)
    console = Column(String)
    genre = Column(String)

base.metadata.create_all(db)

tekken = Games(
    name = "Tekken",
    year = 2004,
    console = "SonyPlaystation",
    genre = "Fignting"
)

mortal_combat = Games(
    name = "Mortal Combat",
    year = 2003,
    console = "SonyPlaystation",
    genre = "Fignting"
)

crash_banditok = Games(
    name = "Crash",
    year = 2005,
    console = "SonyPlaystation",
    genre = "Racing"
)

medal_of_honour = Games(
    name = "Medal of Honour",
    year = 2000,
    console = "SonyPlaystation",
    genre = "Shooter"
)

# session.add(tekken)
# session.add(mortal_combat)
# session.add(crash_banditok)
# session.add(medal_of_honour)

# session.commit()

# games = session.query(Games).filter_by(id = 2).first()
# games.name = "Mortal Combat II"
# session.commit()
game_name = input("Name of the game: ")
games = session.query(Games).filter_by(name = game_name).first()
if games is not None:
    print(f"The {games.name} is found")
    confirmation = input("To delete the game press 'y'")
    if confirmation.lower() == "y":
        session.delete(games)
        session.commit()
        print("The game gas been deleted")
    else:
        print("Delete in cancelled")
else:
    print("Game not found")

game = session.query(Games)

for g in game:
    print(
        g.id,
        g.name,
        g.year,
        g.console,
        g.genre,
        sep = " | "
    )

