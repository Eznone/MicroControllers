# Neste playground, vamos trabalhar com o Active Pieces.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.playground import rodar

@rodar
def main():
    
    # Começamos importando as bibliotecas, como sempre.
    from requests import post
    from flask import Flask
    
    from gpiozero import LED, Button, DistanceSensor, LightSensor, Buzzer
    from Adafruit_CharLCD import Adafruit_CharLCD


    # Antes de começar a trabalhar com o Active Pieces, você precisa criar um conta lá.
    # Se não tiver feito isso ainda, acesse o endereço activepieces.com.
    
    
    # Depois de se cadastrar, crie um flow novo clicando em New Flow.
    # Configure o trigger para ser um Catch Webhook
    # Copie o endereço http que o Active Pieces gerou no menu lateral.
    endereco = "COLOQUE AQUI O ENDEREÇO HTTP QUE O ACTIVE PIECES DEU PARA O SEU WEBHOOK"
    dados = {"nome": "Jan K. S."}
    
    # Primeiro temos que fazer um post de teste para esse endereço.
    
    # DESCOMENTE AS LINHAS ABAIXO PARA CHAMAR O APPLET.
    # DEPOIS DE TESTAR, COMENTE NOVAMENTE.
    
    #post(endereco, params=dados)
    
    
    # Volte para o Active Pieces e selecione a ação como GMail > Send Mail.
    # Clique em Connection e autorize o seu Gmail a integrar com o Active Pieces.
    # Coloque o seu próprio endereço de email como destinatário e crie um título.
    # No campo Body, selecione o parâmetro "nome" no menu lateral (lá embaixo, dentro de queryParams).
    # Você pode colocar outro texto no campo Body junto com esse dado também também.
    # Clique em Publish para ativar o flow.
    
    
    # DESCOMENTE A LINHA ABAIXO PARA CHAMAR NOVAMENTE O FLOW.
    # DEPOIS DE TESTAR, COMENTE NOVAMENTE.
    # VERIFIQUE SE A MENSAGEM CHEGOU NA SUA CAIXA DE EMAIL.
    
    #post(endereco, params=dados)
    
    
    # MUDE A VARIÁVEL dados, COLOCANDO O SEU NOME DEPOIS DO nome, E RODE NOVAMENTE.
    
    
    # Esse chave "nome" poderia ser outra coisa com algum dado dos sensores, para fazer algum tipo de automação residencial.
    # Mas agora vamos testar o Active Pieces no sentido inverso, recebendo um evento de gatilho dele para o nosso servidor.
    
    
    # Rode o Ngrok no seu computador.
    #  - Windows: abra o arquivo rodar_ngrok.bat. Se aparecer um alerta, clique em More Info e Run Anyway.
    #  - Mac: clique no arquivo rodar_ngrok.command com o botão direito > Abrir.
    # Volte no site do Active Pieces e crie um outro applet clicando em New Flow.
    # No trigger, busque e selecione "Google Drive", evento New File e escolha a pasta que você quer monitorar.
    # Clique no botão Load Data para gerar dados de exemplo do Google Drive.
    # Na ação, busque e selecione "Send HTTP Request".
    # Selecione o método GET.
    # Copie e cole no campo URL o endereço gerado pelo NGrok, e adicione no final /novoDocumento/.
    # Depois do /novoDocumento/, selecione o atributo "name" do Google Drive (mo menu flutuante à esquerda)
    # ATENÇÃO: verifique se não tem nenhum espaço em branco no endereço do campo.
    # Ignore os outros campos. Clique em Continue e depois em Finish.
    

    # Agora iniciamos um servidor Flask.
    app = Flask(__name__)


    # Esta página será chamada pelo Active Pieces, recebendo o nome de um arquivo.
    # Arraste um arquivo qualquer para a pasta do Google Drive que você escolheu, enquanto este programa estiver rodando.
    # Observe a mensagem impressa no Shell do Thonny.
    @app.route("/novoDocumento/<string:nome>")
    def novoDocumento(nome):
        
        print("Novo documento adicionado no Google Drive: " + nome)
        
        return "Texto qualquer, porque quem vai acessar esta página é o Active Pieces."



    # EXPERIMENTE CRIAR OUTROS APPLET NO ACTIVE PIECES!
    
    

    # Não esqueça de dar run no servidor aqui no final!
    app.run(port=5000)


    # Não escreva nenhum código depois do run!
    # Ele é tipo um while True que segura o programa, então nada depois dele vai rodar.