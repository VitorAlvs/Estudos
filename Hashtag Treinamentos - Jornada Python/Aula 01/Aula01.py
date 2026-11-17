#ENTRAR E CADASTRAR PRODUTOS NO SISTEMA

#Passo a passo do projeto

#~~Passo 1 - Entrar no sistema da empresa
    #https://dlp.hashtagtreinamentos.com/python/intensivao/login
link = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
#pyautogui - RPA - automação bot
#pip install autogui
import pyautogui 
import time
import pandas as pd

#clicar             -> pyautogui.click
#escrever           -> pyautogui.write
#apertar uma tecla  -> pyautogui.press
#apertar atalho     -> pyautogui.hotkey("","")// ex:pyautogui.hotkey("ctr","c")
#scroll             -> pyautogui.scroll(1000) - para cima // pyautogui.scroll(-1000) - para baixo

pyautogui.PAUSE = 0.5
    #a cada comando ele espera um segundo

#aperta windows (comand + barra de espaço)
pyautogui.press("win")
#digita o nome do programa
pyautogui.write("edge")
time.sleep(3)
#aperta enter
pyautogui.press("enter")
#digitar o link
pyautogui.write(link)
#aperta enter
pyautogui.press("enter")
#esperar 5 segundos
time.sleep(3)

#~~Passo 2 - Fazer login
pyautogui.click(x=2514, y=386) 
#digitar o email
pyautogui.write("login@gmail.com")
#passar para o campo de senha
pyautogui.press("tab")
#digitar a senha
pyautogui.write("Senha123@")
#clicar no botão entrar
pyautogui.press("enter")
time.sleep(3)

#~~Passo 3 - Importar a base de dados
produtos = r"C:\Users\JoãoVítorSantosBR-iT\Documents\GitHub\Estudos\Jornada Python - Hashtag Treinamentos\Aula 01\produtos.csv"

tabela = pd.read_csv(produtos)
print(tabela)

#~~Passo 4 - Cadastrar um produto
for linha in tabela.index:
        pyautogui.click(x=2404, y=266)

        #codigo
        codigo = tabela.loc[linha, "codigo"]
        pyautogui.write(codigo)
        pyautogui.press("tab")

        #marca
        marca = tabela.loc[linha, "marca"]
        pyautogui.write(marca)
        pyautogui.press("tab")

        #tipo
        tipo = tabela.loc[linha, "tipo"]
        pyautogui.write(tipo)
        pyautogui.press("tab")

        #categoria
        categoria = str(tabela.loc[linha, "categoria"])
        pyautogui.write(categoria)
        pyautogui.press("tab")

        #preço unitário
        preco = str(tabela.loc[linha, "preco_unitario"])
        pyautogui.write(preco)
        pyautogui.press("tab")

        #custo      
        custo = str(tabela.loc[linha, "custo"])
        pyautogui.write(custo)
        pyautogui.press("tab")

        #obs
        obs = tabela.loc[linha, "obs"]

        if not pd.isna(obs):
            pyautogui.write(obs)

        #enviar
        pyautogui.press("tab")
        pyautogui.press("enter")

        pyautogui.scroll(5000)

#~~Passo 5 - Repetir isso até acabar a base de dados