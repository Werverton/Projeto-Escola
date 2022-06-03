from db.models.schools import School
from sqlalchemy.orm import Session
from schemas.schools import SchoolCreate

def create_new_school(school:SchoolCreate, db: Session):
    school_obj = School(**school.dict())
    db.add(school_obj)
    db.commit()
    db.refresh(school_obj)
    return school_obj

def list_schools(db: Session):
    schools = db.query(School).all() #no exemplo do cara estava invertido filter com all e isso estava dando erro.
    return schools

def list_schools_by_name(db: Session, name: str):
    schools = db.query(School).filter_by(name=name).all()

def list_schools_by_id(db: Session, id: int):
    schools = db.query(School).filter(School.id==id).all()
    return schools
