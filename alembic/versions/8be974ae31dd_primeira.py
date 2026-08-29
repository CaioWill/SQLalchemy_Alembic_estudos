"""primeira

Revision ID: 8be974ae31dd
Revises: 
Create Date: 2026-08-29 15:07:38.383956

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '8be974ae31dd'
down_revision: Union[str, Sequence[str], None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


#criação da tabela implementada na nova versão
def upgrade() -> None:
    """Upgrade schema."""
    op.create_table(
        'empresas',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome_empresa', sa.String, nullable= False),
        sa.Column('email', sa.String, unique=True, nullable= False),
        sa.Column('data_criação', sa.DateTime, default= sa.func.now())
    )
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.drop_table('empresas')
    pass
