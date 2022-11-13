"""init

Revision ID: 9dbd4a8f55fa
Revises:
Create Date: 2022-11-12 22:19:13.645815

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9dbd4a8f55fa'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    op.create_table(
        "publicacion",
        sa.Column("id", sa.Integer, primary_key=True, index=True),
        sa.Column("text", sa.String),
        sa.Column("date", sa.DateTime),
        sa.Column("classification", sa.String),
        sa.Column("person", sa.String),
    )


def downgrade() -> None:
    op.drop_table("publicacion")

