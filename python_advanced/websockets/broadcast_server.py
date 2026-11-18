#!/usr/bin/env python3
"""WebSocket server that broadcasts messages to all clients."""
import asyncio
import websockets
from websockets.exceptions import ConnectionClosed

connected_clients = set()


async def broadcast(text):
    """Send text to every connected client."""
    for client in list(connected_clients):
        try:
            await client.send(text)
        except ConnectionClosed:
            connected_clients.discard(client)


async def connection_handler(websocket):
    """Track the client and broadcast each message it sends."""
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            await broadcast("B:" + message)
    except ConnectionClosed:
        pass
    finally:
        connected_clients.discard(websocket)


async def main():
    """Start the server on 127.0.0.1:8765."""
    async with websockets.serve(connection_handler, "127.0.0.1", 8765):
        await asyncio.Future()


if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        pass
