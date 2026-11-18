#!/usr/bin/env python3
"""WebSocket client."""
import asyncio
import websockets


async def connect_and_send(url: str, text: str) -> str:
    """Connect, send one message and return the server's reply."""
    async with websockets.connect(url) as websocket:
        await websocket.send(text)
        response = await websocket.recv()
        return response


async def main():
    """Send "Hello WebSocket" to the echo server and print the reply."""
    response = await connect_and_send("ws://127.0.0.1:8765", "Hello WebSocket")
    print(response, end="")


if __name__ == "__main__":
    asyncio.run(main())
