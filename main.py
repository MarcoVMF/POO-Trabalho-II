from controllers import ControladorRelatorios
from models import Jogo, BancoDeDados, Configuracao, Desenvolvedora, FactoryJogo, ItemVenda, Pagamento, SistemaJogosEletronicos, Transportadora, Usuario, Venda
from views import *


jogoA = FactoryJogo.factoryJogo.factory('Acao', 1, 'GTA V', 'Jogo de ação', 'Rockstar', '17/09/2013', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoB = FactoryJogo.factoryJogo.factory('Acao', 2, 'GTA IV', 'Jogo de ação', 'Rockstar', '02/12/2008', 50, 'Windows Vista - Service Pack 1 / Windows XP - Service Pack 3', 4, 'Bom', True)
jogoC = FactoryJogo.factoryJogo.factory('Acao', 3, 'GTA III', 'Jogo de ação', 'Rockstar', '20/05/2002', 10, 'Windows 2000 / Windows XP', 3, 'Regular', True)
jogoD = FactoryJogo.factoryJogo.factory('Aventura', 4, 'The Legend of Zelda: Breath of the Wild', 'Jogo de aventura', 'Nintendo', '03/03/2017', 200, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)

bd = BancoDeDados.BancoDeDados()

bd.inserirJogo(jogoA)
bd.inserirJogo(jogoB)
bd.inserirJogo(jogoC)
bd.inserirJogo(jogoD)

controlador = ControladorRelatorios.ControladorRelatorios()
jogos_acao = controlador.listarJogos(Jogo.Jogo)

for jogo in jogos_acao:
    print(jogo)
    print()

