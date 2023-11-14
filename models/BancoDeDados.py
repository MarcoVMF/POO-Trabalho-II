import sqlite3


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
            'INSERT INTO clientes (nome,cpf,rg,dataNascimento,endereco,cep,email,dataCadastro,nivel,clienteEpico) VALUES (?,?,?,?,?,?,?,?,?,?)',
            (cliente.nome, cliente.cpf, cliente.rg, cliente.dataNascimento, cliente.endereco, cliente.cep,
             cliente.email, cliente.dataCadastro, cliente.nivel, cliente.clienteEpico))
        self._conexao.commit()

    #Retorna uma tupla com o cliente
    def recuperarCliente(self, codigo):
        self._cursor.execute('SELECT * FROM clientes WHERE codigo = ?', (codigo,))
        return self._cursor.fetchone()

    #Retorna uma array de tuplas com todos os clientes
    def recuperarClientes(self):
        self._cursor.execute('SELECT * FROM clientes')
        return self._cursor.fetchall()

    def removerCliente(self, codigo):
        self._cursor.execute('DELETE FROM clientes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirGerente(self, gerente):
        self._cursor.execute(
            'INSERT INTO gerentes (nome,cpf,rg,dataNascimento,endereco,cep,email,salario,pis,dataAdmissao) VALUES (?,?,?,?,?,?,?,?,?,?)',
            (gerente.nome, gerente.cpf, gerente.rg, gerente.dataNascimento, gerente.endereco, gerente.cep,
             gerente.email, gerente.salario, gerente.pis, gerente.dataAdmissao))
        self._conexao.commit()

    def recuperarGerente(self, codigo):
        self._cursor.execute('SELECT * FROM gerentes WHERE codigo = ?', (codigo,))
        return self._cursor.fetchone()

    def recuperarGerentes(self):
        self._cursor.execute('SELECT * FROM gerentes')
        return self._cursor.fetchall()

    def removerGerente(self, codigo):
        self._cursor.execute('DELETE FROM gerentes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirTransportadora(self, transportadora):
        self._cursor.execute(
            'INSERT INTO transportadora (cnpj, nome, email, telefone, enderco, tempoEntrega) VALUES (? ? ? ? ? ?)',
            (transportadora.cnpj, transportadora.nome, transportadora.email, transportadora.telefone, transportadora.endereco, transportadora.tempoEntrega)
        )
        self._conexao.commit()

    def recuperarTrasportadora(self, codigo):
        self._cursor.execute('SELECT * FROM transportadora WHERE codigo = ?', (codigo))
        return self._cursor.fetchone()

    def recuperarTransportadoras(self):
        self._cursor.execute('SELECT * FROM transportadora')
        return self._cursor.fetchall()

    def removerTransportadora(self, codigo):
        self._cursor.execute('DELETE FROM transportadora WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirDesenvolvedora(self, desenvolvedora):
        self._cursor.execute('INSERT INTO desenvolvedora (cnpj, nome, email, site, redeSocial, endereco) VALUES (? ? ? ? ? ?)',
                             (desenvolvedora.cnpj, desenvolvedora.nome, desenvolvedora.email, desenvolvedora.site, desenvolvedora.redeSocial, desenvolvedora.endereco))
        self._conexao.commit()

    def recuperarDesenvolvedora(self, codigo):
        self._cursor.execute('SELECT * FROM desenvolvedora WHERE codigo = ?', (codigo))
        return self._cursor.fetchone()

    def recuperarDesenvolvedoras(self):
        self._cursor.execute('SELECT * FROM desenvolvedora')
        return self._cursor.fetchall()

    def removerDesenvolvedora(self, codigo):
        self._cursor.execute('DELETE FROM desenvolvedora WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirJogo(self, jogo):
        self._cursor.execute('INSERT INTO jogo (nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel) VALUES (? ? ? ? ? ? ? ? ?)',
                             (jogo.nome, jogo.descricao, jogo.desenvolvedora, jogo.dataLancamento, jogo.valor, jogo.requisitosMinimos, jogo.avaliacao, jogo.comentario, jogo.disponivel))
        self._conexao.commit()

    def recuperarJogo(self, codigo):
        self._cursor.execute('SELECT * FROM jogo WHERE codigo = ?', (codigo))
        return self._cursor.fetchone()

    def recuperarJogos(self):
        self._cursor.execute('SELECT * FROM jogo')
        return self._cursor.fetchall()

    def removerJogo(self, codigo):
        self._cursor.execute('DELETE FROM jogo WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirVenda(self, venda):
        self._cursor.execute('INSERT INTO venda (cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora) VALUES (? ? ? ? ? ? ? ? ? ?)',
                             (venda.cliente, venda.gerente, venda.dataVenda, venda.dataEntrega, venda.itensVenda, venda.possuiItensFisico, venda.valorTotal, venda.valorComDesconto, venda.formaPagamento, venda.transportadora))
        self._conexao.commit()

    def recuperarVenda(self, codigo):
        self._cursor.execute('SELECT * FROM venda WHERE codigo = ?', (codigo))
        return self._cursor.fetchone()

    def recuperarVendas(self):
        self._cursor.execute('SELECT * FROM venda')
        return self._cursor.fetchall()

    def removerVenda(self, codigo):
        self._cursor.execute('DELETE FROM venda WHERE codigo = ?', (codigo))
        self._conexao.commit()