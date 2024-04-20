from sqlalchemy import ARRAY, Column, ForeignKey, Integer, String
from sqlalchemy.orm import Mapped, relationship

from .base import Base, created_at
from .user import UserModel


class ReviewModel(Base):
    __tablename__ = 'reviews'

    id = Column(
        Integer,
        primary_key=True,
        autoincrement=True
    )
    review = Column(
        String,
        nullable=False,
        default='Без текста'
    )
    user_id = Column(
        Integer,
        ForeignKey(UserModel.id),
        primary_key=True
    )
    photos = Column(
        ARRAY(String),
        nullable=True
    )
    likes = Column(
        Integer,
        default=0
    )

    created_at: Mapped[created_at]

    user = relationship(
        'UserModel',
        foreign_keys='ReviewModel.user_id'
    )
