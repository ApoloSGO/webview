import flet as ft

def main(pagina):
    titulo = ft.Text("hashzap")
    titulo_janela = ft.Text("Bem vindo")



    
    campo_nome_usuario = ft.TextField(label="escreva seu nome no chat")
    botao_entrar = ft.ElevatedButton("entrar no chat")

    chat = ft.Column()

    def enviar_mensagem(evento):
        texto_mensagem = campo_mensagem.value

        nome_usuario = campo_mensagem.value
        text_chat = ft.Text(f"{nome_usuario}:{texto_mensagem}")
        chat.controls.append(text_chat)
        campo_mensagem.value = ""
        pagina.update()

    def main(pagina):

    linha_mensagem = ft.Row([campo_mensagem, botao_enviar_mensagem])
    def entrar_chat(evento):
        pagina.remove(titulo)
        pagina.remove(botao_iniciar)
        janela.open = False
        pagina.add(chat)
        pagina.add(linha_mensagem) 
        pagina.update()

        campo_mensagem = ft.TextField(label="Escreva a mensagem", on_submit=enviar_mensagem)
        botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
        janela = ft.AlertDialog(title = titulo_janela,
                            content= campo_nome_usuario,
                            actions=[botao_entrar])    
    
    
    def iniciar_chat(evento):
        pagina.dialog = janela
        janela.open = True
        pagina.update()
   
    botao_iniciar = ft.ElevatedButton("iniciar chat",on_click=iniciar_chat)

    pagina.add(titulo)
    pagina.add(botao_iniciar)
    pagina.add(janela)
ft.app(main)
