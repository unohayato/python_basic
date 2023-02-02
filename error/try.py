monsters = [299, 233, 33, 1000]
attack = 30
print(monsters)
monster = int(input('Choose Monster: '))
try:
  monsters[monster] -= attack
except IndexError:
  print('Index Error')
print(monsters)

