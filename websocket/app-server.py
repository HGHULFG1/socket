import asyncio
import websockets

async def echo(websocket):
    while 1:
        async for message in websocket:
            print(message)
            if isinstance(message, dict):
                if message.get('data', None):
                    await websocket.send(
                        {'enroll': True}
                    )
            if message == 'exit':
                break
            await websocket.send('message')

async def main():
    async with websockets.serve(echo, "0.0.0.0", 12001, max_size=1948576):
        await asyncio.Future()  # run forever

asyncio.run(main())