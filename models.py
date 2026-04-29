from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String, DateTime

Base = declarative_base()

class Project(Base):
    __tablename__ = "Project"
    __table_args__ = {"schema": "Volha_Platnitskaya_project"}

    projectId = Column(Integer, primary_key=True)
    title = Column(String)
    description = Column(String)
    deadline = Column(DateTime)
    statusId = Column(Integer)