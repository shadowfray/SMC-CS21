#Benjamin Jewell
#CS 21 2018
#Text-based-dungeon

'''
The idea of The Keep of The Dreamer is a short text based adventure game where
you explore a set of interconnected rooms in search of treasure. The character
can move between the game's 5 total rooms, and can backtrack and move on the
grid however they like. Text input is the only way to interface with the game,
and a set of list of actions for each room has been provided. Some of the items
and objects in each of the rooms can only be interacted with if certain conditions
have been met, say you pulled a lever in the next room or are carrying the key to
the door. To make this work, each of the rooms is it's own function, allowing for
easy branching between each chamber. Each room has it's own set list of what you
can and can't interact with, and the actions in the room maybe be able to even
affect other rooms. As such, the list of events and inventory are passed between
room as parameters so that the game can use them as a way to check what has and
has not been done. 
'''

import random
import time

#The main function simply serves as a way to start the game, inform the players
#of the controls, and to get the game running by starting the first room.
#It takes no parameters. It has a small loading screen for the fun of it.
def main():
    print('THE KEEP OF THE DREAMER [v1.2]')
    print('')
    print('LOADING...')
    print('[', end='')
    #A fun little loading screen 
    for i in range(50):
        a = 0.1 * random.random()
        time.sleep(a)
        print('=', end='')
    print(']')
    print('To interact with an item, simply write the items name. To interact')
    print('with an object, simply write the name of the object. An input of')
    print('"commands" will display all avaliable commands. "inventory" displays')
    print('your current inventory')
    print('')
    print('You have journeyed far across the lands of Skelen,  travelling far  to')
    print('the north,  at the base of the frigid Wor Mountains,  where the fabled')
    print('Amulet of Paryuth is said to be kept. Such an item could bring hope to')
    print('your people in the battle against the dreaded Kalrok the Undying.')
    print('As you press on, you see at the end of the road,  a small ancient stone')
    print('keep set in the side of the mountain. The place is worn with age,  with')
    print('a decrepit outer wall made of crumbling masonry lining the exterior.  A')
    print('rotted wooden tower sags to one side, overlooking the small courtyard.')
    print('======================================================================')
    print('')

    score = []
    #All possible items that can be picked up
    inventory = {'ring':False, 'scroll':False, 'oil':False, 'rag': False, 'cup':False, 'knife':False, 'sapphire':False, 'amulet': False}
    #All possible events that can affect other rooms
    events_dict = {'bridge':False, 'seal': False, 'rag':False}
    room22(inventory, events_dict, score)
    


'''
The command function serves as a way for players to know what they can and cannot
do. While it is not an overly complex piece of code, it is used in every room and
thus saves time and space. It takes a single parameter, the dictionary of available
actions in each room, and iterates over the keys that have a value of True and
printing them out to the user. 
'''
def commands(room_items):
    print('Commands:', end=' ')
    #This loops over each comamnd, checks if they're true
    #(aka visible to the player) and prints them if they are
    for i in room_items:
        if room_items[i] == True:
            print(i,',', end=' ')
    print('')

'''
The inventory_display() function will take one parameter, the inventory of the player,
and prints it out for them to see. This is used as a function to save space in other
functions. It cycles over their inventory, only printing what they are actively carrying. 
'''
def inventory_display(inventory):
        print('Inventory:', end=' ')
        #This loops over each item in their inventory, and if they are
        #carrying it (aka it is true) then print it
        for i in inventory:
            if inventory[i] == True:
                print(i, ',', end=' ')
        print('')


def itempickup(textinput, room_commands, inventory, itemname):
    #redefines it so that the following commands below work
    romcom = room_commands
    if textinput == itemname and romcom[itemname] == True and inventory[itemname] == False:
        #return a value so that it knows what flavor text to print
        inventory[itemname] = True
        return True
    elif textinput == itemname and (romcom[itemname] == False or inventory[itemname] == True):
        print('command not recognized! Type commands for a list of commands')


        

