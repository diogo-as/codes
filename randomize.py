import random, collections

items = ['here', 'are', 'some', 'strings', 'of',
         'which', 'we', 'will', 'select', 'one']

rand_item = items[random.randrange(len(items))]

#print(rand_item)

participantes = {
    'diogo':'',
    'nanda':'',
    'alice':'',
    'tico':'',
    'lorena':'',
    'kleyton':'',
    'pedro':'',
    'regina':'',
    'arthur':'',
    'duda':''
        }
sorteio = {}

for nome in participantes.keys():
    a = random.choice(participantes.keys())
    while (a == nome) or (a in participantes.values()):
            a = random.choice(participantes.keys())
    participantes[nome] = a

for a, b in sorted(participantes.items()):
    print("Participante: "+a+" Tirou: "+b)
