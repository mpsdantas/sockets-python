# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets UDP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets
import time

def getData():
    return str.encode(time.ctime())
    
# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET, SOCK_DGRAM) # criacao do socket UDP
serverSocket.bind((serverName, serverPort)) # bind do ip do servidor com a porta
print ('Servidor UDP esperando conexoes na porta %d ...' % (serverPort))

while 1:
    message, clientAddress = serverSocket.recvfrom(2048) # recebe do cliente
    message = message.decode('utf-8')
    modifiedMessage = message.upper() # converte em letras maiusculas
    
    dataAtual = getData()

    if(modifiedMessage=="DATA"):
        serverSocket.sendto(dataAtual, clientAddress)
    else:
        serverSocket.sendto(str.encode("COMANDO NÃO ACEITO"), clientAddress)  

# envia a resposta para o cliente
serverSocket.close() # encerra o socket do servidor
