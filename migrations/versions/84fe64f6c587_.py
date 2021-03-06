"""empty message

Revision ID: 84fe64f6c587
Revises: f2384f9f69eb
Create Date: 2022-04-10 10:05:38.225759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84fe64f6c587'
down_revision = 'f2384f9f69eb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=True),
    sa.Column('deadline', sa.Date(), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('projects')
    # ### end Alembic commands ###
