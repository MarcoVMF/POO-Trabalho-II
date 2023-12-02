from models import BancoDeDados, SistemaJogosEletronicos
from views import view

bd = BancoDeDados.BancoDeDados()
sistema = SistemaJogosEletronicos.SistemaJogosEletronicos()

view.execucao(sistema)