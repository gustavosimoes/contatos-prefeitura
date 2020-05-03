import requests
from bs4 import BeautifulSoup
from unidecode import unidecode #Para comparacao das Strings (sem acento)

def compare(search2, names, numbers):
    for j in range(len(names)):
        if(search2.lower() in unidecode(names[j].lower())):
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
    print('1 - Mostrar Todos os Contatos')
    print('2 - Pesquisar Contato')
    print('3 - Encerrar o Programa')

    inp = str(input()).strip()
    
    if(inp == '1'):
        compare(' ', namelist, numberlist)
    elif(inp == '2'):
        search = str(input('Qual contato você procura? ')).strip()
        compare(search, namelist, numberlist)
    elif(inp == '3'):
        flag = False
    else:
        print('Numero Inválido')





