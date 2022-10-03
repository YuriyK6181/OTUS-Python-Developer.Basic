import asyncio
from loguru import logger
from models import (
    Base,
    async_engine,
    async_session as async_session,
    fill_users,
    fill_posts,
    )
from jsonplaceholder_requests import fetch_posts_data, fetch_users_data


async def create_tables():
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
        await conn.run_sync(Base.metadata.create_all)


async def get_info():
    logger.info("Starting get_info======================")

    users_data, posts_data = await asyncio.gather(
        fetch_users_data(),
        fetch_posts_data(),
    )
    return users_data, posts_data


async def main():
    await create_tables()
    users_data, posts_data = await get_info()
    logger.info("Users: Recs={}, Symb={}", len(users_data), len(str(users_data)))
    logger.info("Posts: Recs={}, Symb={}", len(posts_data), len(str(posts_data)))
    logger.info("Fill_tables======================")
    async with async_session() as session:
        await fill_users(session, users_data)
        await fill_posts(session, posts_data)
        await session.close()


if __name__ == "__main__":
    # Set event Policy only if work on Windows to prevent showing Error "Event loop is closed"
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

    asyncio.run(main())
