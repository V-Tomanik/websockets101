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

async def echo_brodcast(websocket,path):
    print("Nova conexão no server")
    clients_connected.add(websocket)
    try:
        async for message in websocket:
            for conn in clients_connected:
                #Envia para todos os clientes exeto o que realizado a comunicação
                if conn != websocket:
                    print(f"Mensagem recebida: {message}")
                    await conn.send(f"Outro cliente {message}")
    except websockets.exceptions.ConnectionClosed:
        print("Cliente desconectado")
    finally:
        #Retira da lista o websocket que deslogou
        clients_connected.remove(websocket)


async def main():
    async with websockets.serve(echo_brodcast, "localhost", port):
        await asyncio.Future()


clients_connected = set()
asyncio.run(main())
