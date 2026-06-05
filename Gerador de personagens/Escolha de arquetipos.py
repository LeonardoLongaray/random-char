arquetipos_herois = ['Herói', 'Anti-herói', 'Escolhido', 'Rebelde', 'Mentor', 'Governante', 'Ingênuo', 'Aventureiro', 'Sobrevivente', 'Malandro']
arquetipos_viloes = ['Tirano', 'Fanático', 'Manipulador', 'Monstro', 'O trágico', 'Cientista louco', 'Anti-vilão']
ocupacao = ['Guerreiro', 'Estrategista', 'Investigador', 'Diplomata', 'Assassino', 'Especialista', 'Mercenario', 'Místico']
origem = ['Nobre', 'Camponês', 'Soldado', 'Criminoso', 'Estudioso', 'Acólito', 'Orfão']
objetivo = ['Vingança', 'Poder', 'Redenção', 'Conhecimento', 'Riqueza', 'Proteção', 'Liberdade', 'Legado']
defeito_fatal = ['Orgulho', 'Ganância', 'Covardia', 'Obsessão', 'Ingenuidade', 'Impulsividade', 'Vício', 'Crueldade']

pref_jogador = input('Você prefere jogar de herói ou vilão? ').replace('ó','o').replace('ã', 'a').upper().strip()
idade_jogador = int(input('Qual sua idade? '))
aleatorizar = input('Iniciar aleatório? (sim/não) ').lower()

import random

if idade_jogador <17 and pref_jogador == "VILAO":
  print('Você não tem idade pra jogar de vilão')
  heroi_ou_vilao = 'HEROI'
elif idade_jogador<17:
  heroi_ou_vilao = 'HEROI'
elif aleatorizar == 'sim':
  heroi_ou_vilao = random.choice(['HEROI', 'VILAO'])
else:
  heroi_ou_vilao = pref_jogador

if heroi_ou_vilao == 'HEROI':
  print('Você será um herói e suas características serão as seguintes: ')
  lista = {"Arquétipo": arquetipos_herois,
    "Ocupação": ocupacao,
    "Origem": origem,
    "Objetivo": objetivo,
    "Defeito Fatal": defeito_fatal}

  personagem = {}
  for categoria, lista in lista.items():
    personagem[categoria] = random.choice(lista)
  for categoria, resultado in personagem.items():
    print(f'{categoria}: {resultado}')
else:
  print('Você será um vilão e suas características serão as seguintes: ')
  lista = {"Arquétipo": arquetipos_viloes,
    "Ocupação": ocupacao,
    "Origem": origem,
    "Objetivo": objetivo,
    "Defeito Fatal": defeito_fatal}

  personagem = {}
  for categoria, lista in lista.items():
    personagem[categoria] = random.choice(lista)
  for categoria, resultado in personagem.items():
    print(f'{categoria}: {resultado}')