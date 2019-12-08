"""empty message

Revision ID: 70973c0cef8f
Revises: 7d437513dbcc
Create Date: 2019-12-04 21:26:58.845616

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70973c0cef8f'
down_revision = '7d437513dbcc'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('profile_image')
    # op.add_column('users', sa.Column('profile_image', sa.String(), nullable=False, server_default='default_profile_img'))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'profile_image')
    # ### end Alembic commands ###