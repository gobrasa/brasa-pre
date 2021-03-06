"""add authenticated attribute to user

Revision ID: 2bf38a5fbc12
Revises: 40752845856d
Create Date: 2019-02-01 17:38:58.163361

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2bf38a5fbc12'
down_revision = '40752845856d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('authenticated', sa.Boolean(), nullable=True))
    op.alter_column('users','password_hash',type_=sa.String)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('users', 'authenticated')
    op.alter_column('users', 'password_hash', type_=sa.String(128))
    # ### end Alembic commands ###
