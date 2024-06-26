"""Fixed status with Booking

Revision ID: 689900841e75
Revises: 976daeb3a831
Create Date: 2024-06-30 13:56:39.464309

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '689900841e75'
down_revision = '976daeb3a831'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=mysql.VARCHAR(length=20),
               nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('booking', schema=None) as batch_op:
        batch_op.alter_column('status',
               existing_type=mysql.VARCHAR(length=20),
               nullable=True)

    # ### end Alembic commands ###
