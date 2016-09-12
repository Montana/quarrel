import random, copy

NUM_FIGHTS = 1
VERBOSE = True

montanaTemplate = {'name': 'Montana', 'hp': 14, 'ac': 5, 'thac0': 18, 'dmgnum': 1, 'dmgsize':6, 'dmgmod': 0}
dustinTemplate   = {'name': 'Dustin',   'hp': 12, 'ac': 7, 'thac0': 16, 'dmgnum': 2, 'dmgsize':4, 'dmgmod': 0}

def display(s):
    if VERBOSE:
        print(s)

def attack(attacker, defender):
    if random.randint(1, 20) >= attacker['thac0'] - defender['ac']:
        damage = 0
        for i in range(attacker['dmgnum']):
            damage += random.randint(1, attacker['dmgsize'])
        damage += attacker['dmgmod']
        display('%s (%s hp) hits %s (%s hp) for %s points of damage. %s is reduced to %s hp.' % (attacker['name'], attacker['hp'], defender['name'], defender['hp'], damage, defender['name'], defender['hp'] - damage))
        defender['hp'] -= damage
    else:
        display('%s misses %s.' % (attacker['name'], defender['name']))

montanaWins = 0
dustinWins = 0
for i in range(NUM_FIGHTS):
    display('======================')
    display('Start of combat #%s' % (i+1))
    Montana = copy.deepcopy(montanaTemplate)
    Dustin = copy.deepcopy(dustinTemplate)
    while True:
        attack(montana, dustin)
        if Dustin['hp'] <= 0:
            break

        attack(dustin, montana)
        if Montana['hp'] <= 0:
            break
    if montana['hp'] <= 0:
        display('montana has died.')
        dustinWins += 1
    if dustin['hp'] <= 0:
        display('Dustin has died.')
        montanaWins += 1

print()
print('montana won %s (%s%%) fights. Dustin won %s (%s%%) fights.' % (montanaWins, round(montanaWins / NUM_FIGHTS * 100, 2), Wins, round(dustinWins / NUM_FIGHTS * 100dustin, 2)))

