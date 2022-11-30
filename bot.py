import discord
from discord import app_commands
import random

id_do_servidor = 1046484264302170192


class client(discord.Client):

    def __init__(self):
        super().__init__(intents=discord.Intents.default())
        self.synced = False #Usado para o bot não sincronizar todos os comandos de uma vez

    async def on_ready(self):
        await tree.sync()
        if not self.synced: # Checar se os comandos slash foram sincronizados
            await tree.sync(
                guild=discord.Object(id=id_do_servidor)
            )  # Voce tambem pode deixar sem id do servidor para funcionar em todos os servidores, mas isso fara que demore 1~24 horas pra responder.
            self.synced = True
        print(f"Entramos como {self.user}.")


aclient = client()
tree = app_commands.CommandTree(aclient)

@tree.command(guild=discord.Object(id=id_do_servidor),
              name='salve',
              description='Testando') #comando especifico para o seu servidor 1
async def slash2(interaction: discord.Interaction):
    await interaction.response.send_message(f"Salve parça!", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='dado',
              description='D6') #comando especifico para o seu servidor 2
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 6)
    await interaction.response.send_message(f"{numero}", ephemeral=False)


@tree.command(guild=discord.Object(id=id_do_servidor),
              name='dado2',
              description='D20') #comando especifico para o seu servidor 2
async def slash3(interaction: discord.Interaction):
    numero = random.randint(1, 20)
    await interaction.response.send_message(f"{numero}", ephemeral=False)


aclient.run(
    'MTA0NjgzMjI0MTE3MjU1Nzg3NA.GxTMbP.ld3O5P_opImv-lAv9OuYzeuhiXn5LTOgxnQtC4')

#Obs: NÃO compartilhe este token com NINGUEM que voce gerar.