arquetipos_herois = ['Herói', 'Anti-herói', 'Escolhido', 'Rebelde', 'Mentor', 'Governante', 'Ingênuo', 'Aventureiro', 'Sobrevivente', 'Malandro']
arquetipos_viloes = ['Tirano', 'Fanático', 'Manipulador', 'Monstro', 'O trágico', 'Cientista louco', 'Anti-vilão']
ocupacao = ['Guerreiro', 'Estrategista', 'Investigador', 'Diplomata', 'Assassino', 'Especialista', 'Mercenario', 'Místico']
origem = ['Nobre', 'Camponês', 'Soldado', 'Criminoso', 'Estudioso', 'Acólito', 'Orfão']
objetivo = ['Vingança', 'Poder', 'Redenção', 'Conhecimento', 'Riqueza', 'Proteção', 'Liberdade', 'Legado']
defeito_fatal = ['Orgulho', 'Ganância', 'Covardia', 'Obsessão', 'Ingenuidade', 'Impulsividade', 'Vício', 'Crueldade']

import random

heroi_ou_vilao = random.choice(['Herói', 'Vilão'])
if heroi_ou_vilao == 'Herói':
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