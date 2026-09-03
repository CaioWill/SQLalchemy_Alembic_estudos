# Estudos de SQLAlchemy e Alembic

Repositório com anotações e exemplos práticos de SQLAlchemy (ORM) e Alembic (migrações de banco de dados), seguindo o conteúdo do Dunossauro.

<br>

## O que foi estudado

**SQLAlchemy**
- **Core**: Engine (conexão com o banco), Dialect (tradução de SQL para o banco específico, ex: PostgreSQL), Connection Pool (gerenciamento de conexões abertas)
- **ORM (Object Relational Mapper)**: mapeamento entre tabelas do banco relacional e classes/objetos Python

**Migrações de banco de dados (Alembic)**
- Conceito de migrações evolutivas: versionamento de schema, prevenção de erros manuais, rollback em caso de conflito, padronização entre ambientes
- Configuração e uso do Alembic
- Geração automática de modelos e migrações a partir de classes SQLAlchemy

**Requests assíncronos**
- Uso do resquest assincronos: em aplicações com requisições em api, as apis demoram um tepo para enviar a requisição, logo usamos os resquest assincronos para o python ir fazendo outras quequisições enquando espera a primeira.  
- loop de eventos: a 'fila' de eventos que é processado nas 'pausas' do await.  

<br>

## Estrutura do repositório

- `models.py` — definição dos modelos (classes mapeadas via SQLAlchemy ORM)
- `alembic/` — scripts e versões de migração
- `exemplos/` — exemplos práticos de uso

<br>

## Próximos passos

Aplicação prática desses conceitos no curso de FastAPI (Dunossauro):
https://youtube.com/playlist?list=PLOQgLBuj2-3KT9ZWvPmaGFQ0KjIez0403

<br>

---

Parte da minha trilha de estudos para desenvolvimento backend com Python.