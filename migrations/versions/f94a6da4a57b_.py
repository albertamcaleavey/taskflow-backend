"""empty message

Revision ID: f94a6da4a57b
Revises: 62f58770f926
Create Date: 2022-04-10 19:35:31.355251

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f94a6da4a57b'
down_revision = '62f58770f926'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tasks', sa.Column('complete', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tasks', 'complete')
    # ### end Alembic commands ###
