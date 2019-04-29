"""relationship poistettu humidity_temp

Revision ID: e687f4569ad0
Revises: d8eeaa18ba07
Create Date: 2019-04-29 13:38:25.065732

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e687f4569ad0'
down_revision = 'd8eeaa18ba07'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'humidity_temp', type_='foreignkey')
    op.drop_column('humidity_temp', 'user_id')
    op.drop_constraint(None, 'pics', type_='foreignkey')
    op.drop_column('pics', 'user_id')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('pics', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'pics', 'user', ['user_id'], ['id'])
    op.add_column('humidity_temp', sa.Column('user_id', sa.INTEGER(), nullable=True))
    op.create_foreign_key(None, 'humidity_temp', 'user', ['user_id'], ['id'])
    # ### end Alembic commands ###
