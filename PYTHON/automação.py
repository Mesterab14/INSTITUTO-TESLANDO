import email
import getpass
import smtplib
import requests

def obter_usuarios():
    todos_usuarios = []
    pagina = 1
    
    #olhar as páginas da API
    while pagina <= 2:
        url = "https://reqres.in/api/users?page=" + str(pagina)
        resposta = requests.get(url)
        dados = resposta.json()
        
        # Pega a lista de usuários da página e junta na lista principal
        usuarios_pagina = dados["data"]
        todos_usuarios = todos_usuarios + usuarios_pagina
        
        pagina = pagina + 1
        
    return todos_usuarios

def salvar_txt(usuarios):
    arquivo = open("usuarios.txt", "w", encoding="utf-8")
    
    for u in usuarios:
        linha = "\nID: " + str(u["id"]) + "\n - Nome: " + u["first_name"] + " " + u["last_name"] + "\n - Email: " + u["email"] + "\n"
        arquivo.write(linha)
        
    arquivo.close()

def enviar_email():
    while True:
        print("\nENVIO DO ANEXO POR EMAIL")
        meu_email = input("Digite o seu e-mail: ")
        
        #o getpass vai esconder a senha
        minha_senha = getpass.getpass("Digite sua senha: ")
        
        destinatario = input("Digite o e-mail do destinatário: ")

        mensagem_texto = input("Digite a mensagem que vai no corpo do e-mail: ")

        #corpo do email
        msg = email.message.EmailMessage()
        msg['Subject'] = "Anexo com Lista de Usuários com API"
        msg['From'] = meu_email
        msg['To'] = destinatario
        msg.set_content(mensagem_texto)

        #como vai ficar o arquivo txt
        arquivo = open("usuarios.txt", "rb")
        msg.add_attachment(arquivo.read(), maintype="text", subtype="plain", filename="Lista_de_usuarios.txt")
        arquivo.close()

        #conecta ao email para enviar
        print("Enviando e-mail...")
        
        try:
            servidor = smtplib.SMTP("smtp.gmail.com", 587)
            servidor.starttls()
            servidor.login(meu_email, minha_senha)
            servidor.send_message(msg)
            servidor.quit()
            print("O email foi enviado!")
            break  

        except smtplib.SMTPAuthenticationError:
            print("\nE-mail ou senha incorretos. Tente novamente.")
        except smtplib.SMTPRecipientsRefused:
            print("\nO e-mail do destinatário é inválido. Tente novamente.")
        except Exception as e:
            print(f"\nFalha ao enviar o e-mail: {e}. Tente novamente.")

usuarios = obter_usuarios()
salvar_txt(usuarios)
enviar_email()