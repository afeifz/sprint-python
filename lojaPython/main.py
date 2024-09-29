

''' 
    Login
    Menu com pefil, quiz, loja e sair
    Perfil - mostrar moedas e carro 
    Quiz - perguntas a cada resposta certa = moedas
    Loja - comprar itens pro carro
    Sair - sair
'''

# Variavéis globais
pontos = 10000
usuario = ''
carroUsuario = 'Nenhum'
pneuUsuario = 'Nenhum'
motorUsuario = 'Nenhum'
corUsuario = 'Nenhum'

def obrigarResposta(msg: str, respostasAceita):
    respostaObrigado = input(msg)

    while respostaObrigado not in respostasAceita:
        respostaObrigado = input("Erro!\n " + msg)
        
    return respostaObrigado

# LOGIN
def login():
    global usuario
    usuarios = {}
    
    usuario_nome = input('Digite seu usuário: ')
    senha = input('Digite sua senha: ')
    
    if usuario in usuarios:
        print('Este usuário já está registrado')
        return
    
    usuarios = { 'Nome': usuario_nome, 'Senha': senha }
    usuario = usuarios['Nome']

    print('Usuário registrado com sucesso!')
    menu()

# MENU
def menu():
    print("---------------")
    print('Menu')
    escolhaMenu =  obrigarResposta("1) Perfil\n2) Quiz\n3) Loja\n4) Minigame\n5) Sair\n> ", ['1', '2', '3', '4','5'])
    
    if(escolhaMenu == '1'):
        perfil()
    elif(escolhaMenu == '2'):   
        quiz()    
    elif(escolhaMenu == '3'):
        loja()
    elif(escolhaMenu == '4'):
        minigame()
    else:
        exit()

#PERFIL
def perfil(): 
    global usuario, pontos, carroUsuario, motorUsuario, pneuUsuario, corUsuario

    print("---------------")
    print(f"Bem vindo, {usuario}!")
    print(f"Você tem: {pontos} pontos.")
    print('-' * 20)
    print("Seu carro")
    print('-' * 20)
    print(f"| Carro - {carroUsuario.join(' |')}")
    print(f"| Motor - {motorUsuario.join(' |')}")
    print(f"| Pneu - {pneuUsuario.join(' |')}")
    print(f"| Cor - {corUsuario.join(' |')}")
    print("---------------")
    print("Você pode conseguir mais pontos no quiz!")

    escolha_perfil = obrigarResposta("Quer prosseguir pro quiz? (s/n) ", ["s", "n"])

    if (escolha_perfil == "s"):
        quiz()
    else: 
        menu()

#MINIGAME
def minigame():
    # Inicializar o Pygame
    pygame.init()

    # Configurações da tela
    screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Minigame de Corrida")

    # Carregar a imagem da pista
    track_image = pygame.image.load('8457212.jpg')
    track_image = pygame.transform.scale(track_image, (800, 600))  # Ajuste o tamanho conforme necessário

    # Cor do carro
    car_color = (255, 0, 0)
    car_pos = [520, 235]
    # Loop principal do jogo
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                menu()

        # Movimento do carro
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            car_pos[0] -= 5
        if keys[pygame.K_RIGHT]:
            car_pos[0] += 5
        if keys[pygame.K_UP]:
            car_pos[1] -= 5
        if keys[pygame.K_DOWN]:
            car_pos[1] += 5

        # Desenhar a pista e o carro
        screen.blit(track_image, (0, 0))  # Desenhar a imagem da pista
        pygame.draw.rect(screen, car_color, pygame.Rect(car_pos[0], car_pos[1], 50, 30))  # Desenhar o carro

        pygame.display.flip()
        pygame.time.Clock().tick(30)  # 30 frames por segundo

