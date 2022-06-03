from typing import List
from fastapi import APIRouter, Depends, HTTPException, status


from db.session import get_db

from db.repository.schools import create_new_school
from db.repository.schools import list_schools
from db.repository.schools import list_schools_by_name
from db.repository.schools import list_schools_by_id


from schemas.schools import ShowSchool
from schemas.schools import SchoolCreate

from sqlalchemy.orm import Session

router = APIRouter()

@router.post("/cadastra-escola/", response_model=ShowSchool)
def create_school(school: SchoolCreate, db: Session = Depends(get_db)):
    school = create_new_school(school=school,db=db)
    return school

@router.get("/escolas", response_model=List[ShowSchool])
def read_schools(db:Session = Depends(get_db)):
    schools = list_schools(db=db)
    return schools


@router.get("/get/{id}", response_model=ShowSchool)
def read_job(id:int,db:Session = Depends(get_db)):
    school = list_schools_by_id(id=id,db=db)
    if not school:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Job with this id {id} does not exist")
    return school