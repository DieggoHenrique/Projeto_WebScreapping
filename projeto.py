#============================================================================#
#            RASPAGEM DE DADOS WEBSCREAPING - E-COMMERCE                     #
#============================================================================#

# BIBLIOTECA DO PROJETO
import re

# Construindo o projeto
class WebScreapingEcommerce:
    
    
    def start(self):
        self.menu()
        self.coletar_email_senha()
    
    def menu(self):
        print('#========================================#')
        print('#    RASPAGEM DE DADOS SITE E-COMMERCE   #')
        print('#               PROJETO 01               #')
        print('#========================================#')
    
    def coletar_email_senha(self):
        print('Digite um email e senha válidos para receber o relatório.')
        self.email = input('Digite seu e-mail: ')
        self.valida_email()
        self.senha = input('Digite sua senha: ')
        print('E-mail e senha salvos!')
    
    def valida_email(self):
        email_validador = re.search(r'[a-zA-Z0-9_-]+@[a-zA-Z0-9]+\.[a-zA-Z]{1,3}$', self.email) 
        if email_validador:
            print('E-mail válido!')
        else: 
            print('Digite um e-mail válido!') 
            self.coletar_email_senha()
            
    
        
rum = WebScreapingEcommerce()
rum.start()