import asyncio

import uvloop
from arq import create_pool
from arq.connections import RedisSettings

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())


async def test_task(ctx, word: str) -> str:
    return f"test task return {word}"


async def startup(ctx):
    print("start")


async def shutdown(ctx):
    print("end")


class WorkerSettings:
    functions = [test_task]
    on_startup = startup
    on_shutdown = shutdown
    handle_signals = False


async def main():
    redis = await create_pool(RedisSettings())
    for num in range(10):
        await redis.enqueue_job("test_task", num)
    redis.close()
    await redis.wait_closed()


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
