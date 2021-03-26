"""Add condition on payment item prices

Revision ID: 5a9ba75de4d1
Revises: aac7877cd693
Create Date: 2020-09-13 19:00:16.170600

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a9ba75de4d1'
down_revision = 'b8e4572a4af9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('item_prices', sa.Column('end_date', sa.Date(), nullable=True))
    op.add_column('item_prices', sa.Column('license_types', sa.String(length=256), nullable=True))
    op.add_column('item_prices', sa.Column('start_date', sa.Date(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('item_prices', 'start_date')
    op.drop_column('item_prices', 'license_types')
    op.drop_column('item_prices', 'end_date')
    # ### end Alembic commands ###