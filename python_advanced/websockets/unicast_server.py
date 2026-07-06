#!/usr/bin/env python3

import asyncio
import websockets


connected = set()


async def connection_handler(websocket):
    connected.add(websocket)
    try:
        async for message in websocket:
            for client in connected.copy():
                await client.send("B:" + message)
    finally:
        connected.discard(websocket)


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())
