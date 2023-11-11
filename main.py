import sqlite3

#Exemplo de uso do SQLITE3

con = sqlite3.connect("data_stock.db")
cur = con.cursor()

#Criar tabela
def createTable():
    cur.execute("CREATE TABLE stock(code, price, volume)")

#Adicionando valores na tabela
def addContent(data):
    cur.executemany("INSERT INTO stock VALUES(?, ?, ?)", data)
    con.commit()

#Deletando a tabela
def flushDataBase():
    cur.execute("DROP TABLE Student;")
    con.commit()

#Iterando pela tabela e printando valores
def printData():
    for row in cur.execute("SELECT * FROM stock ORDER BY price"):
        print(row)

data = [('APPL', 53.70, 200000),
        ('GOOGL', 94.64, 300000),
        ('MSFT', 272.13, 400000),
        ('AMZN', 340.20, 500000),
        ('FB', 296.22, 600000),
        ('TSLA', 910.68, 700000),
        ('NVDA', 225.20, 800000),
        ('AMD', 165.87, 900000),
        ('BABA', 129.20, 1000000)
        ]

createTable()
addContent(data)
printData()


cur.close()