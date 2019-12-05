"""empty message

Revision ID: e6d4926a3b96
Revises: 180fdca72472
Create Date: 2019-12-03 16:31:34.278780

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e6d4926a3b96'
down_revision = '180fdca72472'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users') as batch_op:
        batch_op.drop_column('password')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('password', sa.VARCHAR(), nullable=True))
    op.drop_column('users', 'password_hash')
    # ### end Alembic commands ###