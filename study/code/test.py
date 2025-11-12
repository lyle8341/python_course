import asyncio


async def display(num):
    await asyncio.sleep(1)
    print(num)

async def main():
    tasks = asyncio.create_task(display(num) for num in range(10))
    await asyncio.gather(tasks)


if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
    loop.close()
