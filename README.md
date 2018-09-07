# Identificando senha de usuário Linux
Script para identificar a senha do usuário linux, por analise de hash

O script tem por finalidade identificar a senha do usuário Linux, por meio, do hash e salt obtido do arquivo shadow. 
Executando brute force local por meio de wordlist.

<b>Exemplo:</b><br>
<b>Hash completo:</b>
$6$oZZQWBkc$hQ4QKeH2kMHDJNqP/4G4qD03Yiftj1r5n6HJ14jVv4Fq.DH2f.Cp67pZYyyodwoT6BmPvGfKTQnc5yA0.b.mB/ <br>
<b>Salt:</b><br> 
$6$oZZQWBkc$

Este hash equivale a senha "102030", este valor deverá estar contido na <i>wordlist</i>, para que o resultado seja positivo, caso o contrário, o script deverá informar por mensagem que a senha não foi encontrada. 
