import requests
from tkinter import *

#passo a passo para criar tela que executa funcoes:
#from tkinter import *
#colocar o codigo que vc deseja executar dentro de uma ou mais funcoes
#criar uma janela vazia
#ir adicionando os elementos
#modificar a aparencia da janela se quiser
#transformar o codigo em um arquivo executavel

def pegar_cotacoes():
    requisicao = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")

    requisicao_dic = requisicao.json()

    cotacao_dolar = requisicao_dic['USDBRL']['bid']
    cotacao_euro = requisicao_dic['EURBRL']['bid']
    cotacao_btc = requisicao_dic['BTCBRL']['bid']

    texto_cotacoes['text'] = f'''
    Dólar: {cotacao_dolar}
    Euro: {cotacao_euro}
    BTC: {cotacao_btc}'''


#criar janela principal
janela = Tk() # cria a janela
janela.title("Cotação atual das moedas")
#janela.geometry("300x300") #se quiser mudar o tamanho da janela

#incluir elementos na janela
texto_orientacao = Label(janela, text="Clique no botão para ver as cotações das moedas")
texto_orientacao.grid(column=0, row=0, padx = 10, pady=10)

botao = Button(janela, text="Buscar cotações", command=pegar_cotacoes) #sem parenteses em pegar_cotacoes para ele executar a funcao somente quando clicar no botao
botao.grid(column=0, row=1, padx = 10, pady=10)

texto_cotacoes = Label(janela, text="")
texto_cotacoes.grid(column=0, row=2, padx = 10, pady=10)


janela.mainloop() # mantém a janela exibida
