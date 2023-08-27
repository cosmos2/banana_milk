from sqlalchemy.orm import Session

from . import models, schemas


def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(email=user.email, password=user.password)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def get_problems(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Problem).offset(skip).limit(limit).all()


def create_problem(db: Session, problem: schemas.Problem, user_id: int):
    db_problem = models.Problem(**problem.model_dump(), owner_id=user_id)
    db.add(db_problem)
    db.commit()
    db.refresh(db_problem)
    return db_problem
