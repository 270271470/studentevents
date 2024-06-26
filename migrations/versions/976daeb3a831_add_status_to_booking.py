"""Add status to Booking

Revision ID: 976daeb3a831
Revises: 2b835b2a273e
Create Date: 2024-06-30 13:39:49.883999

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '976daeb3a831'
down_revision = '2b835b2a273e'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.add_column(sa.Column('status', sa.String(length=20), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.drop_column('status')

    # ### end Alembic commands ###
