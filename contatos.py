import requests
from bs4 import BeautifulSoup
from unidecode import unidecode #Para comparacao das Strings (sem acento)

def compare(search2, names, numbers):
    for j in range(len(names)):
        if(unidecode(search2.lower()) in unidecode(names[j].lower())):
            print(str(names[j]) +  str(numbers[j]))
    print('\n')



link = 'https://www.capitolio.mg.gov.br/portal/contato'
order = requests.get(link)
#print(requisicao.text)

bfs = BeautifulSoup(order.text, 'html.parser')

namelist = []
numberlist = []
asst = 0

for i in bfs.find_all('div', class_='tit_links'):
    namelist.insert(asst, i.string)
    asst+=1

for i in bfs.find_all('div', class_='botao_links_acesso'):
    numberlist.insert(asst, i.string)
    asst+=1

flag = True
while(flag):
    print('Selecione a opção desejada:')
    print('1 - Salvar Dados Capturados em um Arquivo')
    print('2 - Mostrar Todos os Contatos')
    print('3 - Pesquisar Contato')
    print('4 - Encerrar o Programa')

    inp = str(input()).strip()
    
    if(inp =='1'):
        arquivo = open('newcontacts.txt', 'w')
        for j in range(len(namelist)):
            arquivo.write(str(namelist[j]) +  str(numberlist[j]))
        arquivo.close()
    elif(inp == '2'):
        compare(' ', namelist, numberlist)
    elif(inp == '3'):
        search = str(input('Qual contato você procura? ')).strip()
        compare(search, namelist, numberlist)
    elif(inp == '4'):
        flag = False
    else:
        print('Numero Inválido')





