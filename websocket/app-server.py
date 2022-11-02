import asyncio
import websockets

async def echo(websocket):
    while 1:
        async for message in websocket:
            if message == 'exit':
                break
            await websocket.send('message')

async def main():
    async with websockets.serve(echo, "0.0.0.0", 12001, max_size=1948576):
        await asyncio.Future()  # run forever

asyncio.run(main())