#QUIZ
def quiz():
    dificulty = ['1', '2', '3']
    questions_quantity = 0
    msg_input = '''
        Escolha a dificuldade:

        1 - Fácil (10 perguntas)
        2 - Médio (20 perguntas)
        3 - Difícil (30 perguntas)
    '''

    questions = [
        'Qual cidade sediou a primeira corrida da Fórmula E?',
        'Qual equipe ganhou o campeonato da Fórmula E na temporada 2019-2020?',
        'Quantos pontos são concedidos para a pole position em uma corrida de Fórmula E?',
        'Qual piloto detém o recorde de mais vitórias na Fórmula E até agora?',
        'Qual foi o primeiro fabricante a entrar na Fórmula E?',
        'Qual é a duração média de uma corrida de Fórmula E?',
        'Qual cidade tem o circuito mais longo na Fórmula E?',
        'Quantos modos de potência tem um carro de Fórmula E durante uma corrida?',
        'Qual piloto é conhecido como "o piloto da chuva" na Fórmula E?',
        'Qual é a pontuação máxima possível para uma equipe em uma única corrida na Fórmula E?',
        'Qual é o nome oficial do carro usado na Fórmula E?',
        'Qual é a velocidade máxima de um carro de Fórmula E durante uma corrida?',
        'Qual piloto conquistou o título de campeão na temporada inaugural da Fórmula E em 2014-2015?',
        'Quantas voltas normalmente são disputadas em uma corrida de Fórmula E?',
        'Qual cidade sediou a final da temporada 2018-2019 da Fórmula E?',
        'Qual equipe venceu o Campeonato de Equipes na temporada 2017-2018?',
        'Qual é o sistema de recarga usado pelos carros de Fórmula E durante uma corrida?',
        'Qual é o peso mínimo de um carro de Fórmula E, incluindo o piloto?',
        'Qual é a potência máxima do motor elétrico de um carro de Fórmula E durante uma corrida?',
        'Qual piloto foi o primeiro a vencer uma corrida de Fórmula E em seu país de origem?',
        'Qual cidade sediou a corrida de Fórmula E conhecida como "ePrix das Américas"?',
        'Qual é o sistema de frenagem usado pelos carros de Fórmula E?',
        'Qual é a potência do "modo ataque" usado pelos carros de Fórmula E durante uma corrida?',
        'Qual é o prêmio dado ao vencedor do Campeonato de Equipes na Fórmula E?',
        'Qual é o nome do sistema de segurança usado pelos carros de Fórmula E?',
        'Qual é o peso mínimo de um carro de Fórmula E, incluindo o piloto?',
        'Qual é a duração total de uma temporada típica da Fórmula E?',
        'Qual é o circuito mais longo da Fórmula E em termos de distância percorrida?',
        'Qual é a marca do pneu oficial usado na Fórmula E?',
        'Qual é a potência máxima do modo de ataque durante uma corrida de Fórmula E?'
    ]
    
    answers = [
        'C',
        'C',
        'C',
        'A',
        'D',
        'B',
        'A',
        'D',
        'B',
        'C',
        'B',
        'B',
        'C',
        'B',
        'A',
        'B',
        'A',
        'B',
        'B',
        'B',
        'B',
        'A',
        'A',
        'B',
        'A',
        'A',
        'D',
        'D',
        'B',
        'A',
        'C'
    ]
    
    options = [
        [
            'A) Paris',
            'B) Londres',
            'C) Pequim',
            'D) Berlim'
        ],
        [
           'A) Mercedes-Benz EQ Formula E Team',
           'B) Audi Sport ABT Schaeffler',
           'C) DS Techeetah',
           'D) Nissan e.dams' 
        ],
        [
            'A) 1 ponto',
            'B) 2 pontos',
            'C) 3 pontos',
            'D) 4 pontos'
        ],
        [
            'A) Sébastien Buemi',
            'B) Lucas di Grassi',
            'C) Jean-Éric Vergne',
            'D) Sam Bird'
        ],
        [
            'A) Nissan',
            'B) BMW',
            'C) Audi',
            'D) Renault'
        ],
        [
            'A) 30 minutos',
            'B) 45 minutos',
            'C) 60 minutos',
            'D) 75 minutos'
        ],
        [
            'A) Nova York',
            'B) Mônaco',
            'C) Buenos Aires',
            'D) Santiago'
        ],
        [
            'A) 2',
            'B) 3',
            'C) 4',
            'D) 5'
        ],
        [
            'A) Oliver Rowland',
            'B) Stoffel Vandoorne',
            'C) Nyck de Vries',
            'D) Antonio Felix da Costa'
        ],
        [
            'A) 30 pontos',
            'B) 32 pontos',
            'C) 35 pontos',
            'D) 40 pontos'
        ],
        [
            'A) Gen1',
            'B) Spark SRT05e',
            'C) E-Racer',
            'D) Electra R1'
        ],
        [
            'A) 220 km/h',
            'B) 250 km/h',
            'C) 280 km/h',
            'D) 300 km/h'
        ],
        [
            'A) Lucas di Grassi',
            'B) Sébastien Buemi',
            'C) Nelson Piquet Jr.',
            'D) Jean-Éric Vergne'
        ],
        [
            'A) 25 voltas',
            'B) 30 voltas',
            'C) 35 voltas',
            'D) 40 voltas'
        ],
        [
            'A) Nova York',
            'B) Paris',
            'C) Londres',
            'D) Berlim'
        ],
        [
            'A) Audi Sport ABT Schaeffler',
            'B) DS Techeetah',
            'C) Mahindra Racing',
            'D) Envision Virgin Racing'
        ],
        [
            'A) Recarga por indução',
            'B) Recarga rápida',
            'C) Recarga em paradas nos boxes',
            'D) Recarga solar'
        ],
        [
            'A) 800 kg',
            'B) 850 kg',
            'C) 900 kg',
            'D) 950 kg'
        ],
        [
            'A) 180 kW',
            'B) 200 kW',
            'C) 220 kW',
            'D) 250 kW'
        ],
        [
            'A) Sébastien Buemi',
            'B) Nelson Piquet Jr.',
            'C) Lucas di Grassi',
            'D) Jean-Éric Vergne'
        ],
        [
            'A) Cidade do México',
            'B) Miami',
            'C) Montreal',
            'D) São Paulo'
        ],
        [
            'A) Frenagem regenerativa',
            'B) Freios a disco convencionais',
            'C) Freios cerâmicos',
            'D) Freios a tambor'
        ],
        [
            'A) 180 kW',
            'B) 200 kW',
            'C) 220 kW',
            'D) 250 kW'
        ],
        [
            'A) Troféu de Equipe Campeã',
            'B) Troféu de Construtores',
            'C) Troféu do Campeonato de Fabricantes',
            'D) Troféu das Nações'
        ],
        [
            'A) HALO',
            'B) SCRAM',
            'C) VIRTUS',
            'D) ROLL'
        ],
        [
            'A) Oliver Rowland',
            'B) Stoffel Vandoorne',
            'C) Nyck de Vries',
            'D) Sébastien Buemi'
        ],
        [
            'A) 6 meses',
            'B) 8 meses',
            'C) 10 meses',
            'D) 12 meses'
        ],
        [
            'A) Circuito de Berlim',
            'B) Circuito de Nova York',
            'C) Circuito de Londres',
            'D) Circuito de Marrakech'
        ],
        [
            'A) Michelin',
            'B) Bridgestone',
            'C) Pirelli',
            'D) Continental'
        ],
        [
            'A) 180 kW',
            'B) 200 kW',
            'C) 220 kW',
            'D) 250 kW'
        ]
    ]
    
    print('Bem vindo ao quiz!')
    escolha = obrigarResposta(msg_input, dificulty)
    
    if escolha == '1':
        questions_quantity = 10
    elif escolha == '2':
        questions_quantity = 20
    else:
        questions_quantity = 30
        
    def perguntar():
        global pontos

        for i in range(questions_quantity):
            enunciado = f'''
                {i + 1} - {questions[i]}

                Opções:
                {options[i]}
            '''

            print(enunciado)
            # Mudar opções pra letras minúsculas
            resposta_usuario = obrigarResposta('Qual sua resposta? (A, B, C, D) ', ['A', 'B', 'C', 'D'])

            if resposta_usuario == answers[i]:
                pontos = pontos + 10
                print('Resposta certa!')
            else:
                print('Resposta errada!')

        print('Fim do quiz!')

    perguntar()

