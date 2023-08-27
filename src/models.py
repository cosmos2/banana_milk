from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table, Text
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .database import Base


user_problem = Table(
    'user_problem', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('problem_id', ForeignKey('problem.id'), primary_key=True),
    Column('correct', Boolean, nullable=True, default=None)
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    password = Column(String)
    status = Column(Boolean, default=True)
    created = Column(DateTime, server_default=func.utcnow())
    problems = relationship('Problem', secondary='user_problem', back_populates='users')


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category_detail_id = Column(Integer, ForeignKey('category_detail.id'))
    title = Column(String)
    content = Column(Text)

    categories = relationship('Category', back_populates='problems')
    category_details = relationship('CategoryDetail', back_populates='problems')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)

    problems = relationship('Problem', back_populates='categories')


class CategoryDetail(Base):
    __tablename__ = 'category_detail'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    detail = Column(String)

    problems = relationship('Problem', back_populates='category_details')