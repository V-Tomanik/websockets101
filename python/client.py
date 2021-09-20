import asyncio
from websockets import client

async def listen():
    """
    Função de cliente, assim que conectar com o servidor, envia uma mensagem e espera 
    retornos"""
    url = "ws://127.0.0.1:8765"
    async with client.connect(url) as c:
        await c.send("Conectando")
        while True:
            #Espera uma resposta
            msg = await c.recv()
            print(msg)

asyncio.get_event_loop().run_until_complete(listen())
