"""empty message

Revision ID: 5666ee1d0743
Revises: b11fe840c805
Create Date: 2019-08-12 18:23:47.634286

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5666ee1d0743'
down_revision = 'b11fe840c805'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('last_login', sa.DateTime(), nullable=True))
    op.add_column('users', sa.Column('registered_on', sa.DateTime(), nullable=False))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'registered_on')
    op.drop_column('users', 'last_login')
    # ### end Alembic commands ###
