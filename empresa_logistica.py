# -*- coding: utf-8 -*-
"""Empresa-logistica.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1FlVwa42RafYmCkfBT4d1ic0PnF07avAX
"""

#----------- COMEÇO função dimensoesObjeto-------------#
def dimensoesObjeto ():#função da dimensão do objeto
  while True:
    try:
      comprimento = float(input('Digite o comprimento do objeto (em cm):'))
      largura = float(input('Digite a largura do objeto (em cm):'))
      altura = float(input('Digite a altura do objeto (em cm):'))
      volume = comprimento * largura * altura #calcula o volume do objeto
      print('O volume do seu objeto é: {} cm³' .format(volume))
      if volume < 1000: #verifica se o volume é menor que 1000
        return 10 #caso ele seja menor que 1000, ele retorna com 10 para o multiplicador de valor final
      elif 1000 <= volume < 10000: 
        return 20
      elif 10000<= volume < 30000:
        return 30
      elif 10000<= volume < 30000:
          return 30
      elif 30000 <= volume < 100000:
        return 50
      elif volume >= 100000: 
        print('Não aceitamos objetos com dimensões tão grandes')
        continue #caso seja um volume maior ou igual a 100000, ele retorna para recomeçar o processo
    except ValueError: #caso o usuário digite algo que não seja um número
      print('Você digitou alguma dimensão do objeto com valor não numérico')
      continue #retorna para recomeçar o laço

#----------- FIM função dimensoesObjeto-------------#



#----------- COMEÇO função pesoObjeto-------------#
def pesoObjeto (): #função do peso do objeto
  while True:
    try:
      peso = float(input('Digite o peso do objeto (em kg):'))
      if peso <= 0.1:
        return
      elif 0.1 < peso <= 1: 
        return 1.5
      elif 1 < peso <= 10:
        return 2
      elif 10 < peso <= 30:
        return 3
      elif peso > 30:
        print ('Não aceitamos objetos tão pesados')
    except ValueError:
      print('Você digitou alguma dimensão do objeto com valor não numérico')
      continue
#----------- FIM função pesoObjeto-------------#



#----------- COMEÇO função rotaObjeto-------------#
def rotaObjeto (): #função da rota do objeto
  while True:
    rota = input('Selecione a rota:\n RS - De Rio de Janeiro a São Paulo\nSR - De São Paulo ao Rio de Janeiro\n BS - DE Brasília a São Paulo\nSB - De São Paulo a Brasília\nBR - De Brasília a Rio de Janeiro\n RB - De Rio de Janeiro a Brasilia\n')
    if rota == 'RS':
      return 1
    if rota == 'SR':
      return 1      
    elif rota == 'BS':
      return 1.2   
    elif rota == 'SB':
      return 1.2
    elif rota == 'BR':
      return 1.5
    elif rota == 'RB':
      return 1.5
    else:
      print('Você digitou uma rota que não existe ')
      continue

#----------- FIM função rotaObjeto-------------#



#----------- COMEÇO MAIN ------------#
print('Bem-Vindo à Luana Vieira Machado Logística')
dimensao = float(dimensoesObjeto ())
peso = float(pesoObjeto ())
rota = float(rotaObjeto ())
total = dimensao * peso * rota
print ('Total a pagar (R$): {} (dimensões: {} * peso: {} * rota: {} )' .format(total, dimensao, peso, rota))
#----------- FIM MAIN ------------#