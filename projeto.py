#============================================================================#
#            RASPAGEM DE DADOS WEBSCREAPING - E-COMMERCE                     #
#============================================================================#

# BIBLIOTECA DO PROJETO


# Construindo o projeto
class WebScreapingEcommerce:
    
    
    def start(self):
        self.menu()
        self.coletar_email_senha()
    
    def menu(self):
        print('#========================================#')
        print('#    RASPAGEM DE DADOS SITE E-COMMERCE   #')
        print('#    Digite um e-mail e senha válidos     ')
        print('#========================================#')
        
    def coletar_email_senha(self):
        self.email = input('Digite seu e-mail: ')
        self.senha = input('Digite sua senha: ')
        print('email e senha salvos!')
        
        
rum = WebScreapingEcommerce()
rum.start