from datetime import date
from datetime import datetime
from optparse import Option
from typing import Optional

from pydantic import BaseModel


class SchoolBase(BaseModel):
    name: Optional[str] = None
    date_posted : Optional[str] = datetime.now().date()

class SchoolCreate(SchoolBase):
    name : str
    date_posted : date
    class Config():
        orm_mode = True

class ShowSchool(SchoolBase):
    id : Optional[int]
    name : Optional[str]
    date_posted : Optional[date]
    class Config():
        orm_mode = True