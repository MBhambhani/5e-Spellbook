"""empty message

Revision ID: 15d963629be6
Revises: 3df819dd47d1
Create Date: 2019-07-14 00:34:30.172150

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15d963629be6'
down_revision = '3df819dd47d1'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('spells', sa.Column('bard', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('cleric', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('druid', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('paladin', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('ranger', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('sorcerer', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('warlock', sa.Boolean(), nullable=True))
    op.add_column('spells', sa.Column('wizard', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('spells', 'wizard')
    op.drop_column('spells', 'warlock')
    op.drop_column('spells', 'sorcerer')
    op.drop_column('spells', 'ranger')
    op.drop_column('spells', 'paladin')
    op.drop_column('spells', 'druid')
    op.drop_column('spells', 'cleric')
    op.drop_column('spells', 'bard')
    # ### end Alembic commands ###
