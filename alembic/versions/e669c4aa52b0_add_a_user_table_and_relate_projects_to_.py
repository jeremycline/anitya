"""Add a user table and relate projects to users

Revision ID: e669c4aa52b0
Revises: 9c29da0af3af
Create Date: 2017-03-02 13:35:03.895232

"""

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e669c4aa52b0'
down_revision = '9c29da0af3af'


def upgrade():
    """
    Add a user table and a new foreign key column on projects that maps a
    project to a user.
    """
    op.create_table(
        'user',
        sa.Column('name', sa.String(length=200), nullable=False),
        sa.PrimaryKeyConstraint('name')
    )
    op.add_column(u'projects', sa.Column('created_by_id', sa.String(length=200), nullable=True))
    op.create_foreign_key(
        'FK_PROJECT_CREATOR',
        'projects',
        'user',
        ['created_by_id'],
        ['name'],
        onupdate='cascade',
        ondelete='set null'
    )


def downgrade():
    """
    Drop the user table and the foreign key column to it in the projects table.
    """
    op.drop_constraint('FK_PROJECT_CREATOR', 'projects', type_='foreignkey')
    op.drop_column(u'projects', 'created_by_id')
    op.drop_table('user')
