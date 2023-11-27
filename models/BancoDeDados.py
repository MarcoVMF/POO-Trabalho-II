import sqlite3
from datetime import datetime

from models import Usuario, Transportadora, Desenvolvedora, Jogo, Venda, ItemVenda, Pagamento

class BancoDeDados:
    def __init__(self):
        self._conexao = sqlite3.connect('bancoDeDados.db')
        self._cursor = self._conexao.cursor()
        self._criarTabelas()

    def _criarTabelas(self):
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS clientes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento TEXT, endereco TEXT, cep TEXT, email TEXT, dataCadastro TEXT, nivel INTEGER, clienteEpico INTEGER, pagamento INTEGER, pagamentoTipo TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS gerentes (codigo INTEGER PRIMARY KEY, nome TEXT,cpf TEXT, rg TEXT, dataNascimento TEXT, endereco TEXT, cep TEXT, email TEXT, salario INTEGER, pis INTEGER, dataAdmissao TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS transportadoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, telefone TEXT, endereco TEXT, tempoEntrega INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS desenvolvedoras (codigo INTEGER PRIMARY KEY, cnpj TEXT, nome TEXT, email TEXT, site TEXT, redeSocial TEXT, endereco TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS jogos (codigo INTEGER PRIMARY KEY, nome TEXT, descricao TEXT, desenvolvedora INTEGER, dataLancamento TEXT, valor INTEGER, requisitosMinimos TEXT, avaliacao INTEGER, comentario TEXT, disponivel INTEGER, tipo TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS itensVendas (codigo INTEGER PRIMARY KEY, codigoProduto INTEGER, valor INTEGER, quantidade INTEGER)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS boletos (codigo INTEGER PRIMARY KEY, numero TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS cartaoCreditos (codigo INTEGER PRIMARY KEY, nome TEXT, bandeira TEXT, numero TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS PIXs (codigo INTEGER PRIMARY KEY, codigoPIX TEXT)')
        self._cursor.execute(
            'CREATE TABLE IF NOT EXISTS vendas (codigo INTEGER PRIMARY KEY, cliente INTEGER, gerente INTEGER, dataVenda TEXT, dataEntrega TEXT, itensVenda TEXT, possuiItensFisico INTEGER, valorTotal INTEGER, valorComDesconto INTEGER, formaPagamento INTEGER, tipoPagamento TEXT,transportadora INTEGER)')

    def inserirFormaPagamento(self, formaPagamento):
        if type(formaPagamento).__name__ == 'Boleto':
            self._cursor.execute('INSERT INTO boletos (codigo, numero) VALUES (?, ?) ON CONFLICT(codigo) DO NOTHING',
                                 (formaPagamento.codigo, formaPagamento.numero))
        elif type(formaPagamento).__name__ == 'CartaoCredito':
            self._cursor.execute('INSERT INTO cartaoCreditos (codigo, nome, bandeira, numero) VALUES (?, ?, ?, ?) ON CONFLICT(codigo) DO NOTHING',
                                 (formaPagamento.codigo, formaPagamento.nome, formaPagamento.bandeira, formaPagamento.numero))
        elif type(formaPagamento).__name__ == 'PIX':
            self._cursor.execute('INSERT INTO PIXs (codigo, codigoPIX) VALUES (?, ?) ON CONFLICT(codigo) DO NOTHING',
                                 (formaPagamento.codigo, formaPagamento.codigoPIX))
        self._conexao.commit()

    def recuperarFormaPagamento(self, codigo, pagamentoTipo):
        codigo = str(codigo)
        if pagamentoTipo == 'Boleto':
            self._cursor.execute('SELECT * FROM boletos WHERE codigo = ?', (codigo))
            conteudo = self._cursor.fetchone()
            formaPagamento = Pagamento.Boleto(conteudo[0], conteudo[1])
        elif pagamentoTipo == 'CartaoCredito':
            self._cursor.execute('SELECT * FROM cartaoCreditos WHERE codigo = ?', (codigo))
            conteudo = self._cursor.fetchone()
            formaPagamento = Pagamento.CartaoCredito(conteudo[0], conteudo[1], conteudo[2], conteudo[3])
        elif pagamentoTipo == 'PIX':
            self._cursor.execute('SELECT * FROM PIXs WHERE codigo = ?', (codigo))
            conteudo = self._cursor.fetchone()
            formaPagamento = Pagamento.Pix(conteudo[0], conteudo[1])
        return formaPagamento

    def removerFormaPagamento(self, codigo, pagamentoTipo):
        if pagamentoTipo == 'Boleto':
            self._cursor.execute('DELETE FROM boletos WHERE codigo = ?', (codigo))
        elif pagamentoTipo == 'CartaoCredito':
            self._cursor.execute('DELETE FROM cartaoCreditos WHERE codigo = ?', (codigo))
        elif pagamentoTipo == 'PIX':
            self._cursor.execute('DELETE FROM PIXs WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirCliente(self, cliente):
        self._cursor.execute(
            'INSERT INTO clientes (codigo,nome,cpf,rg,dataNascimento,endereco,cep,email,dataCadastro,nivel,clienteEpico, pagamento, pagamentoTipo) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(codigo) DO NOTHING',
            (cliente.codigo, cliente.nome, cliente.cpf, cliente.rg, cliente.dataNascimento, cliente.endereco, cliente.cep,
             cliente.email, cliente.dataCadastro, cliente.nivel, cliente.clienteEpico, cliente.pagamento.codigo, type(cliente.pagamento).__name__))
        self.inserirFormaPagamento(cliente.pagamento)
        self._conexao.commit()

    #Retorna uma tupla com o cliente
    def recuperarCliente(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('SELECT * FROM clientes WHERE codigo = ?', (codigo,))
        conteudo = self._cursor.fetchone()
        pagamento = self.recuperarFormaPagamento(conteudo[11], conteudo[12])
        cliente = Usuario.Cliente(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], pagamento, conteudo[11])
        return cliente

    #Retorna uma array de tuplas com todos os clientes
    def recuperarClientes(self):
        self._cursor.execute('SELECT * FROM clientes')
        clientes = []
        conteudos =  self._cursor.fetchall()
        for conteudo in conteudos:
            pagamento = self.recuperarFormaPagamento(conteudo[11], conteudo[12])
            cliente = Usuario.Cliente(conteudo[0], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10], pagamento, conteudo[12])
            clientes.append(cliente)
        return clientes

    def removerCliente(self, codigo):
        self._cursor.execute('DELETE FROM clientes WHERE codigo = ?', (codigo,))
        self._conexao.commit()

    def inserirGerente(self, gerente):
        self._cursor.execute(
            'INSERT INTO gerentes (codigo, nome,cpf,rg,dataNascimento,endereco,cep,email,salario,pis,dataAdmissao) VALUES (?,?,?,?,?,?,?,?,?,?,?) ON CONFLICT(codigo) DO NOTHING',
            (gerente.codigo, gerente.nome, gerente.cpf, gerente.rg, gerente.dataNascimento, gerente.endereco, gerente.cep,
             gerente.email, gerente.salario, gerente.pis, gerente.dataAdmissao))
        self._conexao.commit()

    def recuperarGerente(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('SELECT * FROM gerentes WHERE codigo = ?', (codigo,))
        conteudo = self._cursor.fetchone()
        gerente = Usuario.Gerente(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
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
            'INSERT INTO transportadoras (codigo, cnpj, nome, email, telefone, endereco, tempoEntrega) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT(codigo) DO NOTHING',
            (transportadora.codigo, transportadora.cnpj, transportadora.nome, transportadora.email, transportadora.telefone, transportadora.endereco, transportadora.tempoEntrega)
        )
        self._conexao.commit()

    def recuperarTrasportadora(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('SELECT * FROM transportadoras WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        transportadora = Transportadora.Transportadora(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6])
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
        codigo = str(codigo)
        self._cursor.execute('DELETE FROM transportadoras WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirDesenvolvedora(self, desenvolvedora):
        self._cursor.execute(
            'INSERT INTO desenvolvedoras (codigo, cnpj, nome, email, site, redeSocial, endereco) VALUES (?, ?, ?, ?, ?, ?, ?) ON CONFLICT(codigo) DO NOTHING',
            (desenvolvedora.codigo, desenvolvedora.cnpj, desenvolvedora.nome, desenvolvedora.email, desenvolvedora.site,
             desenvolvedora.redeSocial, desenvolvedora.endereco))
        self._conexao.commit()

    def recuperarDesenvolvedora(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('SELECT * FROM desenvolvedoras WHERE codigo = ?', (codigo))
        conteudo = self._cursor.fetchone()
        if conteudo is not None:
            desenvolvedora = Desenvolvedora.Desenvolvedora(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6])
            return desenvolvedora
        else:
            return None

    def recuperarDesenvolvedoras(self):
        self._cursor.execute('SELECT * FROM desenvolvedoras')
        conteudos =  self._cursor.fetchall()
        desenvolvedoras = []
        for conteudo in conteudos:
            desenvolvedora = Desenvolvedora.Desenvolvedora(conteudo[0], conteudo[1], conteudo[2], conteudo[3], conteudo[4], conteudo[5], conteudo[6])
            desenvolvedoras.append(desenvolvedora)
        return desenvolvedoras

    def removerDesenvolvedora(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('DELETE FROM desenvolvedoras WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirJogo(self, jogo):
        if not self.codigoExistente(jogo.codigo):
            self._cursor.execute('INSERT INTO jogos (codigo, nome, descricao, desenvolvedora, dataLancamento, valor, requisitosMinimos, avaliacao, comentario, disponivel, tipo) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ',
                                 (jogo.codigo, jogo.nome, jogo.descricao, jogo.desenvolvedora.codigo, jogo.dataLancamento, jogo.valor, jogo.requisitosMinimos, jogo.avaliacao, jogo.comentario, jogo.disponivel, jogo.tipo))
            self._conexao.commit()
        else:
            pass

    def codigoExistente(self, codigo):
        self._cursor.execute('SELECT COUNT(*) FROM jogos WHERE codigo = ?', (codigo,))
        return self._cursor.fetchone()[0] > 0

    def recuperarJogo(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('SELECT * FROM jogos WHERE codigo = ?', (codigo))
        conteudo = self._cursor.fetchone()
        data_objeto = datetime.strptime(conteudo[4], '%Y-%m-%d %H:%M:%S')
        data_formatada = data_objeto.strftime('%d/%m/%Y')
        desenvolvedora = self.recuperarDesenvolvedora(conteudo[3])
        if conteudo[10] == 'Acao':
            jogo = Jogo.Acao(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        elif conteudo[10] == 'Aventura':
            jogo = Jogo.Aventura(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        elif conteudo[10] == 'Corrida':
            jogo = Jogo.Corrida(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        elif conteudo[10] == 'Esporte':
            jogo = Jogo.Esporte(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
        elif conteudo[10] == 'RPG':
            jogo = Jogo.RPG(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])

        return jogo


    def recuperarJogos(self):
        self._cursor.execute('SELECT * FROM jogos')
        conteudos =  self._cursor.fetchall()
        jogos = []
        for conteudo in conteudos:
            data_objeto = datetime.strptime(conteudo[4], '%Y-%m-%d %H:%M:%S')
            data_formatada = data_objeto.strftime('%d/%m/%Y')

            desenvolvedora = self.recuperarDesenvolvedora(conteudo[3])
            if conteudo[10] == 'Acao':
                jogo = Jogo.Acao(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Aventura':
                jogo = Jogo.Aventura(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Corrida':
                jogo = Jogo.Corrida(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'Esporte':
                jogo = Jogo.Esporte(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)
            elif conteudo[10] == 'RPG':
                jogo = Jogo.RPG(conteudo[0], conteudo[1], conteudo[2], desenvolvedora, data_formatada, conteudo[5], conteudo[6], conteudo[7], conteudo[8], conteudo[9], conteudo[10])
                jogos.append(jogo)

        return jogos

    def removerJogo(self, codigo):
        codigo = str(codigo)
        self._cursor.execute('DELETE FROM jogos WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirItemVenda(self, itemVenda):

        self._cursor.execute('INSERT INTO itensVendas (codigo, codigoProduto, valor, quantidade) VALUES (?, ?, ?, ?) ON CONFLICT(codigo) DO NOTHING',
                             (itemVenda.codigo, itemVenda.codigoProduto, itemVenda.valor, itemVenda.quantidade))
        self._conexao.commit()

    def recuperarItemVenda(self, codigo):
        self._cursor.execute('SELECT * FROM itensVendas WHERE codigo = ?', (codigo))
        conteudo =  self._cursor.fetchone()
        produto = self.recuperarJogo(conteudo[1])
        itemVenda = ItemVenda.ItemVenda(conteudo[0], produto, conteudo[2], conteudo[3])
        return itemVenda

    def recuperarItensVendas(self):
        self._cursor.execute('SELECT * FROM itensVendas')
        conteudos =  self._cursor.fetchall()
        itensVenda = []
        for conteudo in conteudos:
            produto = self.recuperarJogo(conteudo[1])
            itemVenda = ItemVenda.ItemVenda(conteudo[0], produto, conteudo[2], conteudo[3])
            itensVenda.append(itemVenda)
        return itensVenda

    def removerItemVenda(self, codigo):
        self._cursor.execute('DELETE FROM itensVendas WHERE codigo = ?', (codigo))
        self._conexao.commit()

    def inserirVenda(self, venda):
        itensVenda = venda.itensVenda
        itensVendaString = ','.join(str(item.codigo) for item in itensVenda)

        self._cursor.execute(
            'INSERT INTO vendas (codigo, cliente, gerente, dataVenda, dataEntrega, itensVenda, possuiItensFisico, valorTotal, valorComDesconto, formaPagamento, transportadora) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?) ON CONFLICT(codigo) DO NOTHING',
            (venda.codigo, venda.cliente.codigo, venda.gerente.codigo, venda.dataVenda, venda.dataEntrega,
             itensVendaString, venda.possuiItensFisico, venda.valorTotal, venda.valorComDesconto,
             venda.formaPagamento.codigo, type(venda.formaPagamento).__name__, venda.transportadora.codigo))
        self._conexao.commit()

    def recuperarVenda(self, codigo):
        self._cursor.execute('SELECT * FROM vendas WHERE codigo = ?', (codigo))
        conteudo = self._cursor.fetchone()
        cliente = self.recuperarCliente(conteudo[1])
        gerente = self.recuperarGerente(conteudo[2])
        itensVenda = []
        for carac in conteudo[5]:
            itemVenda = self.recuperarItemVenda(int(carac))
            itensVenda.append(itemVenda)
        formaPagamento = self.recuperarFormaPagamento(conteudo[9], conteudo[10])
        transportadora = self.recuperarTrasportadora(conteudo[11])
        venda = Venda.Venda(conteudo[0], cliente, gerente, conteudo[3], conteudo[4], itensVenda, conteudo[6], conteudo[7], conteudo[8], formaPagamento, transportadora)
        return venda

    def recuperarVendas(self):
        self._cursor.execute('SELECT * FROM vendas')
        conteudos =  self._cursor.fetchall()
        vendas = []
        for conteudo in conteudos:
            venda = self.recuperarVenda(conteudo[0])
            vendas.append(venda)
        return vendas

    def removerVenda(self, codigo):
        self._cursor.execute('DELETE FROM vendas WHERE codigo = ?', (codigo))
        self.removerItemVenda(codigo)
        self._conexao.commit()