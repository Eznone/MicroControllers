# Neste playground, vamos trabalhar com o servidor Flask.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.playground import rodar
from time import sleep
@rodar
def main():
    
    # Começamos importando as bibliotecas, como sempre.
    from flask import Flask, render_template, redirect
    
    from gpiozero import LED, Button
    from Adafruit_CharLCD import Adafruit_CharLCD


    # Podemos iniciar os componentes de hardware que nem antes.
    led1 = LED(21)
    led2 = LED(22)
    led3 = LED(23)
    led4 = LED(24)
    lcd = Adafruit_CharLCD(2, 3, 4, 5, 6, 7, 16, 2)


    # Agora iniciamos um servidor.
    app = Flask(__name__)


    # Vamos começar criando com uma página simples, que só mostra um texto.
    # Abra o seu navegador e digite localhost:5000/teste para ver o resultado.
    # Obs: caso o localhost:5000/teste não esteja funcionando, tente 127.0.0.1:5000/teste
    @app.route("/teste")
    def pagina_de_teste():
        return "O servidor está funcionando!"



    # CRIE UMA OUTRA PÁGINA QUE RETORNE O SEU NOME.
    # LEMBRE-SE DE ESCOLHER UM OUTRO NOME PARA A ROTA E PARA A FUNÇÃO!
    # E NÃO ESQUEÇA DE DAR RUN NOVAMENTE!
    @app.route("/nome")
    def pagina_de_nome():
        return "Ronald Mcdonald"
    
    
    
    # Páginas podem receber um parâmetro do usuário.
    # Neste exemplo, a página espera um número inteiro no endereço.
    # Abra o seu navegador e digite localhost:5000/triplica/10 para ver o resultado.
    @app.route("/triplica/<int:x>")
    def triplica(x):
        resultado = x * 3
        return "%d vezes 3 é igual a %d" % (x, resultado)
    
    
    
    # Dá para receber mais de um parâmetro, inclusive do tipo float e string.
    # ATENÇÃO: o parâmetro float exige que os números tenham sempre um ponto decimal.
    # Abra o seu navegador e digite localhost:5000/faz_conta/0.5/x/1.3 para ver o resultado.
    @app.route("/faz_conta/<float:valor1>/<string:operacao>/<float:valor2>")
    def faz_conta(valor1, operacao, valor2):
        if operacao == "+":
            resultado = valor1 + valor2
        elif operacao == "-":
            resultado = valor1 - valor2
        elif operacao == "x":
            resultado = valor1 * valor2
        elif operacao == "÷":
            resultado = valor1 / valor2
        else:
            return "Operação inválida!"
            
        return "%f %s %f = %f" % (valor1, operacao, valor2, resultado)
    
    
    
    # CRIE UMA PÁGINA QUE RECEBA UMA STRING E NÚMERO INTEIRO N.
    # EXIBA A STRING NO LCD (LEMBRE DE DAR CLEAR) E PISQUE O LED 1 N VEZES.
    @app.route("/LCD/<string:message>/<int:n>")
    def message_LCD(message, n):
        for i in range(n):
            lcd.message("%s" % (message))
            sleep(0.3)
            lcd.clear()
            sleep(0.3)
        return "LCD finished"
    
    
    
    # As páginas podem retornar um texto com formatação HTML.
    # Acesse localhost:5000/mensagem_bonitinha no navegador e veja o resultado.
    @app.route("/mensagem_bonitinha")
    def mensagem_bonitinha():
        mensagem = "<h1>Seu sistema está desprotegido!</h1>"
        mensagem += "<p>Baixe a nossa proteção que com certeza não é um vírus!</p>"
        mensagem += "<a href='https://janks.link/micro/playground02.zip'>Baixar arquivo super seguro</a>"
        
        return mensagem


    # Ali em cima, eu montei o texto HTML na função, mas esse código pode ocupar muito espaço aqui.
    # Por isso, o Flask permite você retornar o conteúdo de um arquivo template.
    # Abra o arquivo pagina1.html da pasta templates num editor de texto como o Bloco de Notas.
    # Depois acesse localhost:5000/pagina_complexa no navegador para ver o resultado.
    @app.route("/pagina_complexa")
    def pagina_complexa():
        return render_template("pagina1.html")
    
    
    
    # CRIE UMA PÁGINA CONTENDO OS SEGUINTES ELEMENTOS HTML:
    #  - UMA LISTA COM AS MATÉRIAS QUE VOCÊ ESTÁ CURSANDO ATUALMENTE
    #  - UMA LISTA COM 5 LINKS PARA VÍDEOS DE YOUTUBE
    #  - UMA IMAGEM DE UM ANIMAL FOFO DE SUA PREFERÊNCIA
    # OBS: VOCÊ PRECISA DAR RUN AQUI NOVAMENTE PARA VER AS ALTERAÇÕES NO HTML.
    @app.route("/pagina_eu")
    def pagina_eu():
        return render_template("paginaEu.html")
    


    # Por fim, a sua página pode redirecionar para outra, em vez de retornar uma mensagem.
    # Acesse localhost:5000/redirecionar no navegador e veja a mudança de endereço.
    @app.route("/redirecionar")
    def redirecionar():
        return redirect("/pagina_de_destino")
    
    
    @app.route("/pagina_de_destino")
    def pagina_de_destino():
        return "Você foi redirecionado! Veja que o endereço mudou!"



    # CRIE UMA PÁGINA QUE RECEBA UM PÂRAMETRO DO TIPO STRING.
    # SE O TEXTO FOR IGUAL A "peixe-espada", ACENDA O LED 2 E RETORNE "Senha correta".
    # CASO CONTRÁRIO, REDIRECIONE PARA A PÁGINA /mensagem_bonitinha.
    @app.route("/comp/<string:phrase>")
    def comp(phrase):
        if (phrase == "peixe-espada"):
            return "senha correta"
        else:
            return redirect("/mensagem_bonitinha")




    # EXPERIMENTE CRIAR OUTRAS PÁGINAS QUE INTERAJAM COM O HARDWARE E RETORNEM UM TEXTO HTML!
    
    
    

    # Não esqueça de dar run no servidor aqui no final!
    app.run(port=5000)


    # Não escreva nenhum código depois do run!
    # Ele é tipo um while True que segura o programa, então nada depois dele vai rodar.