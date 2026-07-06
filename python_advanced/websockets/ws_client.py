#!/usr/bin/env python3


import asyncio
import os
import websockets


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as ws:
        await ws.send(message)
        response = await ws.recv()
        return response


async def main():
    uri = os.getenv("WS_URI", "ws://localhost:8765")
    if os.getenv("WS_URI"):
        message = "demo"
    else:
        message = "Hello WebSocket"

    response = await connect_and_send(uri, message)
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