# LOJA
def loja():
    global carroUsuario, motorUsuario, pneuUsuario, corUsuario, pontos

    # Variáveis de opções
    carros = ['Uno', 'Tesla', 'Gol', 'Up', 'Porsche 911']  
    valorCarro = [50, 100, 60, 40, 200]
    motor = ['V6', 'V8', 'V10', 'V12']
    valorMotor = [20, 30, 40, 50]  
    pneu = ['C1', 'C2', 'C3', 'C4', 'C5', 'C6']
    valorPneu = [5, 10, 15, 20, 25, 30]
    pintura = ['Azul', 'Branco', 'Preto', 'Vermelho', 'Roxo']
    valorPintura = 5

    def verificarPontos(preco):
        global pontos

        if pontos < preco:
            return False
        else:
            return True

    print('Bem vindo a nossa loja!')

    escolhas_item = '''
        1) Carro
        2) Motor
        3) Pneu
        4) Pintura
    '''
    escolhaitem = obrigarResposta(escolhas_item, ['1', '2', '3', '4'])     
    
    if escolhaitem == '1':
        carro_escolhas = '''
            1) Uno
            2) Tesla
            3) Gol
            4) Up
            5) Porsche 911
        '''
        escolha_carro = obrigarResposta(carro_escolhas.join('\n '), ['1', '2', '3', '4', '5'])
        
        if escolha_carro == '1':
            print(f'Preço: {valorCarro[0]}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorCarro[0])
                
                if pode_comprar:
                    pontos -= valorCarro[0]
                    carroUsuario = carros[0]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
            elif resposta == 'n':
                menu()

        elif escolha_carro == '2':
            print(f'Preço: {valorCarro[1]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorCarro[1])
                if pode_comprar:
                    pontos -= valorCarro[1]
                    carroUsuario = carros[1]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()

        elif escolha_carro == '3':
            print(f'Preço: {valorCarro[2]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorCarro[2])
                if pode_comprar:
                    pontos -= valorCarro[2]
                    carroUsuario = carros[2]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()

        elif escolha_carro == '4':
            print(f'Preço: {valorCarro[3]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorCarro[3])
                if pode_comprar:
                    pontos -= valorCarro[3]
                    carroUsuario = carros[3]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()

        elif escolha_carro == '5':
            print(f'Preço: {valorCarro[4]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorCarro[4])

                if pode_comprar:
                    pontos -= valorCarro[4]
                    carroUsuario = carros[4]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
    
    elif escolhaitem == '2':
        motor_escolhas = '''
            1) Motor V6
            2) Motor V8
            3) Motor V10
            4) Motor V12
        '''
        escolha_motor = obrigarResposta(motor_escolhas, ['1', '2', '3', '4'])

        if escolha_motor == '1':
            print(f'Preço: {valorMotor[0]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorMotor[0])
                
                if pode_comprar:
                    pontos -= valorMotor[0]
                    motorUsuario = motor[0]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu() 
               
        elif escolha_motor == '2':
            print(f'Preço: {valorMotor[1]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorMotor[1])
                
                if pode_comprar:
                    pontos -= valorMotor[1]
                    motorUsuario = motor[1]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_motor == '3':
            print(f'Preço: {valorMotor[2]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorMotor[2])
                
                if pode_comprar:
                    pontos -= valorMotor[2]
                    motorUsuario = motor[2]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_motor == '4':
            print(f'Preço: {valorMotor[3]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorMotor[3])
                
                if pode_comprar:
                    pontos -= valorMotor[3]
                    motorUsuario = motor[3]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()
            
    elif escolhaitem == '3':
        pneu_escolhas = '''
            1) C1
            2) C2
            3) C3
            4) C4
            5) C5
            6) C6
        '''
        escolha_pneus = obrigarResposta(pneu_escolhas, ['1', '2', '3', '4', '5', '6'])

        if escolha_pneus == '1':
            print(f'Preço: {valorPneu[0]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[0])
                
                if pode_comprar:
                    pontos -= valorPneu[0]
                    pneuUsuario = pneu[0]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_pneus == '2':
            print(f'Preço: {valorPneu[1]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[1])
                
                if pode_comprar:
                    pontos -= valorPneu[1]
                    pneuUsuario = pneu[1]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_pneus == '3':
            print(f'Preço: {valorPneu[2]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[2])
                
                if pode_comprar:
                    pontos -= valorPneu[2]
                    pneuUsuario = pneu[2]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_pneus == '4':
            print(f'Preço: {valorPneu[3]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[3])
                
                if pode_comprar:
                    pontos -= valorPneu[3]
                    pneuUsuario = pneu[3]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_pneus == '5':
            print(f'Preço: {valorPneu[4]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[4])
                
                if pode_comprar:
                    pontos -= valorPneu[4]
                    pneuUsuario = pneu[4]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

        elif escolha_pneus == '6':
            print(f'Preço: {valorPneu[5]}')
            resposta= obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPneu[5])
                
                if pode_comprar:
                    pontos -= valorPneu[5]
                    pneuUsuario = pneu[5]
                    print('Compra efetuada com sucesso.')
                    perfil()
                else:
                    print('Você não tem pontos suficientes.')
                    loja()
            elif resposta == 'n':
                menu()

    elif escolhaitem == '4':
        pintura_escolhas = '''
            1) Azul
            2) Branco
            3) Preto
            4) Vermelho
            5) Roxo
        '''
        escolha_pintura = obrigarResposta(pintura_escolhas, ['1', '2', '3', '4', '5'])

        if escolha_pintura == '1':
            print(f'Preço: {valorPintura}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])
            
            if resposta == 's':
                pode_comprar = verificarPontos(valorPintura)
                
                if pode_comprar:
                    pontos -= valorPintura
                    corUsuario = pintura[0]
                    print('Compra efetuada!')
                else:
                    print('Você não tem pontos suficientes.')
                    
            elif resposta == 'n':
                menu()
                
        if escolha_pintura == '2':
            print(f'Preço: {valorPintura}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPintura)

                if pode_comprar:
                    pontos -= valorPintura
                    corUsuario = pintura[1]
                    print('Compra efetuada!')
                else:
                    print('Você não tem pontos suficientes.')
            elif resposta == 'n':
                menu()

        if escolha_pintura == '3':
            print(f'Preço: {valorPintura}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPintura)

                if pode_comprar:
                    pontos -= valorPintura
                    corUsuario = pintura[2]
                    print('Compra efetuada!')
                else:
                    print('Você não tem pontos suficientes.')
            elif resposta == 'n':
                menu()

        if escolha_pintura == '4':
            print(f'Preço: {valorPintura}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPintura)

                if pode_comprar:
                    pontos -= valorPintura
                    corUsuario = pintura[3]
                    print('Compra efetuada!')
                else:
                    print('Você não tem pontos suficientes.')
            elif resposta == 'n':
                menu()

        if escolha_pintura == '5':
            print(f'Preço: {valorPintura}')
            resposta = obrigarResposta('Gostaria de efetuar a compra? (s/n) ', ['s', 'n'])

            if resposta == 's':
                pode_comprar = verificarPontos(valorPintura)

                if pode_comprar:
                    pontos -= valorPintura
                    corUsuario = pintura[4]
                    print('Compra efetuada!')
                else:
                    print('Você não tem pontos suficientes.')
            elif resposta == 'n':
                menu()

# LÓGICA PRINCIPAL
def main():
    login()
    
    while True:
        menu()

main()