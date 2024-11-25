from sqlalchemy import (
    create_engine, Column, Integer, String
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

db = create_engine("postgresql:///cjinook")

base = declarative_base()

class Programmer(base):
    __tablename__ = "Programmer"
    id = Column(Integer, primary_key = True)
    first_name = Column(String)
    last_name = Column(String)
    gender = Column(String)
    nationality = Column(String)
    famous_for = Column(String)

Session = sessionmaker(db)
session = Session()

base.metadata.create_all(db)

ada_lovelace = Programmer(
    first_name = "Ada",
    last_name = "Lovelace",
    gender = "F",
    nationality = "British",
    famous_for = "First Programmer"
)

alan_turing = Programmer(
    first_name = "Alan",
    last_name = "Turing",
    gender = "M",
    nationality = "British",
    famous_for = "Modern Computing"
)

grace_hopper = Programmer(
    first_name = "Grace",
    last_name = "Hopper",
    gender = "F",
    nationality = "American",
    famous_for = "COBOL Language"
)

margaret_hammilton = Programmer(
    first_name = "Margaret",
    last_name = "Hammilton",
    gender = "F",
    nationality = "American",
    famous_for = "Apollo 11"
)

bill_gates = Programmer(
    first_name = "Bill",
    last_name = "Gates",
    gender = "M",
    nationality = "American",
    famous_for = "Microsoft"
)

tim_berners_lee = Programmer(
    first_name = "Tim",
    last_name = "Berners-Lee",
    gender = "M",
    nationality = "British",
    famous_for = "World Wide Web"
)

alex_me = Programmer(
    first_name = "Alex",
    last_name = "Me",
    gender = "M",
    nationality = "Irish",
    famous_for = "Amazing!" 
)

# session.add(ada_lovelace)
# session.add(alan_turing)
# session.add(grace_hopper)
# session.add(margaret_hammilton)
# session.add(bill_gates)
# session.add(tim_berners_lee)
# session.add(alex_me)

# session.commit()

# programmer = session.query(Programmer).filter_by(id = 10).first()
# programmer.famous_for = "Student"

# session.commit()

# people = session.query(Programmer)
# for person in people:
#     if person.gender == "F":
#         person.gender = "Female"
#     elif person.gender == "M":
#         person.gender = "Male"
#     else:
#         print("Gender not defined")
#     session.commit()

# delete a single record
# fname = input("Enter first name: ")
# lname = input("Enter last name: ")

# programmer = session.query(Programmer).filter_by(first_name = fname, last_name = lname).first()

# defensive programming
# if programmer is not None:
#     print(f"Programmer found: {programmer.first_name} {programmer.last_name}")
#     confirmation = input("Are you sure you want to delete this record? (y/n)")
#     if confirmation.lower() == "y":
#         session.delete(programmer)
#         session.commit()
#         print("Programmer has been deleted")
#     else:
#         print("Programmer not deleted")
# else:
#     print("No records")

# delete multiply records
# programmers = session.query(Programmer)
# for programmer in programmers:
#     session.delete(programmer)
#     session.commit()

# query the database to find all programmers
programmers = session.query(Programmer)

for programmer in programmers:
    print(
        programmer.id,
        programmer.first_name,
        programmer.last_name,
        programmer.gender,
        programmer.nationality,
        programmer.famous_for,
        sep = " | "
    )