#!/usr/bin/env python3

import asyncio
import websockets


async def connection_handler(websocket):
    try:
        async for message in websocket:
            if message.strip():
                await websocket.send("OK:", message)
            else:
                await websocket.send("ERR:EMPTY")
    except websockets.ConnectionClosed:
        pass


async def main():
    async with websockets.serve(connection_handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
