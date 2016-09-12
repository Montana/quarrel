import random, copy

NUM_FIGHTS = 1
VERBOSE = True

MontanaTemplate = {'name': 'Montana', 'hp': 14, 'ac': 5, 'thac0': 18, 'dmgnum': 1, 'dmgsize':6, 'dmgmod': 0}
DustinTemplate   = {'name': 'Dustin',   'hp': 12, 'ac': 7, 'thac0': 16, 'dmgnum': 2, 'dmgsize':4, 'dmgmod': 0}

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

MontanaWins = 0
DustinWins = 0
for i in range(NUM_FIGHTS):
    display('======================')
    display('Start of combat #%s' % (i+1))
    Montana = copy.deepcopy(MontanaTemplate)
    Dustin = copy.deepcopy(DustinTemplate)
    while True:
        attack(Montana, Dustin)
        if Dustin['hp'] <= 0:
            break

        attack(Dustin, Montana)
        if Montana['hp'] <= 0:
            break
    if Montana['hp'] <= 0:
        display('Montana has died.')
        DustinWins += 1
    if Dustin['hp'] <= 0:
        display('Dustin has died.')
        MontanaWins += 1

print()
print('Montana won %s (%s%%) fights. Dustin won %s (%s%%) fights.' % (MontanaWins, round(MontanaWins / NUM_FIGHTS * 100, 2), Wins, round(DustinWins / NUM_FIGHTS * 100Dustin, 2)))

