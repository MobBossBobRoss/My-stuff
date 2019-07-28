import random
print('**********************************')
print('*Welcome to the Eternal Gauntlet!*')
print('**********************************')
input()


class Mage:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Range:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Melee:
    def __init__(self, name, damage):
        self.name = name
        self.damage = damage


class Monsters:
    def __init__(self, name, health):
        self.name = name
        self.health = health

# Weapon definitions
basic_sword = Melee('hefty stick', 7)
basic_flail = Melee('pillowcase full of rocks', 9)
basic_dagger = Melee('rusty old knife', 5)
basic_staff = Mage('slightly magical stick', 11)
basic_wand = Mage('glowing twig', 8)
basic_book = Mage('Book of Magical Mischief', 6)
basic_slingshot = Range('old slingshot', 5)
basic_bow = Range('cracked wooden bow', 7)
basic_throwing = Range('bag of good lookin\' rocks', 9)
# Monster definitions
weak_orc = Monsters('hungry goblin', 10)
weak_dragon = Monsters('baby dragon', 14)
weak_beastman = Monsters('rat man', 12)

def monstergen():
    if playerlevel <4:
        roll = random.randint(1, 3)
        if roll == 1:
            return weak_orc
        elif roll == 2:
            return weak_beastman
        elif roll == 3:
            return weak_dragon
   # elif 8 > playerlevel > 3:
       # roll = random.randint(1,3)
   # elif playerlevel >= 8:
       # roll = random.randint(1,3)

starting_items = ['slightly magical stick', 'glowing twig', 'Book of Magical Mischief',
                  'old slingshot', 'cracked wooden bow', 'bag of good lookin\' rocks',
                  'hefty branch', 'pillowcase full of rocks', 'rusty old knife']

inventory = []
playerlevel = 1
levelprogress = 0
classresult = random.randint(0, 8)

# Class and starting weapon roll

while True:
    if classresult <= 2:
        weaponresult = random.randint(1,3)
        if weaponresult == 1:
            print('You are a wizard with a ' + basic_staff.name + '.')
            inventory.append(basic_staff)
        elif weaponresult == 2:
            print('You are a wizard with a ' + basic_wand.name + '.')
            inventory.append(basic_wand)
        elif weaponresult == 3:
            print('You are a wizard with a ' + basic_book.name + '.')
            inventory.append(basic_book)
        break
    elif 2 < classresult < 6:
        weaponresult = random.randint(1,3)
        if weaponresult == 1:
            print('You are a ranger with a ' + basic_slingshot.name + '.')
            inventory.append(basic_slingshot)
        elif weaponresult == 2:
            print('You are a ranger with a ' + basic_bow.name + '.')
            inventory.append(basic_bow)
        elif weaponresult == 3:
            print('You are a ranger with a ' + basic_throwing.name + '.')
            inventory.append(basic_throwing)
        break
    elif classresult >= 6:
        weaponresult = random.randint(1,3)
        if weaponresult == 1:
            print('You are a warrior with a ' + basic_sword.name + '.')
            inventory.append(basic_sword)
        elif weaponresult == 2:
            print('You are a warrior with a ' + basic_flail.name + '.')
            inventory.append(basic_flail)
        elif weaponresult == 3:
            print('You are a warrior with a ' + basic_dagger.name + '.')
            inventory.append(basic_dagger)
        break

equipped = inventory[0]

# Main game loop

while True:
    print('Enter \"i\" for your inventory, any other key to continue to the next fight.')
    i = input()
    if i == 'i':
        for item in range(len(inventory)):
            print(inventory[item].name)
        print( '\nEnter the name of the item to equip, or enter \'back\' to stop.')
        i = input()
        for item in range(len(inventory)):
            if i.lower() in inventory[item].name.lower():
                equipped = inventory[item]
                print(equipped.name + ' is now equipped.')
    monster = monstergen()
    monsterhealth = monster.health
    print('A ' + monster.name + ' attacks you!\n')
    while monsterhealth > 0:
        print('The ' + monster.name + ' has ' + str(monsterhealth) + ' hp remaining.')
        print('Press enter to attack, enter \'Q\' to give up.')
        response = input()
        if response == '':
            monsterhealth -= equipped.damage
        if monsterhealth <= 0:
            print('The ' + monster.name + ' dies!')
            levelprogress += 1



