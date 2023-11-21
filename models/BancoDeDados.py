import sqlite3
from datetime import datetime

from models import Usuario, Transportadora, Desenvolvedora, Jogo, Venda

class BancoDeDados:
    def __init__(self):
        self._conexao = sqlite3.connect('bancoDeDados.db')
        self._cursor = self._conexao.cursor()
        self._criarTabelas()

    def _criarTabelas(self):
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS clientes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento TEXT, endereco TEXT, cep TEXT, email TEXT, dataCadastro TEXT, nivel INTEGER, clienteEpico INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS gerentes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento TEXT, endereco TEXT, cep TEXT, email TEXT, salario INTEGER, pis INTEGER, dataAdmissao TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS transportadoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, telefone TEXT, endereco TEXT, tempoEntrega INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS desenvolvedoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, site TEXT, redeSocial TEXT, endereco TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS jogos (codigo INTEGER PRIMARY KEY, nome TEXT, descricao TEXT, desenvolvedora TEXT, dataLancamento TEXT, valor INTEGER, requisitosMinimos TEXT, avaliacao INTEGER, comentario TEXT, disponivel INTEGER, tipo TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS vendas (codigo INTEGER PRIMARY KEY, cliente INTEGER, gerente INTEGER, dataVenda TEXT, dataEntrega TEXT, itensVenda TEXT, possuiItensFisico INTEGER, valorTotal INTEGER, valorComDesconto INTEGER, formaPagamento TEXT, transportadora INTEGER)')

    def inserirCliente(self, cliente):
        self._cursor.execute(
            'INSERT INTO clientes (codigo,nome,cpf,rg,dataNascimento,endereco,cep,email,dataCadastro,nivel,clienteEpico) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
            (cliente.codigo, cliente.nome, cliente.cpf, cliente.rg, cliente.dataNascimento, cliente.endereco, cliente.cep,
             cliente.email, cliente.dataCadastro, cliente.nivel, cliente.clienteEpico))
        self._conexao.commit()

    #Retorna uma tupla com o cliente
    def recuperarCliente(self, codigo):
        self._cursor.execute('SELECT * FROM clientes WHERE codigo = ?', (codigo,))
        conteudo = self._cursor.fetchone()
        cliente = Usuario.Cliente(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10], conteudo[11])
        return cliente

    #Retorna uma array de tuplas com todos os clientes
    def recuperarClientes(self):
        self._cursor.execute('SELECT * FROM clientes')
        clientes = []
        conteudos =  self._cursor.fetchall()
        for conteudo in conteudos:
            cliente = Usuario.Cliente(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
            clientes.append(cliente)
        return clientes

    def removerCliente(self, codigo):
        self._cursor.execute('DELETE FROM clientes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirGerente(self, gerente):
        self._cursor.execute(
            'INSERT INTO gerentes (codigo, nome,cpf,rg,dataNascimento,endereco,cep,email,salario,pis,dataAdmissao) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
            (gerente.codigo, gerente.nome, gerente.cpf, gerente.rg, gerente.dataNascimento, gerente.endereco, gerente.cep,
             gerente.email, gerente.salario, gerente.pis, gerente.dataAdmissao))
        self._conexao.commit()

    def recuperarGerente(self, codigo):
        self._cursor.execute('SELECT * FROM gerentes WHERE codigo = ?', (codigo,))
        conteudo =  self._cursor.fetchone()
        gerente = Usuario.Gerente(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10], conteudo[11])
        return gerente

    def recuperarGerentes(self):
        self._cursor.execute('SELECT * FROM gerentes')
        conteudos =  self._cursor.fetchall()
        gerentes = []
        for conteudo in conteudos:
            gerente = Usuario.Gerente(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
            gerentes.append(gerente)
        return gerentes


    def removerGerente(self, codigo):
        self._cursor.execute('DELETE FROM gerentes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirTransportadora(self, transportadora):
        self._cursor.execute(
            'INSERT INTO transportadoras (codigo, cnpj, nome, email, telefone, enderco, tempoEntrega) VALUES (?, ?, ?, ?, ?, ?, ?)',
            (transportadora.codigo, transportadora.cnpj, transportadora.nome, transportadora.email, transportadora.telefone, transportadora.endereco, transportadora.tempoEntrega)
        )
        self._conexao.commit()

    def recuperarTrasportadora(self, codigo):
        self._cursor.execute('SELECT * FROM transportadoras WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        transportadora = Transportadora.Transportadora(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7])
        return transportadora

    def recuperarTransportadoras(self):
        self._cursor.execute('SELECT * FROM transportadoras')
        conteudos =  self._cursor.fetchall()
        transportadoras = []
        for conteudo in conteudos:
            transportadora = Transportadora.Transportadora(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6])
            transportadoras.append(transportadora)
        return transportadoras

    def removerTransportadora(self, codigo):
        self._cursor.execute('DELETE FROM transportadoras WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirDesenvolvedora(self, desenvolvedora):
        self._cursor.execute('INSERT INTO desenvolvedoras (codigo, cnpj, nome, email, site, redeSocial, endereco) VALUES (?, ?, ?, ?, ?, ?, ?)',
                             (desenvolvedora.codigo, desenvolvedora.cnpj, desenvolvedora.nome, desenvolvedora.email, desenvolvedora.site, desenvolvedora.redeSocial, desenvolvedora.endereco))
        self._conexao.commit()

    def recuperarDesenvolvedora(self, codigo):
        self._cursor.execute('SELECT * FROM desenvolvedoras WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        desenvolvedora = Desenvolvedora.Desenvolvedora(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7])
        return desenvolvedora

    def recuperarDesenvolvedoras(self):
        self._cursor.execute('SELECT * FROM desenvolvedoras')
        conteudos =  self._cursor.fetchall()
        desenvolvedoras = []
        for conteudo in conteudos:
            desenvolvedora = Desenvolvedora.Desenvolvedora(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6])
            desenvolvedoras.append(desenvolvedora)
        return desenvolvedoras

    def removerDesenvolvedora(self, codigo):
        self._cursor.execute('DELETE FROM desenvolvedoras WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirJogo(self, jogo):
        if not self.codigoExistente(jogo.codigo):
            self._cursor.execute('INSERT INTO jogos (codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                                 (jogo.codigo, jogo.nome, jogo.descricao, jogo.desenvolvedora, jogo.dataLancamento, jogo.valor, jogo.requisitosMinimos, jogo.avaliacao, jogo.comentario, jogo.disponivel, jogo.tipo))
            self._conexao.commit()
        else:
            pass

    def codigoExistente(self, codigo):
        self._cursor.execute('SELECT COUNT(*) FROM jogos WHERE codigo = ?', (codigo,))
        return self._cursor.fetchone()[0] > 0

    def recuperarJogo(self, codigo):
        self._cursor.execute('SELECT * FROM jogos WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        jogo = Jogo.Jogo(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        return jogo


    def recuperarJogos(self):
        self._cursor.execute('SELECT * FROM jogos')
        conteudos =  self._cursor.fetchall()
        jogos = []
        for conteudo in conteudos:
            data_objeto = datetime.strptime(conteudo[4], '%Y-%m-%d %H:%M:%S')
            data_formatada = data_objeto.strftime('%d/%m/%Y')
            if conteudo[10] == 'Acao':
                jogo = Jogo.Acao(conteudo[0], conteudo[1], conteudo[2], conteudo[3], data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Aventura':
                jogo = Jogo.Aventura(conteudo[0], conteudo[1], conteudo[2], conteudo[3], data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Corrida':
                jogo = Jogo.Corrida(conteudo[0], conteudo[1], conteudo[2], conteudo[3], data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Esporte':
                jogo = Jogo.Esporte(conteudo[0], conteudo[1], conteudo[2], conteudo[3], data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'RPG':
                jogo = Jogo.RPG(conteudo[0], conteudo[1], conteudo[2], conteudo[3], data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)

        return jogos

    def removerJogo(self, codigo):
        self._cursor.execute('DELETE FROM jogos WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirVenda(self, venda):
        self._cursor.execute('INSERT INTO vendas (codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
                             (venda.codigo, venda.cliente, venda.gerente, venda.dataVenda, venda.dataEntrega, venda.itensVenda, venda.possuiItensFisico, venda.valorTotal, venda.valorComDesconto, venda.formaPagamento, venda.transportadora))
        self._conexao.commit()

    def recuperarVenda(self, codigo):
        self._cursor.execute('SELECT * FROM vendas WHERE codigo = ?', (codigo))
        conteudo = self._cursor.fetchone()
        venda = Venda.Venda(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        return venda

    def recuperarVendas(self):
        self._cursor.execute('SELECT * FROM vendas')
        conteudos =  self._cursor.fetchall()
        vendas = []
        for conteudo in conteudos:
            venda = Venda.Venda(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
            vendas.append(venda)
        return vendas

    def removerVenda(self, codigo):
        self._cursor.execute('DELETE FROM vendas WHERE codigo = ?', (codigo))
        self._conexao.commit()