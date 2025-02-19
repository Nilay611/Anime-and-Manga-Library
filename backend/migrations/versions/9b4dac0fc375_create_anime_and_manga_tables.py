"""Create anime and manga tables

Revision ID: 9b4dac0fc375
Revises: 
Create Date: 2025-01-24 01:30:36.473850

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9b4dac0fc375'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('anime',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=255), nullable=True),
    sa.Column('Type', sa.String(length=50), nullable=True),
    sa.Column('Episodes', sa.Integer(), nullable=True),
    sa.Column('Aired', sa.String(length=100), nullable=True),
    sa.Column('Members', sa.Integer(), nullable=True),
    sa.Column('Score', sa.Float(), nullable=True),
    sa.Column('Rank', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('page_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('manga',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('Title', sa.String(length=255), nullable=True),
    sa.Column('Type', sa.String(length=50), nullable=True),
    sa.Column('Volumes', sa.Integer(), nullable=True),
    sa.Column('Published', sa.String(length=100), nullable=True),
    sa.Column('Members', sa.Integer(), nullable=True),
    sa.Column('Score', sa.Float(), nullable=True),
    sa.Column('Rank', sa.Integer(), nullable=True),
    sa.Column('image_url', sa.String(length=500), nullable=True),
    sa.Column('page_url', sa.String(length=500), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('manga')
    op.drop_table('anime')
    # ### end Alembic commands ###
