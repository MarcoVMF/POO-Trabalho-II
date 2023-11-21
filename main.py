from controllers import ControladorRelatorios
from models import Jogo, BancoDeDados, Configuracao, Desenvolvedora, FactoryJogo, ItemVenda, Pagamento, SistemaJogosEletronicos, Transportadora, Usuario, Venda
from views import *


jogoA = FactoryJogo.factoryJogo('Acao', 1, 'GTA V', 'Jogo de ação', 'Rockstar', '2013-09-17', 100, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 5, 'Muito bom', True)
jogoB = FactoryJogo.factoryJogo('Acao', 2, 'GTA IV', 'Jogo de ação', 'Rockstar', '2008-12-02', 50, 'Windows Vista - Service Pack 1 / Windows XP - Service Pack 3', 4, 'Bom', True)
jogoC = FactoryJogo.factoryJogo('Acao', 3, 'GTA III', 'Jogo de ação', 'Rockstar', '2002-05-20', 10, 'Windows 2000 / Windows XP', 3, 'Regular', True)


BancoDeDados.BancoDeDados()
BancoDeDados.BancoDeDados.inserirJogo(jogoA)
BancoDeDados.BancoDeDados.inserirJogo(jogoB)
BancoDeDados.BancoDeDados.inserirJogo(jogoC)

ControladorRelatorios.ControladorRelatorios.listarJogosMaisCaros()

