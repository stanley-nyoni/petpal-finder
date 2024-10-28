"""reviews deleted

Revision ID: 3db93a9c0f24
Revises: 6bd39673c27f
Create Date: 2024-10-28 21:31:34.261959

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3db93a9c0f24'
down_revision = '6bd39673c27f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.add_column(sa.Column('deleted', sa.Boolean(), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('review', schema=None) as batch_op:
        batch_op.drop_column('deleted')

    # ### end Alembic commands ###
