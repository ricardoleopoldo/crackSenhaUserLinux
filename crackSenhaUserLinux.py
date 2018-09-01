#!/usr/bin/python
#coding: utf-8

import crypt
import sys
import time

hash = raw_input('Digite o hash completo: ')
salt = raw_input('Digite o salt:')

file = open('wl.txt','r') #carrega a wordlist
senhas = file.read().split('\n')
inicio = time.time()
print "\nTestando as senhas, por favor aguarde ..."
for senha in senhas:
	resultado = crypt.crypt(senha,salt)
	if (resultado == hash):
		print "Senha encontrada: "+senha
		final = time.time()
		print "Tempo de execução: %.2f" % (final - inicio)+" ms"
		sys.exit(0)
file.close()
print "Senha não encontrada"
final = time.time()
print "Tempo de execução: %.2f" % (final - inicio)+" ms"
sys.exit(0)
