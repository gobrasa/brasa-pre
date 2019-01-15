"""empty message

Revision ID: 5429ce93e8b6
Revises: c7c0f94546f4
Create Date: 2019-01-15 08:34:18.234692

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5429ce93e8b6'
down_revision = 'c7c0f94546f4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('mentees', sa.Column('cycle_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'mentees', 'cycles', ['cycle_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'mentees', type_='foreignkey')
    op.drop_column('mentees', 'cycle_id')
    # ### end Alembic commands ###
