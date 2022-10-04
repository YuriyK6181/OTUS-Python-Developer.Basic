"""
создайте алхимичный engine
добавьте declarative base (свяжите с engine)
создайте объект Session
добавьте модели User и Post, объявите поля:
для модели User обязательными являются name, username, email
для модели Post обязательными являются user_id, title, body
создайте связи relationship между моделями: User.posts и Post.user
"""
import os

from sqlalchemy.orm import (
    declared_attr,
    declarative_base,
)

from sqlalchemy import (
    Column,
    String,
    Integer,
    Text,
    ForeignKey
)

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, AsyncEngine
from sqlalchemy.orm import sessionmaker

from sqlalchemy.orm import (
    relationship
)

PG_CONN_URI = os.environ.get("SQLALCHEMY_PG_CONN_URI") or "postgresql+asyncpg://username:passwd!@localhost/blog"


class Base:
    @declared_attr
    def __tablename__(cls):
        return f'{cls.__name__.lower()}s'

    def __repr__(self):
        return str(self)


Base = declarative_base(cls=Base)


class User(Base):
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(40), unique=False, nullable=False)
    username = Column(String(20), unique=True, nullable=False)
    email = Column(String(60), unique=True, nullable=False)
    posts = relationship('Post', back_populates='user', uselist=True)

    def __str__(self):
        return f'{self.__class__.__name__}('\
            f'id={self.id}, '\
            f'name={self.name}, '\
            f'username={self.username}, '\
            f'email={self.email})'


class Post(Base):
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    title = Column(String(200), unique=False, nullable=False)
    body = Column(Text, nullable=False, default='Empty')
    user_id = Column(Integer, ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='posts')

    def __str__(self):
        return f'{self.__class__.__name__}('\
            f'id={self.id}, '\
            f'title={self.title!r}, ' \
            f'body={self.body!r}, ' \
            f'user_id={self.user_id})'


async def fill_users(session: AsyncSession, users_list: list[dict]):
    users = [
        User(id=int(user.get("id")),
             name=user.get("name"),
             username=user.get("username"),
             email=user.get("email"))
        for user in users_list
    ]
    session.begin()
    session.add_all(users)
    await session.commit()


async def fill_posts(session: AsyncSession, posts_list: list[dict]):
    posts = [
        Post(id=int(post.get("id")),
             user_id=int(post.get("userId")),
             title=post.get("title"),
             body=post.get("body"))
        for post in posts_list
    ]
    session.begin()
    session.add_all(posts)
    await session.commit()

async_engine: AsyncEngine = create_async_engine(PG_CONN_URI, echo=True)

Session = sessionmaker(
    async_engine,
    class_=AsyncSession,
    expire_on_commit=False,
)
