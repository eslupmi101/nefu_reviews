from sqlalchemy.orm import Mapped, mapped_column

from .base import Base, created_at, int_pk


class UserModel(Base):
    __tablename__ = "users"

    id: Mapped[int_pk]
    username: Mapped[str | None]

    full_name: Mapped[str]

    created_at: Mapped[created_at]
    is_admin: Mapped[bool] = mapped_column(default=False)
