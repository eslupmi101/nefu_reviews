from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import Mapped, relationship

from .base import Base, created_at
from .user import UserModel


class ReviewModel(Base):
    __tablename__ = "reviews"

    id = Column(Integer, primary_key=True, autoincrement=True)
    review: Mapped[str]
    user_id = Column(
        Integer,
        ForeignKey(UserModel.id),
        primary_key=True
    )
    created_at: Mapped[created_at]
    likes = Column(
        Integer,
        default=0
    )

    user = relationship(
        'UserModel',
        foreign_keys='ReviewModel.user_id'
    )
