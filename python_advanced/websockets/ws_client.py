#!/usr/bin/env python3

import asyncio
import websockets


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as ws:
        await ws.send(message)
        reponse = await ws.recv()
        print(reponse)
        return reponse


if __name__ == "__main__":
    asyncio.run(connect_and_send(("ws://localhost:8765", "Hello WebSocket")))
