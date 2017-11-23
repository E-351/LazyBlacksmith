"""add reaction preferences

Revision ID: 2c467ca0efe2
Revises: 87f483ad57c2
Create Date: 2017-11-23 14:40:10.383000

"""

# revision identifiers, used by Alembic.
revision = '2c467ca0efe2'
down_revision = '87f483ad57c2'

import sqlalchemy as sa

from alembic import op
from sqlalchemy.dialects import mysql


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user_preference', sa.Column('prod_te_implant', sa.Numeric(
        precision=3, scale=2, decimal_return_scale=2, asdecimal=False
    ), server_default='1.00', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_character_id', sa.BigInteger(), nullable=True))
    op.add_column('user_preference', sa.Column('reaction_facility', sa.Integer(), server_default='5', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_facility', sa.Integer(), server_default='0', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_me_rig', sa.Integer(), server_default='0', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_security', sa.String(length=1), server_default='h', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_system', sa.String(length=100), server_default='Jita', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_te_implant', sa.Numeric(
        precision=3, scale=2, decimal_return_scale=2, asdecimal=False
    ), server_default='1.00', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_manuf_te_rig', sa.Integer(), server_default='0', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_me_rig', sa.Integer(), server_default='0', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_price_regions', sa.Integer(), server_default='10000002', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_price_type', sa.String(length=4), server_default='buy', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_security', sa.String(length=1), server_default='l', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_system', sa.String(length=100), server_default='Rakapas', nullable=False))
    op.add_column('user_preference', sa.Column('reaction_te_rig', sa.Integer(), server_default='0', nullable=False))
    op.create_foreign_key(None, 'user_preference', 'user', ['reaction_character_id'], ['character_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'user_preference', type_='foreignkey')
    op.drop_column('user_preference', 'reaction_te_rig')
    op.drop_column('user_preference', 'reaction_system')
    op.drop_column('user_preference', 'reaction_security')
    op.drop_column('user_preference', 'reaction_price_type')
    op.drop_column('user_preference', 'reaction_price_regions')
    op.drop_column('user_preference', 'reaction_me_rig')
    op.drop_column('user_preference', 'reaction_manuf_te_rig')
    op.drop_column('user_preference', 'reaction_manuf_te_implant')
    op.drop_column('user_preference', 'reaction_manuf_system')
    op.drop_column('user_preference', 'reaction_manuf_security')
    op.drop_column('user_preference', 'reaction_manuf_me_rig')
    op.drop_column('user_preference', 'reaction_manuf_facility')
    op.drop_column('user_preference', 'reaction_facility')
    op.drop_column('user_preference', 'reaction_character_id')
    op.drop_column('user_preference', 'prod_te_implant')
    # ### end Alembic commands ###