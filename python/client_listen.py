import asyncio
import websockets

async def listen():
    url = "ws://127.0.0.1:8765"
    async with websockets.connect(url) as websocket:
        await websocket.send("Conectando")
        while True:
            #Espera uma resposta
            msg = await websocket.recv()
            print(msg)


asyncio.get_event_loop().run_until_complete(listen())
