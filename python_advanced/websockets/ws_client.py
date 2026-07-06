#!/usr/bin/env python3

import asyncio
import websockets


async def main():
    async with websockets.connect("ws://localhost:8765") as ws:
        await ws.send("Salut serveur")
        reponse = await ws.recv()
        print("Le serveur dit:", reponse)


if __name__ == "__main__":
    asyncio.run(main())
