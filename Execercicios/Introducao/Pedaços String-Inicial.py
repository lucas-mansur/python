#!/usr/bin/env python
# coding: utf-8

# ### Forma Básica

precos = "Jan: 25, Fev: 27, Mar: 29"

print(len(precos))
print(precos[0])
print(precos[-1])

print("Janeiro:", precos[5:7])
print("Janeiro:", precos[-20:-18])
print("Fevereiro:",precos[14:16])
print("Fevereiro:",precos[-11:-9])
print("Março: ", precos[23:25])
print("Março: ", precos[-2:])

# ### Posição Inicial e Final



# ### Posição Inicial e Final com Step


codigo = "1.2.3.4,5,1,2.3.4,7.9"

print(codigo[::2])

