import random
import os
import pickle
print('**************************************************************')
print('***************Welcome to the Eternal Gauntlet!***************')
print('**************************************************************')
input('> ')


class Mage:
    def __init__(self, name, damage=None):
        self.name = name
        self.damage = damage


class Range:
    def __init__(self, name, damage=None):
        self.name = name
        self.damage = damage


class Melee:
    def __init__(self, name, damage=None):
        self.name = name
        self.damage = damage


# Melee weapons
basic_sword = Melee('hefty stick', 7)
basic_flail = Melee('pillowcase full of rocks', 9)
basic_dagger = Melee('rusty old knife', 5)
medium_sword = Melee('crude iron sword', 12)
medium_flail = Melee('old iron flail', 14)
# Mage weapons
basic_staff = Mage('slightly magical stick', 10)
basic_wand = Mage('glowing twig', 8)
basic_book = Mage('Book of Magical Mischief', 6)
medium_wand = Mage('apprentice wand', 15)
medium_staff = Mage('battlestaff', 18)
# Range weapons
basic_slingshot = Range('old slingshot', 4)
basic_bow = Range('cracked wooden bow', 6)
basic_throwing = Range('bag of good lookin\' rocks', 9)
medium_bow = Range('yew shortbow', 11)
medium_throwing = Range('bag of throwing axes', 14)

class Potions:
    def __init__(self,name, hp, mana):
        self.name = name
        self.hp = hp
        self.mana = mana


# Potion Definitions
small_health = Potions('small hp potion', 10, 0)
med_health = Potions('medium hp potion', 20, 0)
high_health = Potions('large hp potion', 40, 0)


class RandDrops:
    def __init__(self, lowmage, medmage, highmage,
                       lowrange, medrange, highrange,
                       lowmel, medmel, highmel):

        self.lowmage = lowmage
        self.medmage = medmage
        self.highmage = highmage
        self.lowrange = lowrange
        self.medrange = medrange
        self.highrange = highrange
        self.lowmel = lowmel
        self.medmel = medmel
        self.highmel = highmel


# Universal Drop Table
droptable = RandDrops([small_health, basic_wand, basic_staff],    # Beginner mage drops

                      [med_health, medium_wand, medium_staff],    # Apprentice mage drops

                      [high_health],                              # Experienced mage drops

                      [small_health, basic_bow, basic_throwing],  # Beginner ranger drops

                      [med_health, medium_bow, medium_throwing],  # Apprentice ranger drops

                      [high_health],                              # Experienced ranger drops

                      [small_health, basic_sword, basic_flail],   # Beginner warrior drops

                      [med_health, medium_sword, medium_flail],   # Apprentice warrior drops

                      [high_health])                              # Experienced warrior drops


class Monsters:
    def __init__(self, name, health, damage,):
        self.name = name
        self.health = health
        self.damage = damage
       # self.drops = drops


# Monster definitions
weak_orc = Monsters('hungry goblin', 10, 5)
weak_dragon = Monsters('baby dragon', 14, 8)
weak_beastman = Monsters('rat man', 12, 6)
medium_orc = Monsters('young orc', 25, 11)
medium_dragon = Monsters('juvenile dragon', 32, 15)
medium_beastman = Monsters('lizard man', 28, 12)

class Playerchar:
    def __init__(self, name, health, equipped, inventory, level, levelprogress, caste, killcount):
        self.name = name
        self.health = health
        self.equipped = equipped
        self.inventory = inventory
        self.level = level
        self.levelprogress = levelprogress
        self.caste = caste
        self.killcount = killcount


# Player info
player = Playerchar('', 0, None, [], 1, 0, '', 0)


def monstergen():
    roll = random.randint(1, 3)
    if player.level < 4:
        if roll == 1:
            return weak_orc
        elif roll == 2:
            return weak_beastman
        elif roll == 3:
            return weak_dragon
    elif 7 > player.level > 3:
        if roll == 1:
            return medium_orc
        elif roll == 2:
            return medium_beastman
        elif roll == 3:
            return medium_dragon
       # elif playerlevel >= 7:


