import asyncio
import websockets


port = 8765
print(f"Iniciando Server no port {port}")

async def echo(websocket,path):
    print("Nova conexão no server")
    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            await websocket.send(message)
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado")

async def main():
    async with websockets.serve(echo, "localhost", port):
        await asyncio.Future()


asyncio.run(main())
