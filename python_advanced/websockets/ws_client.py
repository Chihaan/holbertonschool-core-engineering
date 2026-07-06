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
    message = (
        os.environ.get("WS_MSG")
        or os.environ.get("WS_MESSAGE")
        or os.environ.get("WS_TEXT")
        or os.environ.get("MESSAGE")
        or os.environ.get("MSG")
        or "Hello WebSocket"
    )
    asyncio.run(connect_and_send(uri, message))
