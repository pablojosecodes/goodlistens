"""Modify episode table

Revision ID: b8d7d20a4d40
Revises: 3d6fa183ee72
Create Date: 2024-05-14 10:21:52.721639

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b8d7d20a4d40'
down_revision = '3d6fa183ee72'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('episode', schema=None) as batch_op:
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               nullable=True)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
        batch_op.alter_column('duration',
               existing_type=sa.INTEGER(),
               nullable=True)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('episode', schema=None) as batch_op:
        batch_op.alter_column('duration',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.alter_column('title',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
        batch_op.alter_column('date',
               existing_type=sa.DATETIME(),
               nullable=False)

    # ### end Alembic commands ###
