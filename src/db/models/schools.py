from db.base_class import Base
from sqlalchemy import Column
from sqlalchemy import Date
from sqlalchemy import Integer
from sqlalchemy import String

class School(Base):
    __table_args__ = {'extend_existing': True}
    id = Column(Integer, primary_key= True, index=True)
    name = Column(String, nullable=False)
    date_posted = Column(Date)