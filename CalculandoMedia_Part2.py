a = int(input('Primeiro Bimestre: '))
if a > 10:
    a = int(input('Voce digitou errado. Primeiro Bimestre: '))
b = int(input('Segundo Bimestre: '))
if b > 10:
    b = int(input('Voce digitou errado. Segundo Bimestre: '))
c = int(input('Terceiro Bimestre: '))
if c > 10:
    c = int(input('Voce digitou errado. Terceiro Bimestre: '))
d = int(input('Quarto Bimestre: '))
if d > 10:
    d = int(input('Voce digitou errado. Quarto Bimestre: '))
media = (a + b + c + d) / 4
print('media: {}'.format(media))
