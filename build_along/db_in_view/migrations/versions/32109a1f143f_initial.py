"""initial

Revision ID: 32109a1f143f
Revises: 
Create Date: 2019-11-28 13:24:37.191448

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '32109a1f143f'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('puppies',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('puppies')
    # ### end Alembic commands ###
