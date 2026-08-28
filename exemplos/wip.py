from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

# Criando a conexao com o banco de dados
engine =  create_engine( # Factory
    'postgresql+psycopg://app_user:senha123@localhost:5432/sqlalchemy',
    # Postgres -> db
    # psycopg -> driver, Dialetoque sera usado para se comunicar com o postgreSQL
    # :// -> conexao

    #echo= True # -> mostra no terminal oque ta fazendo
)

with engine.connect() as con: # pode ser aberta ate 5 conexoes
    with con.begin(): # -> aqui é uma trasação
        sql = text("SELECT nome, email FROM test LIMIT 10")

        #mesma coisa do psycopg
        result = con.execute(sql).fetchall()
        for linha in result:
            print(f'nome: {linha[0]} email: {linha[1]}')

        # possui mais de 50 metodos, esses são os mais usados 
            # fetchone() -> pega o primeiro
            # fetchmany(n) -> pega o numero que voce colocou 
            # fetchall() -> pega 

    
    # with con.begin(): # -> outra transação, sem descartar a conexao, sendo mais rápido 
    #     sql = text("SELECT * LIMIT 10 OFFSET 10 FROM test")

    #     #mesma coisa do psycopg
    #     result = con.execute(sql).fetchall()
    #     print(result)