def charroll():
    while True:
        classresult = random.randint(0, 8)
        if classresult <= 2:
                weaponresult = random.randint(1, 3)
                if weaponresult == 1:
                    print('You are a wizard with a ' + basic_staff.name + '.')
                    player.inventory.append(basic_staff)
                elif weaponresult == 2:
                    print('You are a wizard with a ' + basic_wand.name + '.')
                    player.inventory.append(basic_wand)
                elif weaponresult == 3:
                    print('You are a wizard with a ' + basic_book.name + '.')
                    player.inventory.append(basic_book)
                player.caste = 'Wizard'
                player.equipped = player.inventory[0]
                player.health = 25
                break
        elif 2 < classresult < 6:
                weaponresult = random.randint(1, 3)
                if weaponresult == 1:
                    print('You are a ranger with a ' + basic_slingshot.name + '.')
                    player.inventory.append(basic_slingshot)
                elif weaponresult == 2:
                    print('You are a ranger with a ' + basic_bow.name + '.')
                    player.inventory.append(basic_bow)
                elif weaponresult == 3:
                    print('You are a ranger with a ' + basic_throwing.name + '.')
                    player.inventory.append(basic_throwing)
                player.caste = 'Ranger'
                player.equipped = player.inventory[0]
                player.health = 30
                break
        elif classresult >= 6:
                weaponresult = random.randint(1, 3)
                if weaponresult == 1:
                    print('You are a warrior with a ' + basic_sword.name + '.')
                    player.inventory.append(basic_sword)
                elif weaponresult == 2:
                    print('You are a warrior with a ' + basic_flail.name + '.')
                    player.inventory.append(basic_flail)
                elif weaponresult == 3:
                    print('You are a warrior with a ' + basic_dagger.name + '.')
                    player.inventory.append(basic_dagger)
                player.caste = 'Warrior'
                player.equipped = player.inventory[0]
                player.health = 40
                break
    print('\nPlease enter a name for your character.')
    player.name = input('> ')


def invmanage():
        while True:
            print('Enter \"i\" for your inventory, \"c\" for your info, any other key to continue to the next fight.')
            i = input('> ')
            if i.lower() == 'i':
                while True:
                    print(''.center(50, '.'))
                    print('INVENTORY'.center(50, '.'))
                    for item in range(len(player.inventory)):
                        if player.inventory[item] == player.equipped:
                            print('> {.name}(E) <'.format(player.inventory[item]).center(50, '.'))
                        else:
                            print('> {.name} <'.format(player.inventory[item]).center(50, '.'))
                    print(''.center(50, '.'))
                    print('\nEnter the name of the item to equip/use, or enter \'back\' to stop.')
                    i = input('> ')
                    if i == 'back':
                        break
                    for item in range(len(player.inventory)):
                        if i.lower() in player.inventory[item].name.lower():
                            if hasattr(player.inventory[item], 'hp'):
                                player.health += player.inventory[item].hp
                                print('You drink the {0.name}. It increases your hp to {1.health}'
                                      .format(player.inventory[item], player))
                                player.inventory.remove(player.inventory[item])
                                savegame()
                                input('Press enter to continue.')
                                break
                            else:
                                player.equipped = player.inventory[item]
                                print('{0.name} is now equipped.'.format(player.equipped))
                                savegame()
                                break
            elif i.lower() == 'c':
                print('''                 Your name is {0.name}.\n
                 You are a {0.caste}.\n
                 You are level {0.level}.\n
                 You are holding a {0.equipped.name}.\n
                 You have {0.health} hp.\n
                 You have killed {0.killcount} monsters.
                 '''.format(player))
            else:
                while True:
                    print('Are you sure you want to continue? y/n')
                    i = input('> ')
                    if i == 'y':
                        return
                    elif i == 'n':
                        break



def battle():
    monster = monstergen()
    monsterhealth = monster.health
    print('A {0.name} appears!\n'.format(monster))
    while monsterhealth > 0:
        print('You have ' + str(player.health) + ' hp remaining.')
        print('The {0.name} has {1} hp remaining.\n'.format(monster, int(monsterhealth)))
        print('Press enter to attack, enter \'Q\' to give up.')
        response = input('> ')
        if response == '':
            damage = player.equipped.damage * random.uniform(0.5, 2)
            monsterhealth -= int(damage)
            print('You deal {0} damage!'.format(int(damage)))
        if monsterhealth > 0:
            player.health -= monster.damage
            print('The {0.name} hits you for {0.damage} damage!\n'.format(monster))
        if player.health <= 0:
                print('You die...')
                input('> ')
                break
        if monsterhealth <= 0:
            print('The ' + monster.name + ' dies!\n')
            player.killcount += 1
            player.levelprogress += 1
            if player.levelprogress == 3:
                player.level += 1
                print('You have leveled up! You are now level {0}'.format(player.level))
                player.levelprogress = 0
            dropgen(player.level, player.caste)


