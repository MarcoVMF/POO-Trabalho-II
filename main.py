from controllers import ControladorRelatorios, ControladorJogo, ControladorDesenvolvedora, ControladorTransportadora, ControladorUsuario, ControladorVendas
from models import Jogo, BancoDeDados, Configuracao, Desenvolvedora, FactoryJogo, ItemVenda, Pagamento, SistemaJogosEletronicos, Transportadora, Usuario, Venda, Iterator
from views import *

bd = BancoDeDados.BancoDeDados()
sistema = SistemaJogosEletronicos.SistemaJogosEletronicos()

controlador_desenvolvedora = ControladorDesenvolvedora.ControladorDesenvolvedora(sistema)
controlador_transportadora = ControladorTransportadora.ControladorTransportadora(sistema)
controlador_jogo = ControladorJogo.ControladorJogo(sistema)
controlador_usuario = ControladorUsuario.ControladorUsuario(sistema)


desenvolvedoraA = controlador_desenvolvedora.criarDesenvolvedora(1, '1234567', 'RockStar', 'rock@gmail', 'www.rockstar.com', 'www.instagram/rockstar', 'Rua RockAndRoll')
desenvolvedoraB = controlador_desenvolvedora.criarDesenvolvedora(2, '9876543', 'Nintendo', 'nintendo@gmail', 'www.nintendo.com', 'www.instagram/nintendo', 'Rua NintendoMania')


controlador_desenvolvedora.inserirDesenvolvedora(desenvolvedoraA)
controlador_desenvolvedora.inserirDesenvolvedora(desenvolvedoraB)


transportadoraA = controlador_transportadora.criarTransportadora(1, '1234567', 'Transportadora A', 'transportadoraA@gmail', '11 0118181717', 'Rua TransportadoraA', 14)
transportadoraB = controlador_transportadora.criarTransportadora(2, '9876543', 'Transportadora B', 'transportadoraB@gmail', '11 0118181717', 'Rua TransportadoraB', 5)


controlador_transportadora.inserirTransportadora(transportadoraA)
controlador_transportadora.inserirTransportadora(transportadoraB)

pagamentoA = Pagamento.CartaoCredito(1, 'Usuario A', 'Visa', '12345678910')
pagamentoB = Pagamento.Boleto(2, '12345678910')


usuarioA = controlador_usuario.criarCliente(1, 'Usuario A', '1234567', '131313-3', '20/04/2000', 'Rua UsuarioA', '12345678910', 'usuarioA@gmail', '20/05/2022', 0, 0, pagamentoA)
usuarioB = controlador_usuario.criarCliente(2, 'Usuario B', '9876543', '131313-3', '20/04/2000', 'Rua UsuarioB', '12345678910', 'usuarioB@gmail', '20/05/2022', 0, 1, pagamentoB)
gerenteA = controlador_usuario.criarGerente(1, 'Gerente A', '1234567', '131313-3', '20/04/2000', 'Rua GerenteA', '12345678910', 'gerenteA@gmail', '20/05/2022', 'Nivel A', 1)
gerenteB = controlador_usuario.criarGerente(2, 'Gerente B', '9876543', '131313-3', '20/04/2000', 'Rua GerenteB', '12345678910', 'gerenteB@gmail', '20/05/2022', 'Nivel B', 2)


controlador_usuario.inserirCliente(usuarioA)
controlador_usuario.inserirCliente(usuarioB)

controlador_usuario.inserirGerente(gerenteA)
controlador_usuario.inserirGerente(gerenteB)


