#============================================================================#
#            RASPAGEM DE DADOS WEBSCREAPING - E-COMMERCE                     #
#============================================================================#

# BIBLIOTECA DO PROJETO
import re
import smtplib
from email.message import EmailMessage

# Construindo o projeto
class WebScreapingEcommerce:
    
    
    def start(self):
        self.menu()
        self.coletar_email_senha()
        self.conexao_email()
        self.envia_email()
    
    # Cabeçalho do projeto
    def menu(self):
        print('#========================================#')
        print('#    RASPAGEM DE DADOS SITE E-COMMERCE   #')
        print('#               PROJETO 01               #')
        print('#========================================#')
    
    # Nesta etapa serão solicitados o e-mail e senha do usuário
    # A senha será por conta que a nossa solução irá acessar o
    # e-mail e enviar o relatório em excel.
    def coletar_email_senha(self):
        print('Digite um email e senha válidos para receber o relatório.')
        self.email = input('Digite seu e-mail: ')
        self.senha = input('Digite sua senha: ')
        self.valida_email()
        print('E-mail e senha salvos!')
    
    # Nesta etapa, iremos realizar a validação de e-mail, pois
    # precisamso ter a certeza que o usuário da aplciação irá
    # irá digitar o seu e-mail corretamente. Caso Seja digitado 
    # email inválido a solução irá retornar desde o início até 
    # que o email seja digitado com as caracteristicas corretas.
    def valida_email(self):
        email_validador = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', self.email) 
        if email_validador:
            print('E-mail válido!')
        else: 
            print('Digite um e-mail válido!') 
            self.coletar_email_senha()
            
    
    def anvia_email(self, email, senha):
        msg = EmailMessage()
        msg['Subject'] = 'Planilha de Preços Site U Stora'
        msg['From'] = self.email
        msg['To'] = self.email
        msg.set_content('Segue planilha com o resultado solicitado.')

    def conexao_email(self):
        msg = EmailMessage()
        conexao = smtplib.SMTP('smtp.gmail.com: 587')
        conexao.starttls()
        conexao.ehlo()
        conexao.login(self.email, self.senha, initial_response_ok=True)
        conexao.send_message(msg)
        print(f'Email enviado com sucesso!')
        conexao.quit()


        
        
                
rum = WebScreapingEcommerce()
rum.start()