def dropgen(level, caste):
    if level <= 3:
        roll = random.randint(1, 100)
        if caste == 'Wizard':
            if roll > 25:
                player.inventory.append(droptable.lowmage[0])
                print('You find a {.name}\n'.format(droptable.lowmage[0]))
            if 90 > roll > 60:
                if droptable.lowmage[1] not in player.inventory:
                    player.inventory.append(droptable.lowmage[1])
                    print('You also find a {.name}\n'.format(droptable.lowmage[1]))
            if roll >= 90:
                if droptable.lowmage[2] not in player.inventory:
                    player.inventory.append(droptable.lowmage[2])
                    print('You also find a {.name}\n'.format(droptable.lowmage[2]))
        if caste == 'Ranger':
            if roll > 25:
                player.inventory.append(droptable.lowrange[0])
                print('You find a {.name}\n'.format(droptable.lowrange[0]))
            if 90 > roll > 60:
                if droptable.lowrange[1] not in player.inventory:
                    player.inventory.append(droptable.lowrange[1])
                    print('You also find a {.name}\n'.format(droptable.lowrange[1]))
            if roll >= 90:
                if droptable.lowrange[2] not in player.inventory:
                    player.inventory.append(droptable.lowrange[2])
                    print('You also find a {.name}\n'.format(droptable.lowrange[2]))
        if caste == 'Warrior':
            if roll > 25:
                player.inventory.append(droptable.lowmel[0])
                print('You find a {.name}\n'.format(droptable.lowmel[0]))
            if 90 > roll > 60:
                if droptable.lowmel[1] not in player.inventory:
                    player.inventory.append(droptable.lowmel[1])
                    print('You also find a {.name}\n'.format(droptable.lowmel[1]))
            if roll >= 90:
                if droptable.lowmel[2] not in player.inventory:
                    player.inventory.append(droptable.lowmel[2])
                    print('You also find a {.name}\n'.format(droptable.lowmel[2]))
    if 7 > level > 3:
        roll = random.randint(1, 100)
        if caste == 'Wizard':
            if roll > 25:
                player.inventory.append(droptable.medmage[0])
                print('You find a {.name}\n'.format(droptable.medmage[0]))
            if 90 > roll > 60:
                if droptable.medmage[1] not in player.inventory:
                    player.inventory.append(droptable.medmage[1])
                    print('You also find a {.name}\n'.format(droptable.medmage[1]))
            if roll >= 90:
                if droptable.medmage[2] not in player.inventory:
                    player.inventory.append(droptable.medmage[2])
                    print('You also find a {.name}\n'.format(droptable.medmage[2]))
        if caste == 'Ranger':
            if roll > 25:
                player.inventory.append(droptable.medrange[0])
                print('You find a {.name}\n'.format(droptable.medrange[0]))
            if 90 > roll > 60:
                if droptable.medrange[1] not in player.inventory:
                    player.inventory.append(droptable.medrange[1])
                    print('You also find a {.name}\n'.format(droptable.medrange[1]))
            if roll >= 90:
                if droptable.medrange[2] not in player.inventory:
                    player.inventory.append(droptable.medrange[2])
                    print('You also find a {.name}\n'.format(droptable.medrange[2]))
        if caste == 'Warrior':
            if roll > 25:
                player.inventory.append(droptable.medmel[0])
                print('You find a {.name}\n'.format(droptable.medmel[0]))
            if 90 > roll > 60:
                if droptable.medmel[1] not in player.inventory:
                    player.inventory.append(droptable.medmel[1])
                    print('You also find a {.name}\n'.format(droptable.medmel[1]))
            if roll >= 90:
                if droptable.medmel[2] not in player.inventory:
                    player.inventory.append(droptable.medmel[2])
                    print('You also find a {.name}\n'.format(droptable.medmel[2]))


def savegame():
    with open('.\\saves\\gamesave.dat', 'wb') as s:
        pickle.dump(player, s)


# Main game loop
if os.path.exists('.\\saves\\gamesave.dat'):
    while True:
        print('Enter \'c\' to continue game, \'n\' for new game.')
        r = input('> ')
        if r == 'c':
            with open('.\\saves\\gamesave.dat', 'rb') as s:
                player = pickle.load(s)
            break
        if r == 'n':
            charroll()
            break
else:
    charroll()
while player.health > 0:
    invmanage()
    battle()
    savegame()
print('############')
print('#GAME OVER#')
print('############')



