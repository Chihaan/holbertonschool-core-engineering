#!/usr/bin/env python3

import asyncio
import websockets


async def connect_and_send():
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("Hello WebSocket")
        reponse = await ws.recv()
        print(reponse)


if __name__ == "__main__":
    asyncio.run(connect_and_send())
