class Intro():
    print('What be thy name.')
    Name = input()
    print(Name + "... Thats a dumb name.")
    print('What be thy class? classes be that of Dolphin, and Puffer')
    Class = input()
    if not (Class == 'Dolphin' or 'Puffer'):
        print("Thats not a class.")
    elif (Class == 'Puffer'):
        print("Watch out for Dolphins.")