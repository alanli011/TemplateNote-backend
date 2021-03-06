"""create notebooks table

Revision ID: 77932e18cd1d
Revises: bbad6dc534fe
Create Date: 2020-06-17 09:50:44.196086

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77932e18cd1d'
down_revision = 'bbad6dc534fe'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('notebooks',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('name', sa.String(length=120), nullable=False),
                    sa.Column('user_id', sa.Integer(), nullable=False),
                    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
                    sa.PrimaryKeyConstraint('id')
                    )
    op.alter_column('users', 'username',
                    existing_type=sa.VARCHAR(),
                    nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('users', 'username',
                    existing_type=sa.VARCHAR(),
                    nullable=False)
    op.drop_table('notebooks')
    # ### end Alembic commands ###
