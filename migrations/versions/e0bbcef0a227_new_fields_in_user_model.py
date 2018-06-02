"""new fields in user model

Revision ID: e0bbcef0a227
Revises: 24404df44d84
Create Date: 2018-05-23 22:36:50.821823

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0bbcef0a227'
down_revision = '24404df44d84'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_Seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_Seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
