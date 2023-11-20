import sqlite3
import Venda, Usuario, Transportadora, Desenvolvedora, Jogo

class BancoDeDados:
    def __init__(self):
        self._conexao = sqlite3.connect('bancoDeDados.db')
        self._cursor = self._conexao.cursor()
        self._criarTabelas()

    def _criarTabelas(self):
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS clientes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento DATE, endereco TEXT, cep TEXT, email TEXT, dataCadastro DATE, nivel INTEGER, clienteEpico INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS gerentes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento DATE, endereco TEXT, cep TEXT, email TEXT, salario INTEGER, pis INTEGER, dataAdmissao DATE)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS transportadoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, telefone TEXT, endereco TEXT, tempoEntrega INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS desenvolvedoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, site TEXT, redeSocial TEXT, endereco TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS jogos (codigo INTEGER PRIMARY KEY, nome TEXT, descricao TEXT, desenvolvedora TEXT, dataLancamento DATE, valor INTEGER, requisitosMinimos TEXT, avaliacao INTEGER, comentario TEXT, disponivel INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS vendas (codigo INTEGER PRIMARY KEY, cliente INTEGER, gerente INTEGER, dataVenda DATE, dataEntrega DATE, itensVenda TEXT, possuiItensFisico INTEGER, valorTotal INTEGER, valorComDesconto INTEGER, formaPagamento TEXT, transportadora INTEGER)')

    def inserirCliente(self, cliente):
        self._cursor.execute(
            'INSERT INTO clientes (codigo,nome,cpf,rg,dataNascimento,endereco,cep,email,dataCadastro,nivel,clienteEpico) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
            (cliente.nome, cliente.cpf, cliente.rg, cliente.dataNascimento, cliente.endereco, cliente.cep,
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
        conteudo =  self._cursor.fetchall()
        for i in conteudo:
            cliente = Usuario.Cliente(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            clientes.append(cliente)
        return clientes

    def removerCliente(self, codigo):
        self._cursor.execute('DELETE FROM clientes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirGerente(self, gerente):
        self._cursor.execute(
            'INSERT INTO gerentes (codigo, nome,cpf,rg,dataNascimento,endereco,cep,email,salario,pis,dataAdmissao) VALUES (?,?,?,?,?,?,?,?,?,?,?)',
            (gerente.nome, gerente.cpf, gerente.rg, gerente.dataNascimento, gerente.endereco, gerente.cep,
             gerente.email, gerente.salario, gerente.pis, gerente.dataAdmissao))
        self._conexao.commit()

    def recuperarGerente(self, codigo):
        self._cursor.execute('SELECT * FROM gerentes WHERE codigo = ?', (codigo,))
        conteudo =  self._cursor.fetchone()
        gerente = Usuario.Gerente(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10], conteudo[11])
        return gerente

    def recuperarGerentes(self):
        self._cursor.execute('SELECT * FROM gerentes')
        conteudo =  self._cursor.fetchall()
        gerentes = []
        for i in conteudo:
            gerente = Usuario.Gerente(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9], i[10], i[11])
            gerentes.append(gerente)
        return gerentes


    def removerGerente(self, codigo):
        self._cursor.execute('DELETE FROM gerentes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirTransportadora(self, transportadora):
        self._cursor.execute(
            'INSERT INTO transportadora (codigo, cnpj, nome, email, telefone, enderco, tempoEntrega) VALUES (? ? ? ? ? ? ?)',
            (transportadora.cnpj, transportadora.nome, transportadora.email, transportadora.telefone, transportadora.endereco, transportadora.tempoEntrega)
        )
        self._conexao.commit()

    def recuperarTrasportadora(self, codigo):
        self._cursor.execute('SELECT * FROM transportadora WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        transportadora = Transportadora.Transportadora(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7])
        return transportadora

    def recuperarTransportadoras(self):
        self._cursor.execute('SELECT * FROM transportadora')
        conteudo =  self._cursor.fetchall()
        transportadoras = []
        for i in conteudo:
            transportadora = Transportadora.Transportadora(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            transportadoras.append(transportadora)
        return transportadoras

    def removerTransportadora(self, codigo):
        self._cursor.execute('DELETE FROM transportadora WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirDesenvolvedora(self, desenvolvedora):
        self._cursor.execute('INSERT INTO desenvolvedora (codigo, cnpj, nome, email, site, redeSocial, endereco) VALUES (? ? ? ? ? ? ?)',
                             (desenvolvedora.cnpj, desenvolvedora.nome, desenvolvedora.email, desenvolvedora.site, desenvolvedora.redeSocial, desenvolvedora.endereco))
        self._conexao.commit()

    def recuperarDesenvolvedora(self, codigo):
        self._cursor.execute('SELECT * FROM desenvolvedora WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        desenvolvedora = Desenvolvedora.Desenvolvedora(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7])
        return desenvolvedora

    def recuperarDesenvolvedoras(self):
        self._cursor.execute('SELECT * FROM desenvolvedora')
        conteudo =  self._cursor.fetchall()
        desenvolvedoras = []
        for i in conteudo:
            desenvolvedora = Desenvolvedora.Desenvolvedora(i[1], i[2], i[3], i[4], i[5], i[6], i[7])
            desenvolvedoras.append(desenvolvedora)
        return desenvolvedoras

    def removerDesenvolvedora(self, codigo):
        self._cursor.execute('DELETE FROM desenvolvedora WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirJogo(self, jogo):
        self._cursor.execute('INSERT INTO jogo (codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel) VALUES (? ? ? ? ? ? ? ? ? ?)',
                             (jogo.nome, jogo.descricao, jogo.desenvolvedora, jogo.dataLancamento, jogo.valor, jogo.requisitosMinimos, jogo.avaliacao, jogo.comentario, jogo.disponivel))
        self._conexao.commit()

    def recuperarJogo(self, codigo):
        self._cursor.execute('SELECT * FROM jogo WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        jogo = Jogo.Jogo(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        return jogo

    def recuperarJogos(self):
        self._cursor.execute('SELECT * FROM jogo')
        conteudo =  self._cursor.fetchall()
        jogos = []
        for i in conteudo:
            jogo = Jogo.Jogo(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
            jogos.append(jogo)
        return jogos

    def removerJogo(self, codigo):
        self._cursor.execute('DELETE FROM jogo WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirVenda(self, venda):
        self._cursor.execute('INSERT INTO venda (codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora) VALUES (? ? ? ? ? ? ? ? ? ? ?)',
                             (venda.cliente, venda.gerente, venda.dataVenda, venda.dataEntrega, venda.itensVenda, venda.possuiItensFisico, venda.valorTotal, venda.valorComDesconto, venda.formaPagamento, venda.transportadora))
        self._conexao.commit()

    def recuperarVenda(self, codigo):
        self._cursor.execute('SELECT * FROM venda WHERE codigo = ?', (codigo))
        conteudo = self._cursor.fetchone()
        venda = Venda.Venda(conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10], conteudo[11])
        return venda

    def recuperarVendas(self):
        self._cursor.execute('SELECT * FROM venda')
        conteudo =  self._cursor.fetchall()
        vendas = []
        for i in conteudo:
            venda = Venda.Venda(i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9])
            vendas.append(venda)
        return vendas

    def removerVenda(self, codigo):
        self._cursor.execute('DELETE FROM venda WHERE codigo = ?', (codigo))
        self._conexao.commit()