"""Add user and third_party_user tables

Revision ID: 793495dbc90c
Revises: 8040ef9a9dda
Create Date: 2017-06-23 19:08:45.990534
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '793495dbc90c'
down_revision = '8040ef9a9dda'


def upgrade():
    op.create_table(
        'local_user',
        sa.Column('id', sa.Integer(), nullable=False),
        sa.Column('primary_email', sa.String(length=256), nullable=False),
        sa.PrimaryKeyConstraint('id')
    )
    op.create_index(
        op.f('ix_local_user_primary_email'), 'local_user', ['primary_email'], unique=True)
    op.create_table(
        'third_party_user',
        sa.Column('third_party_user_id', sa.String(length=256), nullable=False),
        sa.Column('identity_service', sa.String(length=256), nullable=False),
        sa.Column('local_user_id', sa.Integer(), nullable=False),
        sa.ForeignKeyConstraint(['local_user_id'], ['local_user.id'], ),
        sa.PrimaryKeyConstraint('third_party_user_id', 'identity_service')
    )


def downgrade():
    op.drop_table('third_party_user')
    op.drop_index(op.f('ix_local_user_primary_email'), table_name='local_user')
    op.drop_table('local_user')
