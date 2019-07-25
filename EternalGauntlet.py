import random

print('Welcome to the Eternal Gauntlet!\nPress any button to begin.')
input()

starting_items = ['slightly magical stick', 'glowing twig', 'Book of Magical Mischief',
                  'old slingshot', 'cracked wooden bow', 'bag of good lookin\' rocks',
                  'hefty branch', 'pillowcase full of rocks', 'rusty old knife']

classresult = random.randint(0, 8)
while True:
    if classresult <= 2:
        print('You are a wizard with a ' + starting_items[classresult] + '.')
        playerclass = 'Wizard'
        break
    elif 2 < classresult < 6:
        print('You are a ranger with a ' + starting_items[classresult] + '.')
        playerclass = 'Ranger'
        break
    elif classresult >= 6:
        print('You are a fighter with a ' + starting_items[classresult] + '.')
        playerclass = 'Fighter'
        break
