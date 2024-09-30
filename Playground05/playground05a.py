# Neste playground, vamos trabalhar com timers, sensor de luz e sensor de movimento.
# Veja os códigos de exemplo e programe o que está sendo soliticado em LETRAS MAIÚSCULAS.


# Inicialização do simulador. Escreva todo o seu código dentro da main!
from extra.playground import rodar

@rodar
def main():
    
    # Começamos importando as bibliotecas, como sempre.
    from threading import Timer
    
    from gpiozero import LED, Button, DistanceSensor, Buzzer, LightSensor, MotionSensor
    from Adafruit_CharLCD import Adafruit_CharLCD
    from time import sleep
    
    
    # Vamos começar com o Timer, que já tinha aparecido rapidamento no Projeto 02.
    # Ela é uma ótima alternativa à sleep para aguardar um tempo, sem travar o programa.
    # Primeiro a gente cria uma função que será chamada quando o tempo terminar.
    def timer1_terminou():
        print("O timer terminou!")
        
        
    # Depois é só criar um timer que receba essa função.
    # ATENÇÃO: lembre que eu passo só o nome da função, sem os parêntesis no final!
    timer1 = Timer(5.0, timer1_terminou)
    
    
    # Agora a parte final importante: inicie o timer com o start!
    timer1.start()
    print("Timer de 5 segundos iniciado. Aguarde...")
    
    
    # Timers vêm com um comando de cancelar a contagem.
    # Vamos usar o Botão 1 para testar isso.
    def cancelar_timer1():
        timer1.cancel()
        print("Timer cancelado!")
        
    botao1 = Button(11)
    botao1.when_pressed = cancelar_timer1
    
    
    # RODE O CÓDIGO, ESPERE O TIMER TERMINAR E VEJA O RESULTADO NO SHELL.
    # DEPOIS RODE NOVAMENTE E CANCELE O TIMER APERTANDO O BOTÃO 1.
    
    
    
    # Caso eu queira criar e cancelar um mesmo timer várias vezes, podemos usar o global.
    global timer2
    timer2 = None
    
    
    # Função para quando o timer terminar, que também anula a variável global.
    def explodir():
        global timer2
        timer2 = None
        
        print("Cabum!")
        
        
    # Ao apertar o botão 2, eu crio um novo timer, se ele não existir.
    def comecar_timer2():
        global timer2
        if timer2 == None:
            timer2 = Timer(3.0, explodir)
            
            # Não esquece de chamar a start!
            timer2.start()           
            
            print("Bomba vai explodir em 3 segundos!")
            
    botao2 = Button(12)
    botao2.when_pressed = comecar_timer2
    
    
    # Ao apertar o botão 3, eu cancelo o timer em andamento e anulo ele.
    def cancelar_timer2():
        global timer2
        if timer2 != None:
            timer2.cancel()
            timer2 = None
            
            print("Bomba desarmada!")
            
    botao3 = Button(13)
    botao3.when_pressed = cancelar_timer2
    
    
    # TESTE OS BOTÕES 2 E 3 PARA INICIAR E CANCELAR O TIMER 2!
    
    
    
    # CRIE UMA FUNÇÃO QUE TOQUE A CAMPAINHA 2 VEZES.
    # AO DETECTAR PROXIMIDADE NO SENSOR DE DISTÂNCIA, CRIE E INICIE UM TIMER DE 3 SEGUNDOS PARA CHAMAR ESSA FUNÇÃO. 
    # AO DETECTAR DISTÂNCIA NESSE SENSOR, CANCELE O TIMER SE ELE ESTIVER EM ANDAMENTO.
    
    
    
    
    # Por fim, a gente pode usar um timer recorrente, recriando o timer na própria função do término.
    def repetir_print():
        print("+1 segundo")
        
        global timer3
        timer3 = Timer(1.0, repetir_print)
        timer3.start()
        
    global timer3
    timer3 = Timer(1.0, repetir_print)
    
    
    
    # DESCOMENTE A LINHA ABAIXO PARA TESTAR O TIMER RECORRENTE.
    # DEPOIS DISSO, COMENTE A LINHA NOVAMENTE.
    #timer3.start()
        
    
    
    # CRIE UM TIMER RECORRENTE QUE FIQUE MOSTRANDO E APAGANDO A MENSAGEM "ALERTA!" NO LCD A CADA 1 SEGUNDO.
    # DICA: USE UMA OUTRA VARIÁVEL GLOBAL BOOLEANA PARA SABER SE É PARA ESCREVER OU APAGAR O LCD.
    
    
    
    
    # Agora vamos para a parte de hardware, começando com o sensor de luz.
    sensor_de_luz = LightSensor(8)
    
    # Na prática, ele é bem parecido com o sensor de distância.
    # Depois de iniciá-lo, eu posso pegar o valor medido a qualquer momento.
    # Ele retorna algo entre 0 e 1, sendo 0 a escuridão total e 1 o brilho total.
    quantidade_de_luz = sensor_de_luz.value
    
    
    # E, novamente, o sensor pode avisar quando houver uma mudança a partir de um limiar.
    # É a mesma ideia do when_in_range e when_out_of_range do Projeto 03.
    def luz_detectada():
        print("Ficou mais claro que o limiar configurado.")
        
    def escuridao_detectada():
        print("Ficou mais escuro que o limiar configurado.")
        
    
    sensor_de_luz.when_light = luz_detectada
    sensor_de_luz.when_dark = escuridao_detectada
    
    
    # O limiar padrão de claro/escuro é 0.1 (bem baixo), mas a gente pode reconfigurar.
    sensor_de_luz.threshold = 0.5
    

    # RODE O CÓDIGO, MEXA NO CONTROLE DO SENSOR DE LUZ E VEJA AS MENSAGENS NO SHELL DO THONNY.
    # DEPOIS MUDE O LIMIAR E VEJA A DIFERENÇA.
    
    
    
    # Para finalizar, vamos para sensor de movimento.
    sensor_de_movimento = MotionSensor(27)
    
    
    # Ele também vem com uma propriedade para ler o que o sensor está detectando.
    # Neste caso, o valor é True se houver movimento ou False se não houver.
    tem_movimento = sensor_de_movimento.motion_detected
    
    
    # E também temos funções para avisar quando ele detectar movimento ou inércia.
    def movimento_detectado():
        print("Sensor detectou movimento!")
        
    def inercia_detectada():
        print("Sensor detectou inércia.")
        
    
    sensor_de_movimento.when_motion = movimento_detectado
    sensor_de_movimento.when_no_motion = inercia_detectada
    

    # Só que essas detecções são um pouco mais peculiares que as anteriores.
    # O sensor vem com duas rodinhas: uma para ajustar a sensibilidade e outra para ajustar o tempo.
    # Essa última define quanto tempo você precisa ficar "parado" para ele assumir que não tem mais movimento.
    # Só que, além desse tempo, existe um segundo atraso para ele voltar a detectar movimento.
    # É esse atraso que faz parecer que o sensor não está funcionando direito.
    
    
    # TESTE O SENSOR DE MOVIMENTO, MEXENDO O MOUSE PERTO DELE E DEPOIS ESPERANDO UM POUCO.
    # PERCEBA O ÍCONE INDICANDO O ESTADO DO SENSOR E O MOMENTO EM QUE AS MENSAGENS APARECEM NO SHELL.
    # PERCEBA O MOMENTO DO ATRASO PARA VOLTAR A DETECTAR MOVIMENTO.
    
    
    
    # EXPERIMENTE INTEGRAR OS NOVOS SENSORES COM OUTRAS COISAS! BRINQUE À VONTADE!
    # Sugestão 1: crie um timer recorrente de 6 segundos que salve o datetime atual e o valor do sensor de luz numa coleção do MongoDB.
    # Sugestão 2: envie uma mensagem de texto para o Telegram se o sensor detectar movimento, mas sem mandar novamente até passar pelo menos 30 segundos.
        # Dica: use uma variável global do tipo datetime para salvar o momento do último envio.





    while True:
        sleep(0.1)