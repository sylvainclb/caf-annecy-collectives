"""Add parent event to payments

Revision ID: 03efbbcc54de
Revises: 0d576470d1ed
Create Date: 2022-10-03 21:27:30.668256

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = "03efbbcc54de"
down_revision = "0d576470d1ed"
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column(
        "item_prices", sa.Column("parent_event_id", sa.Integer(), nullable=True)
    )
    op.create_foreign_key(None, "item_prices", "events", ["parent_event_id"], ["id"])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, "item_prices", type_="foreignkey")
    op.drop_column("item_prices", "parent_event_id")
    # ### end Alembic commands ###
