# CORE sqlalchemy
import sqlalchemy as sa

engine = sa.create_engine('postgresql+psycopg://app_user:senha123@localhost:5432/sqlalchemy')

metadata = sa.MetaData() # catalogo com os metadados das tabelas = colunas ...

t = sa.Table('test', metadata, autoload_with=engine)
# autoload_with=engine -> ele carrega a tabela test automaticamente da conexao e faz a leitura

sql = (
    sa.select(t.c.id, t.c.nome, t.c.email) # cria o select automaticamente
    # t == tabela
    # c == coluna
    # nome da coluna
    .limit(10)
    .offset(10)
)
print(sql)

with engine.connect() as con:
    resulte = con.execute(sql)
    print(resulte.fetchall())