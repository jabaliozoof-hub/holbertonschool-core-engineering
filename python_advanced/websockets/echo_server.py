#!/usr/bin/env python3
"""Echo WebSocket server."""
import asyncio
import websockets


async def connection_handler(websocket):
    """Echo every text message back to the sender."""
    async for message in websocket:
        await websocket.send(message)


async def main():
    """Start the server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
    