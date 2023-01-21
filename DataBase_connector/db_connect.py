import aiosqlite
import asyncio


async def DataBase():
    DB = await aiosqlite.connect('JustBot_db.db')
    return DB


DB = asyncio.run(DataBase())
