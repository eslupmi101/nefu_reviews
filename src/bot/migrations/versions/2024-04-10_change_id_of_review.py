"""Change id of Review

Revision ID: bd3d61bb317b
Revises: 4202f9c0279b
Create Date: 2024-04-10 14:08:08.014788

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'bd3d61bb317b'
down_revision: Union[str, None] = '4202f9c0279b'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('reviews_id_key', 'reviews', type_='unique')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('reviews_id_key', 'reviews', ['id'])
    # ### end Alembic commands ###
