"""added first last name to mentors

Revision ID: 83f5af92cf6f
Revises: bbd9cd11f427
Create Date: 2019-01-26 20:36:53.920154

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '83f5af92cf6f'
down_revision = 'bbd9cd11f427'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mentees', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('mentees', sa.Column('last_name', sa.String(length=50), nullable=True))
    op.add_column('mentors', sa.Column('first_name', sa.String(length=50), nullable=True))
    op.add_column('mentors', sa.Column('last_name', sa.String(length=50), nullable=True))
    op.add_column('mentors', sa.Column('username', sa.String(length=64), nullable=True))
    op.create_index(op.f('ix_mentors_username'), 'mentors', ['username'], unique=True)
    op.create_foreign_key(None, 'mentors', 'pre_users', ['username'], ['username'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mentors', type_='foreignkey')
    op.drop_index(op.f('ix_mentors_username'), table_name='mentors')
    op.drop_column('mentors', 'username')
    op.drop_column('mentors', 'last_name')
    op.drop_column('mentors', 'first_name')
    op.drop_column('mentees', 'last_name')
    op.drop_column('mentees', 'first_name')
    # ### end Alembic commands ###