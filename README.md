# ORM Client
Данный клиент является вспомогательной библиотекой, которая может стать частью фреймворка для тестирования API. Позволяет работать с базой данных по средствам `ORM` запросов. Основной библиотекой является `SQLAlchemy`

### Пример работы
Ниже приведён пример переиспользования библиотеки в своём проекте, все функции на вход принимают обязательный параметр `login`:
````
from orm_client.orm_client import OrmClient
from sqlalchemy import select, update, delete, Boolean, Column, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
orm = OrmClient(
    host='127.0.0.1',
    port='5432',
    database='database',
    user='user',
    password='password'
)


class User(Base):
    __tablename__ = 'Users'

    UserId = Column(UUID, primary_key=True)
    Login = Column(String(100))
    Email = Column(String(100))
    Activated = Column(Boolean, nullable=False)


# Типовой запрос с использованием оператора SELECT на выборку данных
def get_user_by_login(login: str):
    query = select([User]).where(User.Login == login)
    dataset = orm.send_query(query=query)
    return dataset

# Запрос с использованием операторов DELETE и WHERE для удаления данных
def del_user_by_login(login: str):
    query = delete(User).where(User.Login == login)
    orm.send_bulk_query(query=query)

# Запрос с использованием операторов UPDATE и WHERE для обновления данных 
def activate_user_by_login(login: str):
    query = update(User).where(User.Login == login).values(Activated=True)
    orm.send_bulk_query(query=query)

````