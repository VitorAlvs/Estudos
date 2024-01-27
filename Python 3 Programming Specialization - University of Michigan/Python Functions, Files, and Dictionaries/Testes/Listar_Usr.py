import os
import csv

# Muda o diretório de trabalho atual para o diretório do script
os.chdir(os.path.dirname(os.path.abspath(__file__)))

#Abrir doc
with open("Usuários.csv", "r", encoding="utf-16") as doc:
    #Ler doc
    read_doc = doc.read()
    #Dividir as linhas em lista
    split = read_doc.split("\n")
    #Definir cabeçalho
    header = split[0].split(",")
    header = header[0], header[2]
    #Definir conteúdo
    content = split[1:]
    #Todos os usuários
    users = []
    #Todos usuários ativos/habilitados que não são BR-iT
    active_usr = []
    quant_active_usr = 0
    #Lista de usuários BR-iT
    brit_Usr = {'aluvizeto', 'br-itsoftware.com.br\aluvizeto',
                'cburanelo', 'br-itsoftware.com.br\cburanelo', 
                'frodrigues', 'br-itsoftware.com.br\frodrigues', 
                'jvitoriano', 'br-itsoftware.com.br\jvitoriano', 
                'jsantos', 
                'dfaustino', 'br-itsoftware.com.br\dfaustino',
                'lsantos', 'br-itsoftware.com.br\lsantos', 
                'rmariano', 'br-itsoftware.com.br\rmariano', 
                'segoncalves', 'br-itsoftware.com.br\segoncalves',
                'userMSCD', 
                'M4LawAdmin', 'admin@br-itsoftware.com.br', 
                'csousa', 
                'M4Law Tester', 
                'kribeiro', 
                'pmotta', 'br-itsoftware.com.br\pmotta' }

    #Transformar string de dados de login em lista de dados de login
    for each in content:
        users.append(each.split(","))

    #Separar usuários active_usr
    for each in users:
        if '(conta de login desabilitada)' not in each[0]:
            if len(each) >= 4:
                desabilitado = len(each[3])
                conta_login = each[0]
                if desabilitado == 0 and conta_login not in brit_Usr:
                    Usr = each[0], each[2]
                    active_usr.append(Usr)
                    quant_active_usr += 1

with open('Listagem de Usuários Ativos.csv', 'w', newline='', encoding='utf-8') as csvfile:
    campos_head = list(header)
    writer = csv.DictWriter(csvfile, fieldnames = campos_head, delimiter=';')
    
    writer.writeheader()
    for each in active_usr:
        loginacc = str(each[0])
        name = str(each[1])
        writer.writerow({campos_head[0]: loginacc, campos_head[1]: name})
    

