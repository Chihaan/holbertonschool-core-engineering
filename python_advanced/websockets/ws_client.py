#!/usr/bin/env python3

import asyncio, websockets, os, sys


async def connect_and_send(uri, message):
    async with websockets.connect(uri) as ws:
        await ws.send(message)
        reponse = await ws.recv()
        print(reponse, end="")
        return reponse


if __name__ == "__main__":
    uri = os.environ.get("WS_URI", "ws://localhost:8765")
    if len(sys.argv) > 1:
        message = sys.argv[2]
    else:
        message = os.environ.get("WS_MSG", "Hello WebSocket")
    asyncio.run(connect_and_send(uri, message))
