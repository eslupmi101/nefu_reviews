from __future__ import annotations

from typing import TYPE_CHECKING, Union, List
from sqlalchemy import func, select, update

from app.database.models.user import UserModel
from app.database.models.review import ReviewModel

if TYPE_CHECKING:
    from aiogram.types import User
    from sqlalchemy.ext.asyncio import AsyncSession


async def add_user(
    session: AsyncSession,
    user: User,
    full_name: str
) -> None:
    """Add a new user to the database."""

    new_user = UserModel(
        id=int(user.id),
        username=user.username,
        full_name=full_name
    )

    session.add(new_user)
    await session.commit()


async def add_review(
    session: AsyncSession,
    user: UserModel,
    review: str,
    photos: list[str] | None = None
):
    """
    Add a review to the database.

    :param
    - session (AsyncSession): Async database session.
    - user (UserModel): User object representing the author of the review.
    - review (str): The text content of the review.
    - photos (List[str]): List of photo filenames associated with the review.
    """

    if photos is not None:
        instance = ReviewModel(
            user_id=user.id,
            review=review,
            photos=photos
        )
    else:
        instance = ReviewModel(
            user_id=user.id,
            review=review
        )

    session.add(instance)
    await session.commit()


async def get_all_review_texts(session: AsyncSession) -> List[str]:
    query = await session.execute(select(ReviewModel))
    reviews = query.scalars().all()
    review_texts = [str(review.user.full_name + ' ' + review.review) for review in reviews]
    return review_texts


async def get_user(
    session: AsyncSession,
    telegram_id: Union[int, str]
) -> UserModel | None:
    """Get a user to the database."""

    query = select(UserModel).filter(UserModel.id == telegram_id).limit(1)

    result = await session.execute(query)
    user = result.scalar_one_or_none()

    return user


async def user_exists(
    session: AsyncSession,
    telegram_id: int | str
) -> bool:
    """Checks if the user is in the database."""
    query = select(UserModel.id).filter_by(id=int(telegram_id)).limit(1)

    result = await session.execute(query)

    user = result.scalar_one_or_none()
    return bool(user)


async def get_first_name(
    session: AsyncSession,
    user_id: int
) -> str:
    user_id = int(user_id)
    query = select(UserModel.first_name).filter_by(id=user_id)

    result = await session.execute(query)

    first_name = result.scalar_one_or_none()
    return first_name or ""


async def get_language_code(
    session: AsyncSession,
    user_id: int | str
) -> str:
    user_id = int(user_id)
    query = select(UserModel.language_code).filter_by(id=user_id)

    result = await session.execute(query)

    language_code = result.scalar_one_or_none()
    return language_code or ""


async def get_user_age(
    session: AsyncSession,
    user_id: int
) -> int:
    user_id = int(user_id)
    query = select(UserModel.age).filter_by(id=user_id)

    result = await session.execute(query)

    age = result.scalar_one_or_none()
    return age


async def set_language_code(
    session: AsyncSession,
    user_id: int | str,
    language_code: str,
) -> None:
    user_id = int(user_id)
    stmt = update(UserModel).where(UserModel.id == user_id).values(language_code=language_code)

    await session.execute(stmt)
    await session.commit()


async def set_user_age(
    session: AsyncSession,
    user_id: int | str,
    age: int,
) -> None:
    user_id = int(user_id)
    stmt = update(UserModel).where(UserModel.id == user_id).values(age=age)

    await session.execute(stmt)
    await session.commit()


async def is_admin(
    session: AsyncSession,
    user_id: int | str
) -> bool:
    user_id = int(user_id)
    query = select(UserModel.is_admin).filter_by(id=user_id)

    result = await session.execute(query)

    is_admin = result.scalar_one_or_none()
    return bool(is_admin)


async def set_is_admin(session: AsyncSession, user_id: int | str, is_admin: bool) -> None:
    user_id = int(user_id)
    stmt = update(UserModel).where(UserModel.id == user_id).values(is_admin=is_admin)

    await session.execute(stmt)
    await session.commit()


async def get_all_users(session: AsyncSession) -> list[UserModel]:
    query = select(UserModel)

    result = await session.execute(query)

    users = result.scalars()
    return list(users)


async def get_user_count(session: AsyncSession) -> int:
    query = select(func.count()).select_from(UserModel)

    result = await session.execute(query)

    count = result.scalar_one_or_none() or 0
    return int(count)
