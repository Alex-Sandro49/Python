#Define uma ordem entre 4 alunos.

from random import shuffle

a1 = str(input('Primeiro aluno: '))
a2 = str(input('Segundo aluno: '))
a3 = str(input('Terceiro aluno:'))
a4 = str(input('Quarto aluno: '))
alunos = [a1, a2, a3, a4]
shuffle(alunos)
print(f'A ordem de apresentação será \n {alunos}')
