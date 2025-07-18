"""Adicionando campo senha_hash ao Administrador

Revision ID: 3264048bc8c0
Revises: fb388a6af780
Create Date: 2025-06-23 21:37:02.873574

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3264048bc8c0'
down_revision = 'fb388a6af780'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('_alembic_tmp_administradores')
    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=256), nullable=True))
        batch_op.drop_column('senha')

    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=256), nullable=True))
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=False)
        batch_op.create_unique_constraint('uq_clientes_email', ['email'])
        batch_op.drop_column('senha')

    with op.batch_alter_table('profissionais', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha_hash', sa.String(length=256), nullable=True))
        batch_op.drop_column('senha')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('profissionais', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.VARCHAR(length=256), nullable=False))
        batch_op.drop_column('senha_hash')

    with op.batch_alter_table('clientes', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.VARCHAR(length=256), nullable=True))
        batch_op.drop_constraint(None, type_='unique')
        batch_op.alter_column('email',
               existing_type=sa.VARCHAR(length=120),
               nullable=True)
        batch_op.drop_column('senha_hash')

    with op.batch_alter_table('administradores', schema=None) as batch_op:
        batch_op.add_column(sa.Column('senha', sa.VARCHAR(length=256), nullable=False))
        batch_op.drop_column('senha_hash')

    op.create_table('_alembic_tmp_administradores',
    sa.Column('idAdministrador', sa.INTEGER(), nullable=False),
    sa.Column('senha_hash', sa.VARCHAR(length=256), nullable=False),
    sa.Column('nome', sa.VARCHAR(length=100), nullable=False),
    sa.Column('email', sa.VARCHAR(length=120), nullable=False),
    sa.PrimaryKeyConstraint('idAdministrador'),
    sa.UniqueConstraint('email')
    )
    # ### end Alembic commands ###
