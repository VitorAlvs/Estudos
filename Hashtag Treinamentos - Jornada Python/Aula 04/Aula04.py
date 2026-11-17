#Título Hashzap
#Botão Iniciar Chat
    #PopUp
        #Bem vindo ao Hashzap
        #Escreva seu nome
        #Entrar no Chat
#Chat
    #Usuário entrou no chat
    #Mensagens do usuário
#Campo para enviar mensagem
#Botao de enviar

import flet as ft 

def main(pagina):
    texto = ft.Text("Hashzap")

    nome_usuario = ft.TextField(label="Seu nome")

    chat = ft.Column()

    def enviar_mensagem_tunel(informacoes):
        chat.controls.append(ft.Text(informacoes))
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)       
    
    def enviar_mensagem(evento):
        #colocar o nome do usr na msg
        texto_campo_mensagem = f"{nome_usuario.value}: {campo_mensagem.value}"
        pagina.pubsub.send_all(texto_campo_mensagem)
        #limpar campo msg
        campo_mensagem.value = ""
        pagina.update()

    campo_mensagem = ft.TextField(label="Escreva sua mensagem aqui", on_submit=enviar_mensagem)

    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)


    def entrar_chat(evento):
        #feche o popup
        popup.open = False
        #tirar o btn "iniciar chat" da tela
        pagina.remove(botao_iniciar)
        #adicionar o chat
        pagina.add(chat)
        #criar o campo de enviar msg
        #btn enviar msg
        linha_mensagem = ft.Row(
            [campo_mensagem, botao_enviar]
        )
        pagina.add(linha_mensagem)
        texto = f"{nome_usuario.value} entrou no chat"
        pagina.pubsub.send_all(texto)
        pagina.update()

    popup = ft.AlertDialog(
        open=False, 
        modal=True, 
        title=ft.Text("Bem vindo ao Hashzap"),
        content= nome_usuario,
        actions=[ft.ElevatedButton("Entrar", on_click=entrar_chat)]
        )

    def iniciar_chat(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()

    botao_iniciar = ft.ElevatedButton("Iniciar chat", on_click=iniciar_chat)

    pagina.add(texto)
    pagina.add(botao_iniciar)

ft.app(main, view=ft.WEB_BROWSER)