"""
Add a creation time to versions.

Revision ID: 166516ff8ab5
Revises: 34b9bb5fa388
Create Date: 2018-07-14 14:28:01.887985
"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '166516ff8ab5'
down_revision = '34b9bb5fa388'


def upgrade():
    """Add a nullable column for the date versions were discovered."""
    op.add_column('projects_versions', sa.Column('created_on', sa.DateTime(), nullable=True))


def downgrade():
    """Drop the nullable column for the date versions were discovered."""
    op.drop_column('projects_versions', 'created_on')
