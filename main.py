from controllers import ControladorRelatorios, ControladorJogo
from models import Jogo, BancoDeDados, Configuracao, Desenvolvedora, FactoryJogo, ItemVenda, Pagamento, SistemaJogosEletronicos, Transportadora, Usuario, Venda
from views import *


jogoA = FactoryJogo.factoryJogo.factory('Acao', 1, 'GTA V', 'Jogo de ação', 'Rockstar', '17/09/2013', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoB = FactoryJogo.factoryJogo.factory('Acao', 2, 'GTA IV', 'Jogo de ação', 'Rockstar', '02/12/2008', 50, 'Windows Vista - Service Pack 1 / Windows XP - Service Pack 3', 4, 'Bom', True)
jogoC = FactoryJogo.factoryJogo.factory('Acao', 3, 'GTA III', 'Jogo de ação', 'Rockstar', '20/05/2002', 10, 'Windows 2000 / Windows XP', 3, 'Regular', True)
jogoD = FactoryJogo.factoryJogo.factory('Aventura', 4, 'The Legend of Zelda: Breath of the Wild', 'Jogo de aventura', 'Nintendo', '03/03/2017', 200, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoE = FactoryJogo.factoryJogo.factory('Aventura', 5, 'The Legend of Zelda: Ocarina of Time', 'Jogo de aventura', 'Nintendo', '21/11/1998', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoF = FactoryJogo.factoryJogo.factory('Aventura', 6, 'The Legend of Zelda: Majora\'s Mask', 'Jogo de aventura', 'Nintendo', '27/04/2000', 50, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 4, 'Bom', True)
jogoG = FactoryJogo.factoryJogo.factory('Aventura', 7, 'The Legend of Zelda: Twilight Princess', 'Jogo de aventura', 'Nintendo', '19/11/2006', 10, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 3, 'Regular', True)
jogoH = FactoryJogo.factoryJogo.factory('Aventura', 8, 'The Legend of Zelda: Skyward Sword', 'Jogo de aventura', 'Nintendo', '18/11/2011', 200, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoI = FactoryJogo.factoryJogo.factory('Aventura', 9, 'The Legend of Zelda: A Link to the Past', 'Jogo de aventura', 'Nintendo', '21/11/1991', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoJ = FactoryJogo.factoryJogo.factory('Aventura', 10, 'The Legend of Zelda: The Wind Waker', 'Jogo de aventura', 'Nintendo', '13/12/2002', 50, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 4, 'Bom', True)
jogoK = FactoryJogo.factoryJogo.factory('Aventura', 11, 'The Legend of Zelda: Phantom Hourglass', 'Jogo de aventura', 'Nintendo', '23/06/2007', 10, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 3, 'Regular', True)
jogoL = FactoryJogo.factoryJogo.factory('Aventura', 12, 'The Legend of Zelda: Spirit Tracks', 'Jogo de aventura', 'Nintendo', '07/12/2009', 200, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoM = FactoryJogo.factoryJogo.factory('Aventura', 13, 'The Legend of Zelda: A Link Between Worlds', 'Jogo de aventura', 'Nintendo', '22/11/2013', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)


bd = BancoDeDados.BancoDeDados()
sistema = SistemaJogosEletronicos.SistemaJogosEletronicos()


controlador_jogo = ControladorJogo.ControladorJogo(sistema)

controlador_jogo.inserirJogo(jogoA)
controlador_jogo.inserirJogo(jogoB)
controlador_jogo.inserirJogo(jogoC)
controlador_jogo.inserirJogo(jogoD)
controlador_jogo.inserirJogo(jogoE)
controlador_jogo.inserirJogo(jogoF)
controlador_jogo.inserirJogo(jogoG)
controlador_jogo.inserirJogo(jogoH)
controlador_jogo.inserirJogo(jogoI)
controlador_jogo.inserirJogo(jogoJ)
controlador_jogo.inserirJogo(jogoK)
controlador_jogo.inserirJogo(jogoL)
controlador_jogo.inserirJogo(jogoM)


controlador = ControladorRelatorios.ControladorRelatorios(sistema)
mais_caros = controlador.listarJogosMaisCaros()
mais_baratos = controlador.listasJogosMaisBaratos()

aux = 1

print("MAIS CAROS")

for jogos in mais_caros:
    print(f"{aux} - {jogos.nome} - {jogos.valor}")
    print()
    aux = aux + 1

aux = 1

print("MAIS BARATOS")

for jogos in mais_baratos:
    print(f"{aux} - {jogos.nome} - {jogos.valor}")
    print()
    aux = aux + 1