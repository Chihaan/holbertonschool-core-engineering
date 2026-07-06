#!/usr/bin/env python3

import asyncio
import websockets


async def handler(websocket):
    async for message in websocket:
        print("reçu:", message)
        await websocket.send(message)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
