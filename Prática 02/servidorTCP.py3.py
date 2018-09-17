# UNIVERSIDADE FEDERAL DO RIO GRANDE DO NORTE
# DEPARTAMENTO DE ENGENHARIA DE COMPUTACAO E AUTOMACAO
# DISCIPLINA REDES DE COMPUTADORES (DCA0113)
# AUTOR: PROF. CARLOS M D VIEGAS (viegas 'at' dca.ufrn.br)
#
# SCRIPT: Servidor de sockets TCP modificado para receber texto minusculo do cliente enviar resposta em maiuscula
#

# importacao das bibliotecas
from socket import * # sockets


def getArquivo():
  f = open('arquivo.txt')
  return f.read()

# definicao das variaveis
serverName = '' # ip do servidor (em branco)
serverPort = 12000 # porta a se conectar
serverSocket = socket(AF_INET,SOCK_STREAM) # criacao do socket TCP
serverSocket.bind((serverName,serverPort)) # bind do ip do servidor com a porta
serverSocket.listen(1) # socket pronto para 'ouvir' conexoes
print ('Servidor TCP esperando conexoes na porta %d ...' % (serverPort))

while 1:
  connectionSocket, addr = serverSocket.accept() # aceita as conexoes dos clientes
  sentence = connectionSocket.recv(1024) # recebe dados do cliente
  sentence = sentence.decode('utf-8')
  capitalizedSentence = sentence.upper() # converte em letras maiusculas
  if(capitalizedSentence=="OBTER ARQUIVO.TXT"):
    connectionSocket.send(str.encode(getArquivo())) # envia para o cliente o texto transformado
  else:
    connectionSocket.send(str.encode("Codigo inválido"))
  connectionSocket.close() # encerra o socket com o cliente
serverSocket.close() # encerra o socket do servidor