'''
Room22 is the first room the players enter when playing the game. Since all rooms are
almost identical, this room will detail the process of all rooms. Each room has a
dictionary of available objects and items that the player can interact with, the ones
that can currently be interacted with being True, while hidden objects are False. The
dictionary also includes the 3 universal commands of the game, commands, which tells
the user what they can and cannot do, using the commands() function, the investigate
function, which reveals hidden objects and items to the user, and inventory, which
displays the current inventory of the player. From here, there is a loop that runs,
asking the user for input. If the input is is on the item list for the room, and it
is also set to true, it allows for interaction. The user picks up something, the
item will be set as True in their inventory. When moving to the next room, the next
room function will be called, passing the events dictionary and the inventory
dictionary along. Room 22 itself has a rusted lever in it that can lower the
drawbridge in Room 23 if oil from another room is used on it. There is also a blue
ring here that can absorb lightning if carried into room 14, as well as a scroll that
hints at the gem offering in Room 24. There is a gate leading here to Room 23, and
there is an exit here. You cannot leave without the amulet'
'''
def room22(inventory, events_dict, score):

    print('The courtyard you stand in is overgrown with grass and weeds,  with a')
    print('column of silverlight ivy growing up the wall.The ground beneath your')
    print('feet would be muddy in  any other season,  but the cold Skelen autumn')
    print('keeps it firm beneath your leather boots.  To the north lies a rotted')
    print('wooden gate, hanging half open,  the cold wind gently rocking it open')
    print('and closed. Under the silverlight ivy you can make out an iron lever,')
    print('rusted over,  connected to a large chain dissapearing into the wooden')
    print('loaming above you, like a monster watching its prey.')

    #the list of all avaliable commands in the room
    room22_items = {'gate':True, 'lever':True, 'ring':False, 'scroll':False, 'investigate':True, 'commands':True, 'inventory':True, 'road':False}
    #If the player has the win condition item, allow them to exit and win
    if inventory['amulet'] == True:
        print('The road away beckons to you, as the Amulet of Paryuth softly pulses')
        print('in your hand. It would be a long journey back,  but better than this')
        print('frozen keep')
        room22_items['road'] = True
        
        
    while True:
        print('')
        textinput = input('>')
        if textinput in room22_items:
            if textinput == 'gate':
                #allows for movement into the next room
                print('You move forward towards the old gate, pushing it open with a')
                print('gentle creak as you move past it.')
                room23(inventory, events_dict, score)
                #The breaks are here so that when you win or lose, you finish the game
                break

            if textinput == 'road' and room22_items['road'] == True:
                #allows you to walk down the road and win if they ahve the amulet
                end(True, score)
                break
            
            if textinput == 'investigate':
                #If they don't already have the items, allow them to find it and add
                #it to the items they can interact with in the room.
                if inventory['ring'] == False:
                    print('Among the vines you find a  small band of metal lying there')
                    print('in the mud. As you examine you realize it is a ring made of')
                    print('a brilliant blue metal, inset with small silver bands.')
                    room22_items['ring'] = True
                if inventory['scroll'] == False:
                    print('As you look through the rubble, you stumble across a tube of')
                    print('leather, a scroll case. The outside is dirty but undamaged.')
                    room22_items['scroll'] = True

            
            if textinput == 'lever':
                #If the player has the oil to interact with the lever, allow the possibility
                #of oiling it and pull it, opening the door in the next room
                if inventory['oil'] == True:
                    oilchoice = input('Would you like to oil the lever? [y/n] ')
                    if oilchoice == 'y':
                        print('Using your flask of oil,  you are able work most of  the rust off')
                        print('the old lever.  The gears seem to be in order,  and with a tug it')
                        print('easy shifts,  the chains behind it sudden whirling to life. Above')
                        print('you hear gears shift and turn in the wooden tower. A moment later')
                        print('there is a loud crash from beyond the gate.')
                        score.append(3)
                        events_dict['bridge'] = True
             
                else:
                    print('Examining the lever, you can see it has been consumed in rust, jamming')
                    print('any possibility of movement it might have had. You see the chains')
                    print('seem to be in a condition where they could easily move.')

            if textinput == 'ring':
                item = itempickup(textinput, room22_items, inventory, 'ring')
                #if the user picks up the ring, print the text for picking up the ring
                if item == True:
                    score.append(3)
                    print('You pick up the strange ring,  noticing how light it is for its size.')
                    print('As you look it over, you swear you saw a strange glint in the silver.')
                

            if textinput == 'scroll':
                item = itempickup(textinput, room22_items, inventory, 'scroll')
                if item == True:
                    score.append(1)
                    print('You reach down,  opening the scroll  case you found.  The cap comes off')
                    print('easily, and within you can see the parchment is still intact.  Reaching')
                    print('in, you pull it out, unfurling this ancient document. It seems to be an')
                    print('illustration  of some sort,  depicting several figures  gathered around')
                    print('an altar.   One of the figures offers up a brilliant blue light towards')
                    print('the heavens as a thousand eyes descend to fill the air.')
        

            #allows the user to call the commands function and print out all the commands in the room
            if textinput == 'commands':
                commands(room22_items)

            #allows the user to call the inventory function and print out the contents of their inventory
            if textinput == 'inventory':
                inventory_display(inventory)
                
        #if the command is not recognized, print an error message   
        else:
            print('command not recognized! type commands for a list of commands')
    
        
