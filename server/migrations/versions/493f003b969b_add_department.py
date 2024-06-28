"""add Department

Revision ID: 493f003b969b
Revises: 9af6ca9b228b
Create Date: 2024-06-28 19:01:10.316760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '493f003b969b'
down_revision = '9af6ca9b228b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('department',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('department')
    # ### end Alembic commands ###
