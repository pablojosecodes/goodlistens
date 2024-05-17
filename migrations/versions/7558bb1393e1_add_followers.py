"""Add Followers

Revision ID: 7558bb1393e1
Revises: 1212a72a99fa
Create Date: 2024-05-08 23:05:50.580832

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7558bb1393e1'
down_revision = '1212a72a99fa'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('followers',
    sa.Column('follower_id', sa.Integer(), nullable=False),
    sa.Column('followed_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['followed_id'], ['user.id'], ),
    sa.ForeignKeyConstraint(['follower_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('follower_id', 'followed_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('followers')
    # ### end Alembic commands ###
