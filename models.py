from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, declarative_base

Base = declarative_base()

class Hostel(Base):
    __tablename__ = 'hostels'

    id = Column(Integer(), primary_key=True)
    name = Column(String(), nullable=False)
    capacity = Column(Integer())

    students = relationship("Student", back_populates='hostel')

    def __repr__(self):
        return f"Name: '{self.name}' Capacity: '{self.capacity}' rooms"

class Student(Base):
    __tablename__ = 'students'

    id = Column(Integer(), primary_key=True)
    reg_no = Column(Integer(), nullable=False)
    name = Column(String(), nullable=False)
    hostel_id = Column(Integer(), ForeignKey('hostels.id'))

    hostel = relationship("Hostel", back_populates='students')


    def __repr__(self):
        return f"Student's name: '{self.name}' Reg_No: '{self.reg_no}'"
