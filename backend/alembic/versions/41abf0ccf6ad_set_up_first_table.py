"""Set up first table

Revision ID: 41abf0ccf6ad
Revises: 
Create Date: 2024-02-13 00:28:39.637560

"""

from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.sql import func


# revision identifiers, used by Alembic.
revision: str = "41abf0ccf6ad"
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "sensor_data",
        sa.Column("id", sa.Integer(), primary_key=True),
        sa.Column("sensor_id", sa.Integer()),
        sa.Column("distance", sa.Float()),
        sa.Column(
            "created_date", sa.DateTime, nullable=False, server_default=func.now()
        ),
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table("sensor_data")
    # ### end Alembic commands ###
