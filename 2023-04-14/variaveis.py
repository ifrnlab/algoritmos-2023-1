from time import sleep as dormir

nome = 'Fulano de Tal'
idade = 25
altura = 1.75
ta_fraco = False
nadinha = None
matricula = '20239876543210'

letra_de_musica = '''

Encontros e Despedidas
(Milton Nascimento)

Mande notícias do mundo de lá
Diz quem fica
Me dê um abraço, venha me apertar
'To chegando
Coisa que gosto é poder partir
Sem ter planos
Melhor ainda é poder voltar
Quando quero
Todos os dias é um vai e vem
A vida se repete na estação
Tem gente que chega pra ficar
Tem gente que vai pra nunca mais
Tem gente que vem e quer voltar
Tem gente que vai e quer ficar
Tem gente que veio só olhar
Tem gente a sorrir e a chorar
E assim, chegar e partir
São só dois lados
Da mesma viagem
O trem que chega
É o mesmo trem da partida
A hora do encontro
É também despedida
A plataforma dessa estação
É a vida desse meu lugar
É a vida desse meu lugar
É a vida
A hora do encontro
É também despedida
A plataforma dessa estação
É a vida desse meu lugar
É a vida desse meu lugar
É a vida
'''

print(f'Meu nome é {nome}, tenho {idade} anos, {altura}m de altura e minha matrícula é {matricula}.')
print('Minha música predileta é...')

for linha in letra_de_musica.splitlines():
    print(linha)
    dormir(0.3)
    