import requests
from bs4 import BeautifulSoup
from unidecode import unidecode #Para comparacao das Strings (sem acento)

def compare(search2, names, numbers):
    flag2 = True
    for j in range(len(names)):
        if(unidecode(search2.lower()) in unidecode(names[j].lower())):
            print(str(names[j]) +  str(numbers[j]))
            flag2 = False
    if(flag2):
        print('\nNada Encontrado')    



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
        print('\n')
        arquivo = open('newcontacts.txt', 'w')
        for j in range(len(namelist)):
            arquivo.write(str(namelist[j]) +  str(numberlist[j]))
        arquivo.close()
        print('Dados salvos em "newcontacts.txt"\n')
    elif(inp == '2'):
        print('\n')
        compare(' ', namelist, numberlist)
        print('\n')
    elif(inp == '3'):
        print('\n')
        search = str(input('Qual contato você procura? ')).strip()
        compare(search, namelist, numberlist)
        print('\n')
    elif(inp == '4'):
        print('\nFinalizando...\n')
        flag = False
    else:
        print('\nOpção Inválida\n')