jogoA = controlador_jogo.criarJogo('Acao', 1, 'GTA V', 'Jogo de ação', desenvolvedoraA, '17/09/2013', 200, 'Windows 7 64 Bit Service Pack 1, Windows 8 64 Bit, Windows 8.1 64 Bit', 1.5, 'Muito bom', True)
jogoB = controlador_jogo.criarJogo('Acao', 2, 'GTA IV', 'Jogo de ação', desenvolvedoraA, '29/04/2008', 100, 'Windows Vista - Service Pack 1 / Windows XP - Service Pack 3', 5, 'Muito bom', True)
jogoC = controlador_jogo.criarJogo('Acao', 3, 'GTA San Andreas', 'Jogo de ação', desenvolvedoraA, '07/06/2005', 50, 'Windows 2000 Service Pack 1 ou superior', 3, 'Muito bom', True)
jogoD = controlador_jogo.criarJogo('Acao', 4, 'GTA Vice City', 'Jogo de ação', desenvolvedoraA, '13/05/2003', 30, 'Windows 98/98SE/ME/2000/XP', 5, 'Muito bom', True)
jogoE = controlador_jogo.criarJogo('Acao', 5, 'GTA III', 'Jogo de ação', desenvolvedoraA, '20/05/2002', 20, 'Windows 98/98SE/ME/2000/XP', 5, 'Muito bom', True)
jogoF = controlador_jogo.criarJogo('Acao', 6, 'GTA 2', 'Jogo de ação', desenvolvedoraA, '22/10/1999', 10, 'Windows 95/98/ME/2000/XP', 5, 'Muito bom', True)
jogoG = controlador_jogo.criarJogo('Acao', 7, 'GTA', 'Jogo de ação', desenvolvedoraA, '21/10/1997', 5, 'Windows 95/98/ME/2000/XP', 0.1, 'Muito bom', True)
jogoH = controlador_jogo.criarJogo('Acao', 8, 'GTA London 1969', 'Jogo de ação', desenvolvedoraA, '31/03/1999', 5, 'Windows 95/98/ME/2000/XP', 100, 'Muito bom', True)
jogoI = controlador_jogo.criarJogo('Acao', 9, 'GTA London 1961', 'Jogo de ação', desenvolvedoraA, '01/06/1999', 5, 'Windows 95/98/ME/2000/XP', 50, 'Muito bom', True)


controlador_jogo.inserirJogo(jogoA)
controlador_jogo.inserirJogo(jogoB)
controlador_jogo.inserirJogo(jogoC)
controlador_jogo.inserirJogo(jogoD)
controlador_jogo.inserirJogo(jogoE)
controlador_jogo.inserirJogo(jogoF)
controlador_jogo.inserirJogo(jogoG)
controlador_jogo.inserirJogo(jogoH)
controlador_jogo.inserirJogo(jogoI)



controlador_vendas = ControladorVendas.ControladorVendas(sistema)

itemVendaA = controlador_vendas.criarItemVenda(1, 1, 200, 1)
itemVendaB = controlador_vendas.criarItemVenda(2, 2, 100, 1)
itemVendaC = controlador_vendas.criarItemVenda(3, 3, 50, 1)


controlador_vendas.inserirItemVenda(itemVendaA)
controlador_vendas.inserirItemVenda(itemVendaB)
controlador_vendas.inserirItemVenda(itemVendaC)

vendaA = controlador_vendas.criarVenda(1, usuarioA, gerenteA, '20/05/2021', '20/05/2021', itemVendaA, False, 200, 200, pagamentoA, transportadoraA)
vendaB = controlador_vendas.criarVenda(2, usuarioB, gerenteB, '20/05/2021', '20/05/2021', itemVendaB, False, 100, 100, pagamentoB, transportadoraB)
vendaC = controlador_vendas.criarVenda(3, usuarioB, gerenteB, '20/05/2021', '20/05/2021', itemVendaC, False, 100, 100, pagamentoB, transportadoraB)


controlador_vendas.inserirVenda(vendaA)
controlador_vendas.inserirVenda(vendaB)
controlador_vendas.inserirVenda(vendaC)


controlador_relatorios = ControladorRelatorios.ControladorRelatorios(sistema)

#controlador_relatorios.listarDesenvolvedorasMaisJogosVendidos()

#controlador_relatorios.listarDesenvolvedorasMaisLucro()
#lucro = controlador_relatorios.listarVendasLucroDesenvolvedora(5, desenvolvedoraA.nome)

#print(controlador_relatorios.listarTransportadoras())
#print(controlador_relatorios.listarGerentes())
#print(controlador_relatorios.listarClientes())
#print(controlador_relatorios.listarClientesEpicos())
#print(controlador_relatorios.listarDezClientesMaiorNivel())
#print(controlador_relatorios.listarHistoricoVendasCliente(usuarioA.codigo))
#print(controlador_relatorios.todasVendas())
#print(controlador_relatorios.listarVendasLucroMes(5))
#print(controlador_relatorios.listarJogoPorAvaliacao('B'))
#print(controlador_relatorios.listarJogosMaisCaros())
#print(controlador_relatorios.listarJogosMaisBaratos())
#jogos = controlador_relatorios.listarJogos(Jogo.Jogo)