'''
Room 23 is the first impassible object, requiring the lever event in Room 22 to
be true. There is a fountain here, as well as rag and oil. The rag and oil are
useless for now, but can be used in other rooms (oil on the lever in 22, and the
rags on the hole in 34). By itself the fountain does nothing, but if you bring the
cup from Room 24, it will provide a clue that the ring can protect you from
lightning. There is a gate here going back to Room 22, and the drawbridge
going on to Room 24.This room takes 2 parameters,the inventory of the player
and the dictionary of events. 
''' 
def room23(inventory, events_dict, score):
    print('')
    print('The inner courtyard is dotted with rubble and weeds, with a deep moat along the')
    print('north side. To the east are a collection of old wooden boxes,  most broken from')
    print('wear, perfect kindling if you needed a fire.  Across from them there is a stone')
    print('bowl set into the wall,  with a grotesque face carved into the stone,  dripping')
    print('water  -  it was probably once a nice fountain. Overhead,  a chain runs through')
    print('old pipes, leading to the gatehouse from which a plank drawn bridge is connected')
    if events_dict['bridge'] == True:
        print('The drawbridge has been lowered, resting its tired wood on the mud and dirt')
    else:
        print('The old drawbridge is raised, making crossing the moat impossible')

    room23_items = {'commands':True, 'inventory':True, 'investigate':True, 'fountain':True, 'drawbridge':True, 'gate':True, 'oil' :False, 'rag':False}

    while True:
        print('')
        textinput = input('>')
        if textinput in room23_items:
            if textinput == 'drawbridge':
                #Checks if the lever in the first room has been pulled, and if so lowers the drawbridge
                #and allows them to cross it. Otherwise the moat is impassible.
                if events_dict['bridge'] == True:
                    print('You walk across the old planks, creaking beneath your feet with each')
                    print('step as you make your way into the building.')
                    room24(inventory, events_dict, score)
                    break
                else:
                    print('With the drawbridge raised, it is impossible to cross')
                    
            if textinput == 'gate':
                print('You push your way out through the gate, a blast of cold northern wind')
                print('brushing over you,  sending a chill through your skin as you walk out.')
                room22(inventory, events_dict, score)
                break


            #reveals items that can then be interacted with in the room
            if textinput == 'investigate':
                #makes sure you can't pick up an item you already have
                if inventory['oil'] == False:
                    print('Looking through the old boxes, you find tucked away is a')
                    print('small flask of oil.')
                    room23_items['oil'] = True
                if inventory['rag'] == False:
                    print('Folded up in one of the crates is a small white rag, with')
                    print('oil stains standing out against the clear cloth.')
                    room23_items['rag'] = True

            if textinput == 'oil':
                item = itempickup(textinput, room23_items, inventory, 'oil')
                if item == True:
                    print('You pick up the flask of oil, it seems to still be mostly full')
                
            if textinput == 'rag':
                item = itempickup(textinput, room23_items, inventory, 'rag')
                if item == True:
                    print('You pick up the dirty old rag, covered in oil')
              
            if textinput == 'fountain':
                print('The fountain here is formed from an old stone bowl inset into the')
                print('wall, with a grotesque face above it dripping water slowly out of')
                print('its mouth into the pool below. The water is murky and dirty,  and')
                print('probably contains some of last springs rainfall as well.')
                if inventory['cup'] == False:
                    print('You probably dont want to taint your waterskin with that.')
                    #lowers your score by 1 for drinking from the dirty water
                    score.append(-1)
                #if you have the cup you can chose to drink and recieve a vision
                elif inventory['cup'] == True:
                    cupchoice = input('Would you like to use your cup to drink from the fountain?[y/n] ')
                    if  cupchoice == 'y':
                        print('')
                        print('You reach down with the brozen cup, slowly filling it with')
                        print('the opaque water. A moment later, you down the water,  the')
                        print('cool sensation running down your throat...')
                        print('')
                        print('A moment later, you see a flash,  and there,  in your mind')
                        print('you can make out the image of a ring, made of a mysterious')
                        print('blue metal. Suddenly, lightning strikes it out of nowhere,')
                        print('but is absorbed into the metal without a single mark.')
                        #increases your score by 3
                        score.append(3)
                    else:
                        print('You turn your attention away from the fountain, disgusted')
                        print('by the mucky and opaque water.')


            if textinput == 'commands':
                commands(room23_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type commands for a list of commands')
                
'''
Room 14 has a clay sigil in it, binding the Lightning Elemental here that
electrocutes the wire to the door in Room 24. You need to break the sigil,
however if you get to close the elemental electrocutes you and you lose the
game. If you have the blue ring from room22 you are resistant to it's attacks
and are able to break the sigil, destroying the Lightning elemental.
Investigating this room reveals a sapphire. The only exit to this room
is a way back out to Room 24.This room takes 2 parameters, the inventory of
the player and the dictionary of events. 
'''
def room14(inventory, events_dict, score):
    #One can enrage the elemental by bugging it too much, this keeps track of that
    elementalrage = 0
    
    print('This cylindrical chamber is almost completely bare, save for a skylight')
    print('above, where the faded northern light shines in. Next to it, old chains')
    print('hang,  all connecting to the exposed  metal wire running down along the')
    print('old staircase in the east wall.')
    #if the elemental is still here, describe it
    if events_dict['seal'] == False:
        print('Hovering in the middle of the room is a creature composed out of pure')
        print('electricity,  lightning arcing from it  about the chamber.  It floats')
        print('above a clay sigil on the floor,  and seems to be arcing lightning on')
        print('to chains hanging from the ceiling around it, the electricity running')
        print('along a wire that descends down the staircase.')
    #otherwise the room is empty as it should be
    else:
        print('The room is quite, and in the middle lies the smashed remnants of a')
        print(' shattered clay sigil.')
    
    room14_items = {'commands': True, 'inventory': True, 'investigate': True, 'stairs':True, 'sapphire':False, 'sigil': True, 'elemental':True}

    while True:
        print('')
        textinput = input('>')
        if textinput in room14_items:
            if textinput == 'stairs':
                print('You make your way back down the old stone steps, winding back down to the chamber below.')
                room24(inventory, events_dict, score)
                break

            if textinput == 'investigate':
                print('You cant find anything, and that lightning elemental keeps starring at you')
                print('You notice the lightning elemental seems to be bound to the clay sigil...')

            #The elemental doesn't want to fight initially, but if you disturb it enough (4 times) it
            #will eventually attack and kill you
            if textinput == 'elemental' and events_dict['seal'] == False:
                elementalrage += 1
                if elementalrage < 3:
                    print('The elemental starts to flicker and hiss as you approach, its probably a good idea to stay back')
                elif elementalrage == 3:
                    print('The elemental is really starting to look angry! It shoots a bolt of')
                    print('lightning over your head as a warning!')
                elif elementalrage > 3:
                    print('The elemental shots a bolt of lightning at you!')
                    #if you have the ring it absorbs the lightning, saving your life
                    if inventory['ring'] == True:
                        print('The ring seems to absorb the majority of the lightning blast!')
                    else:
                        print('The lightning zaps you, killing you instantly!')
                        #if the elemental kills you, lose 5 points
                        score.append(-5)
                        #With your death you lose the game
                        end(False, score)
                        break

            #Makes sure you haven't already broken the sigil
            if textinput == 'sigil' and events_dict['seal'] == False:
                if inventory['ring'] == True:
                    print('The lightning elemental zaps lightning at you, but the ring you carry abosorbs it all')
                    print('You smash the sigil, and with a pop, the lightning elemental vanishes,')
                    print('absorbed into a brilliant blue gemstone')
                    #unlocks the door in room 24
                    events_dict['seal'] = True
                    #for destroying the elemental you gain 6 points
                    score.append(6)
                    #Allows you to pick up the sapphire that appears when the elemental dies
                    room14_items['sapphire'] = True
                    
                else:
                    #if you don't have the ring you can try to press onward but you will be slain
                    #the choice here is to avoid instant player death
                    lightningchoice = input('The lightning elemental shots a warning blast at you! Do you press onward?[y/n] ')
                    if lightningchoice == 'y':
                        print('The lightning elemental zaps you, vaporizing you and all your possessions!')
                        #once more, getting killed by the elemental loses you 5 points
                        #and you lose the game
                        score.append(-5)
                        end(False, score)
                        break
                    else:
                        print('You back away from the lightning elemental')

            if textinput == 'sapphire':
                item = itempickup(textinput, room14_items, inventory, 'sapphire')
                if item == True:
                    print('You pick up the brilliant sapphire')
                
            if textinput == 'commands':
                commands(room14_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type commands for a list of commands')
                
'''
Room 24 is the first branching path in the game. There is a staircase and a door covered
in lightning, with a cable going up the stairs. Trying to go through the door will electrocute
you and kill you, and as such one must go up to Room 14 to stop it. The other feature in here
is an altar with a dagger and a cup on it, each which can be picked up. Examining the altar
while holding the sapphire from Room 14 will show a vision of the trap around The Amulet,
asking if the user wants to offer their sapphire on the altar. The three exits are the
drawbridge (23), the stairs (14) and the door (34).This room takes 2 parameters, the
inventory of the player and the dictionary of events. 
'''
def room24(inventory, events_dict, score):
    print('The room here is dark, the only light shinning in over the drawbridge to the')
    print('south,  casting a dim light over the masonry of the walls.  On the back wall')
    print('sits an old stone altar set against the wall,drapped over with a embroidered')
    print('blue cloth.  Other old cloth is piled on top,  perhaps old robes or flags to')
    print('some long gone lord. To the west,  set into the wall is an arch way,  with a')
    print('staircase leading up into a tower above. A wire leads from it, running along')
    print('the ceiling to the metal door on the east wall.', end=' ')
    #change the description depending on what took place in room14
    if events_dict['seal'] == False:
        print('Lightning arcs from it, humming with deadly static')
    elif events_dict['seal'] == True:
        print('The door is quiet')

    room24_items = {'commands': True, 'inventory': True, 'investigate': True, 'stairs':True, 'door':True, 'drawbridge': True, 'knife': False, 'cup':False, 'altar': True}

    while True:
        print('')
        textinput = input('>')
        if textinput in room24_items:
            if textinput == 'drawbridge':
                print('You walk back across the drawbridge, the wooden plank creaking')
                print('under each step, and the chains groaning.')
                room23(inventory, events_dict, score)
                break
            
            if textinput == 'stairs':
                print('You ascend up the old stone staircase up the tower. You hear a')
                print('crackling above')
                room14(inventory, events_dict, score)
                break
            
            if textinput == 'door':
                #controls if the door is electrified and if it kills you or not
                if events_dict['seal'] == True:
                    print('You pull the door open, it swings easily on its well oiled')
                    print('hinges, revealing a glowing light beyond.')
                    room34(inventory, events_dict, score)
                    break
                else:
                    doorchoice = input('The door is electrified, do you want to try to open it?[y/n] ')
                    if doorchoice == 'y':
                        #If you go forward and touch the door, since the ring absorbs lightning
                        #it can save your life as seen below
                        if inventory['ring'] == True:
                            print('The door zaps you, but the blue ring absorbs all the lightning.')
                            print('However, the door still seems stuck, perhaps by magnets powered')
                            print('by the elementals lightning.')
                        else:
                            print('The door is stuck and electrifies you!')
                            print('Everything goes black as you fall to the floor...')
                            score.append(-5)
                            end(False, score)
                            break
                    else:
                        print('you step back from the door and turn your attention to the rest of the room')

            if textinput == 'investigate':
                if inventory['cup'] == False: 
                    room24_items['cup'] = True
                    print('Searching through the cloth on the altar, you find an ornate bronze')
                    print('cup knocked over, the inside stained with some old dried liquid.')
                    
                if inventory['knife'] == False:
                    room24_items['knife'] = True
                    print('A steel knife lies on the stone altar, hidden under the bundles of cloth')

            if textinput == 'knife':
                item = itempickup(textinput, room24_items, inventory, 'knife')
                if item == True:
                    print('You pick up the steel dagger')
                

            if textinput == 'cup':
                item = itempickup(textinput, room24_items, inventory, 'cup')
                if item == True:
                    print('You pick up the ornate bronze cup')

            if textinput == 'altar':
                print('There is an ornate altar here')
                #if you have the gem you may place it on the altar for a special vision
                if inventory['sapphire'] == True:
                    sapphirechoice = input('do you want to place the sapphire on the altar?[y/n] ')
                    #If you place the sapphire on the altar it dissapears and you get a clue
                    if sapphirechoice == 'y':
                        print('you gently place the sapphire on the altar...')
                        inventory['sapphire'] = False
                        print('The sapphire is suddenly consumed in a flash of light, cracking into burnt glass')
                        print('Your mind is suddenly filled with a vision!  Before you there is an altar, above')
                        print('floats a glowing ornate amulet, shaped like an unblinking eye.  Your vision then')
                        print('focuses on a small hole in the wall, and you get a sense of death, of a chocking')
                        print('feeling filling your lungs.')
                        print('You suddenly wake, and find yourself lying on the altar...')
                        #seeing this vision gets you 5 points
                        score.append(5)
                    else:
                        print('You step away from the altar, turning your attention back on the room')

            if textinput == 'commands':
                commands(room24_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type commands for a list of commands')
                
'''
Room 34 is the final room of the game, and contains the amulet the player is seeking. Simply rushing in and
grabbing the amulet triggers a poison gas trap, killing the player and losing the game. One can use the rag
from room 23 to clog it up. Once the user has the amulet, they can leave from room22 without losing the
game. The only way out is the door back into room 24. This room takes 2 parameters, the inventory of the
player and the dictionary of events. 
'''
def room34(inventory, events_dict, score):
    print('The walls of this room are covered in tapestries, faded with age,')
    print('hidding  the cold stone walls.  In the center of the back wall is')
    print('an altar, covered with engraved stone runes.  Above it,  floating')
    print('midair is a glowing amulet, made of ornate metal, shaped into the')
    print('form of an ublinking eye, with a chain of silver tied to it seems')
    print('sway in some ethereal breeze.  A soft silver radiance shines from')
    print('the amulet, faintly filling the room.  Behind you the door slowly')
    print('creaks shut on the west wall.')
    
    room34_items = {'amulet':True, 'investigate':True, 'commands':True, 'inventory':True, 'hole':False, 'tapestries': True, 'door':True}
    #controls the death timer of the player in regards to the point timer
    poisontimer, poison = False, 0

    while True:
        print('')
        textinput = input('>')
        #if the player it poisoned, it controls how long it is before they die
        #Since this timer is not passed between room, the player can survive by running out of the
        #poison cloud into the other room if they do that immediatly
        if poisontimer == True:
            poison += 1
            #after 1 set of actions, the player dies to the poison, loosing the game and 3 points
            if poison > 1:
                print('You cough up blood as the poison burns your lungs and you suddenly fall to the ground dead')
                end(False, score)
                score.append(-3)
                break
        
        if textinput in room34_items:
            if textinput == 'door':
                print('You step out of the room back through the old metal door you came in through')
                room24(inventory, events_dict, score)
                break
            
            if textinput == 'investigate':
                room34_items['hole'] = True
                print('you discover a small hole in the wall above the amulet, about the size of a pencil')
                print('tucked in between the tapestries')

            if textinput == 'tapestries':
                print('You examine the tapestries, depicting scenes of religious monks and knights.')
                print('Above it all, there is a large eye,  watching all.  Within the iris a figure')
                print('a figure slumbers, a golden tree growing from their mind.  Below the eye, an')
                print('amulet slowly descends to a  holy figure below,  similar to the one found on')
                print('the altar here.')
                #investigating the tapestries gets you 1 point
                score.append(1)

            if textinput == 'hole':
                #This hole is where the poison gas comes from, and one
                #can plug it with the rags they have to stop the poison
                print('you find a small hole, smelling of rotten eggs and smoke')
                if inventory['rag'] == True:
                    ragchoice = input('Would you like to stuff it with the rag?[y/n] ')
                    if ragchoice == 'y':
                        print('You stuff the hole with the rag')
                        events_dict['rag'] = True
                    else:
                        print('Your attention shifts away from the small hole towards the glowing amulet')

            if textinput == 'amulet' and inventory['amulet'] == False:
                #If the player has not disabled the poison trap, it is activated and they do not
                #pick up the amulet
                if events_dict['rag'] == True:
                    print('You grab The Amulet of Paryuth off the altar...it glows in your hand')
                    print('and pulses with a faint warmth')
                    #picking up the amulet is worth 10 points
                    score.append(10)
                    inventory['amulet'] = True
                else:
                    print('As you touch the amulet, there is a sudden hiss as from a small hole')
                    print('in the wall a cloud of poisonous gas fills your head...')
                    poisontimer = True
                    score.append(-5)
            
            if textinput == 'commands':
                commands(room34_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type commands for a list of commands')

'''
This function is run when the game is over. It tells the user if they have won or
lost the game, based on what they have done. It takes a single Boolean value
parameter to tell if it is a win or loss.
'''
def end(win, score):
    totscore = 0
    if win == True:
        score.append(20)
        print('you walk down the road, back to civilization, with the amulet of paryuth in your hands')
        print('You Win!')
        print('')
    else:
        print('You lose!')
        print('')
    #Takes the sum of the player score and then prints it (max score = 52)
    for i in score:
        totscore += int(i)
    print('SCORE: ', totscore)
    time.sleep(5)
    print('type "main()" to play again!')
        
main()
