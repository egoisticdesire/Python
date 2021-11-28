player = {
    'name': input('Enter your name: '),
    'health': 100,
    'damage': 40,
    'armor': 1.3
}

enemy = {
    'name': 'Werwolf',
    'health': 100,
    'damage': 50,
    'armor': 1.2
}


def attack(hero, target):
    def armor_attack(damage, armor):
        return round(damage / armor, 2)

    dmg = armor_attack(hero['damage'], target['armor'])
    target['health'] -= dmg
    return target


print(attack(player, enemy))
print(attack(enemy, player))
