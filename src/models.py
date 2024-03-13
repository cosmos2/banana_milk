from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, DateTime, Table, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

Base = declarative_base()


user_problem = Table(
    'user_problem', Base.metadata,
    Column('user_id', ForeignKey('user.id'), primary_key=True),
    Column('problem_id', ForeignKey('problem.id'), primary_key=True),
    Column('correct', Boolean, nullable=True, default=None)
)


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(60), unique=True, index=True)
    password = Column(String(30))
    status = Column(Boolean, default=True)
    created = Column(DateTime, server_default=func.now())
    problems = relationship('Problem', secondary='user_problem', back_populates='users')


class Problem(Base):
    __tablename__ = 'problem'

    id = Column(Integer, primary_key=True, index=True)
    category_id = Column(Integer, ForeignKey('category.id'))
    category_detail_id = Column(Integer, ForeignKey('category_detail.id'))
    title = Column(String(256))
    content = Column(Text)
    explanation = Column(Text)
    subjective_answer = Column(String(60), nullable=True)

    users = relationship('User', secondary='user_problem', back_populates='problems')
    categories = relationship('Category', back_populates='problems')
    category_details = relationship('CategoryDetail', back_populates='problems')
    answers = relationship('Answer', back_populates='problems')


class Answer(Base):
    __tablename__ = 'answer'

    id = Column(Integer, primary_key=True, index=True)
    problem_id = Column(Integer, ForeignKey('problem.id'))
    content = Column(String(30))
    correct = Column(Boolean)

    problems = relationship('Problem', back_populates='answers')


class Category(Base):
    __tablename__ = 'category'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(24))
    detail = Column(String(36))

    problems = relationship('Problem', back_populates='categories')


class CategoryDetail(Base):
    __tablename__ = 'category_detail'

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(24))
    detail = Column(String(36))

    problems = relationship('Problem', back_populates='category_details')