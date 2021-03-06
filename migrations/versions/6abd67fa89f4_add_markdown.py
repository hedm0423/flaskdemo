"""add markdown

Revision ID: 6abd67fa89f4
Revises: 16c06c739a94
Create Date: 2017-02-09 10:07:21.820000

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6abd67fa89f4'
down_revision = '16c06c739a94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('body_html', sa.Text(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'body_html')
    # ### end Alembic commands ###
