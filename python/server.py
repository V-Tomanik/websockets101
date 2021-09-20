import asyncio
from websockets import exceptions
from websockets import server 

#Porta que eu vou usar
port = 8765
print(f"Iniciando Server no port {port}")

#Todas as rotinas que o server performar precisa receber tanto a conecção "websocket" quando o path
async def echo(websocket,path):
    """
    Função de criação do servidor, espera a entrada de sockets e reenvia a mensagem que foi recebida para o mesmo socket,
    os outros clientes não recebem
    """
    print("Nova conexão no server")
    try:
        async for message in websocket:
            print(f"Mensagem recebida: {message}")
            await websocket.send(message)
    except exceptions.ConnectionClosed:
        print("Cliente desconectado")

async def echo_brodcast(websocket,path):
    """
    Função de criação de um servidor, lista todas as conecções, quando recebe uma mensagem envia para todos os outros clientes
    exeto para original
    """
    print("Nova conexão no server")
    clients_connected.add(websocket)
    try:
        async for message in websocket:
            for conn in clients_connected:
                #Envia para todos os clientes exeto o que realizado a comunicação
                if conn != websocket:
                    print(f"Mensagem recebida: {message}")
                    await conn.send(f"Outro cliente {message}")
    #Caso um socket se desconecte, para não dar erro
    except exceptions.ConnectionClosed:
        print("Cliente desconectado")
    finally:
        #Retira da lista o websocket que deslogou
        clients_connected.remove(websocket)


async def main():
    #Função de criação do servidor usando uma co-rotina no path localhost na porta x
    async with server.serve(echo, "localhost", port):
        await asyncio.Future()


clients_connected = set()
asyncio.run(main())
