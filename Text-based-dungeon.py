#Benjamin Jewell
#CS 21 2018
#Text-based-dungeon

'''

'''

def main():
    print('Welcome to the adventure!')
    print('To interact with an item, simply write the items name. To interact')
    print('with an object, simply write the name of the object. An input of')
    print('"Help" will display all avaliable commands. "Inventory" displays your')
    print('current inventory')
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

    inventory = {'ring':False, 'scroll':False, 'oil':False, 'rag': False, 'cup':False, 'knife':False, 'sapphire':False, 'amulet': False}
    events_dict = {'bridge':False, 'seal': False, 'rag':False}
    room22(inventory, events_dict)

def Help(room_items):
    print('Help:', end=' ')
    for i in room_items:
        if room_items[i] == True:
            print(i,',', end=' ')
    print('')

def inventory_display(inventory):
        print('Inventory:', end=' ')
        for i in inventory:
            if inventory[i] == True:
                print(i, ',', end=' ')
        print('')
        

def room22(inventory, events_dict):

    print('The courtyard you stand in is overgrown with grass and weeds,  with a')
    print('column of silverlight ivy growing up the wall.The ground beneath your')
    print('feet would be muddy in  any other season,  but the cold Skelen autumn')
    print('keeps it firm beneath your leather boots.  To the north lies a rotted')
    print('wooden gate, hanging half open,  the cold wind gently rocking it open')
    print('and closed. Under the silverlight ivy you can make out an iron lever,')
    print('rusted over,  connected to a large chain dissapearing into the wooden')
    print('loaming above you, like a monster watching its prey.')
    print('')
          

    room22_items = {'gate':True, 'lever':True, 'ring':False, 'scroll':False, 'investigate':True, 'Help':True, 'inventory':True, 'road':False}
    if inventory['amulet'] == True:
        print('The road away beacons to you, as the Amulet of Paryuth softly pulses')
        print('in your hand. It would be a long journey back,  but better than this')
        print('frozen keep')
        room22_items['road'] = True
        
        
    while True:
        print('')
        textinput = input('>')
        if textinput in room22_items:
            if textinput == 'gate':
                print('You move forward towards the old gate, pushing it open with a')
                print('gentle creak as you move past it.')
                room23(inventory, events_dict)
                break

            if textinput == 'road' and room22_items['road'] == True:
                end(True)
                break
            
            if textinput == 'investigate':
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
                if inventory['oil'] == True:
                    oilchoice = input('Would you like to oil the lever? [y/n]')
                    if oilchoice == 'y':
                        print('Using your flask of oil,  you are able work most of  the rust off')
                        print('the old lever.  The gears seem to be in order,  and with a tug it')
                        print('easy shifts,  the chains behind it sudden whirling to life. Above')
                        print('you hear gears shift and turn in the wooden tower. A moment later')
                        print('there is a loud crash from beyond the gate.')
                        events_dict['bridge'] = True
             
                else:
                    print('Examining the lever, you can see it has been consumed in rust, jamming')
                    print('any possibility of movement it might have had. You see the chains')
                    print('seem to be in a condition where they could easily move.')
                
                
            if textinput == 'ring' and room22_items['ring'] == True and inventory['ring'] == False:
                print('You pick up the strange ring,  noticing how light it is for its size.')
                print('As you look it over, you swear you saw a strange glint in the silver.')
                inventory['ring'] = True
            elif textinput == 'ring' and (room22_items['ring'] == False or inventory['ring'] == True):
                print('command not recognized! Type Help for a list of commands')

            if textinput == 'scroll' and room22_items['scroll'] == True and inventory['scroll'] == False:
                print('You reach down,  opening the scroll  case you found.  The cap comes off')
                print('easily, and within you can see the parchment is still intact.  Reaching')
                print('in, you pull it out, unfurling this ancient document. It seems to be an')
                print('illustration  of some sort,  depicting several figures  gathered around')
                print('an altar.   One of the figures offers up a brilliant blue light towards')
                print('the heavens as a thousand eyes descend to fill the air.')
                inventory['scroll'] = True
            elif textinput == 'scroll' and (room22_items['scroll'] == False or inventory['scroll'] == True):
                print('command not recognized! Type Help for a list of commands')

            if textinput == 'Help':
                Help(room22_items)
                
            if textinput == 'inventory':
                inventory_display(inventory)
                
                
        else:
            print('command not recognized! type Help for a list of commands')
    
        
    
    
def room23(inventory, events_dict):
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

    events_dict = events_dict
    inventory_list = inventory
    room23_items = {'Help':True, 'inventory':True, 'investigate':True, 'fountain':True, 'drawbridge':True, 'gate':True, 'oil' :False, 'rag':False}

    while True:
        print('')
        textinput = input('>')
        if textinput in room23_items:
            if textinput == 'drawbridge':
                if events_dict['bridge'] == True:
                    print('You walk across the old planks, creaking beneath your feet with each')
                    print('step as you make your way into the building.')
                    room24(inventory, events_dict)
                    break
                else:
                    print('With the drawbridge raised, it is impossible to cross')
            if textinput == 'gate':
                print('You push your way out through the gate, a blast of cold northern wind')
                print('brushing over you,  sending a chill through your skin as you walk out')
                room22(inventory, events_dict)
                break

            if textinput == 'investigate':
                if inventory['oil'] == False:
                    print('Looking through the old boxes, you find tucked away is a')
                    print('small flask of oil.')
                    room23_items['oil'] = True
                if inventory['rag'] == False:
                    print('Folded up in one of the crates is a small white rag, with')
                    print('oil stains standing out against the clear cloth.')
                    room23_items['rag'] = True

            if textinput == 'oil' and room23_items['oil'] == True and inventory['oil'] == False:
                print('You pick up the flask of oil, it seems to still be mostly full')
                inventory['oil'] = True
            elif textinput == 'oil' and (room23_items['oil'] == False or inventory['oil'] == True):
                print('command not recognized! Type Help for a list of commands')

            if textinput == 'rag' and room23_items['rag'] == True and inventory['rag'] == False:
                print('You pick up the dirty old rag, covered in oil')
                inventory['rag'] = True
            elif textinput == 'rag' and (room23_items['rag'] == False or inventory['rag'] == True):
                print('command not recognized! Type Help for a list of commands')

            if textinput == 'fountain':
                print('The fountain here is formed from an old stone bowl inset into the')
                print('wall, with a grotesque face above it dripping water slowly out of')
                print('its mouth into the pool below. The water is murky and dirty,  and')
                print('probably contains some of last springs rainfall as well.')
                if inventory['cup'] == False:
                    print('You probably dont want to taint your waterskin with that.')
                elif inventory['cup'] == True:
                    cupchoice = input('Would you like to use your cup to drink from the fountain?[y/n] ')
                    if  cupchoice == 'y':
                        print('You reach down with the brozen cup, slowly filling it with')
                        print('the opaque water. A moment later, you down the water,  the')
                        print('cool sensation running down your throat...')
                        print('A moment later, you see a flash,  and there,  in your mind')
                        print('you can make out the image of a ring, made of a mysterious')
                        print('blue metal. Suddenly, lightning strikes it out of nowhere,')
                        print('but is absorbed into the metal without a single mark.')
                    else:
                        print('You turn your attention away from the fountain, disgusted')
                        print('by the mucky and opaque water.')


            if textinput == 'Help':
                Help(room23_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type Help for a list of commands')
                

def room14(inventory, events_dict):
    elementalrage = 0
    
    print('This cylindrical chamber is almost completely bare, save for a skylight')
    print('above, where the faded northern light shines in. Next to it, old chains')
    print('hang,  all connecting to the exposed  metal wire running down along the')
    print('old staircase in the east wall')
    if events_dict['seal'] == False:
        print('Hovering in the middle of the room is a creature made of pure electricity, lightning arcing about the chamber')
        print('It floats above a clay sigil  on the floor,  and seems to be arcing  lightning into the chains around it, the')
        print('electicity running along the wire.')
    else:
        print('The room is quite, and in the middle lies the smashed remnants of a clay sigil')
    
    room14_items = {'Help': True, 'inventory': True, 'investigate': True, 'stairs':True, 'sapphire':False, 'sigil': True, 'elemental':True}

    while True:
        print('')
        textinput = input('>')
        if textinput in room14_items:
            if textinput == 'stairs':
                print('You make your way back down the old stone steps, winding back down to the chamber below.')
                room24(inventory, events_dict)
                break

            if textinput == 'investigate':
                print('You cant find anything, and that lightning elemental keeps starring at you')
                print('You notice the lightning elemental seems to be bound to the clay sigil...')

            if textinput == 'elemental' and events_dict['seal'] == False:
                elementalrage += 1
                if elementalrage < 3:
                    print('The elemental starts to flicker and hiss as you approach, its probably a good idea to stay back')
                elif elementalrage == 3:
                    print('The elemental is really starting to look angry! It shoots a bolt of lightning over your head as a warning!')
                elif elementalrage > 3:
                    print('The elemental shots a bolt of lightning at you!')
                    if inventory['ring'] == True:
                        print('The ring seems to absorb the majority of the lightning blast!')
                    else:
                        print('The lightning zaps you, killing you instantly!')
                        end(False)

            if textinput == 'sigil' and events_dict['seal'] == False:
                if inventory['ring'] == True:
                    print('The lightning elemental zaps lightning at you, but the ring you carry abosorbs it all')
                    print('You smash the sigil, and with a pop, the lightning elemental vanishes, absorbed into a brilliant gemstone')
                    events_dict['seal'] = True
                    room14_items['sapphire'] = True
                    
                else:
                    lightningchoice = input('The lightning elemental shots a warning blast at you! Do you press onward?[y/n]')
                    if lightningchoice == 'y':
                        print('The lightning elemental zaps you, vaporizing you and all your possessions!')
                        end(False)
                    else:
                        print('You back away from the lightning elemental')

            if textinput == 'sapphire' and room14_items['sapphire'] == True and inventory['sapphire'] == False:
                print('You pick up the brilliant sapphire')
                inventory['sapphire'] = True
            elif textinput == 'sapphire' and (room14_items['sapphire'] == False or inventory['sapphire'] == True):
                print('command not recognized! Type Help for a list of commands')
    
            
            if textinput == 'Help':
                Help(room14_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type Help for a list of commands')
                

def room24(inventory, events_dict):
    print('The room here is dark, the only light shinning in over the drawbridge to the')
    print('south,  casting a dim light over the masonry of the walls.  On the back wall')
    print('sits an old stone altar set against the wall,drapped over with a embroidered')
    print('blue cloth.  Other old cloth is piled on top,  perhaps old robes or flags to')
    print('some long gone lord. To the west,  set into the wall is an arch way,  with a')
    print('staircase leading up into a tower above. A wire leads from it, running along')
    print('the sealing to the metal door on the east wall.', end=' ')
    if events_dict['seal'] == False:
        print('Lightning arcs from it, humming with deadly static')
    elif events_dict['seal'] == True:
        print('The door is quiet')

    room24_items = {'Help': True, 'inventory': True, 'investigate': True, 'stairs':True, 'door':True, 'drawbridge': True, 'knife': False, 'cup':False, 'altar': True}

    while True:
        print('')
        textinput = input('>')
        if textinput in room24_items:
            if textinput == 'drawbridge':
                print('You walk back across the drawbridge, the wooden plank creaking')
                print('under each step, and the chains groaning.')
                room23(inventory, events_dict)
                break
            if textinput == 'stairs':
                print('You ascend up the old stone staircase up the tower. You hear a')
                print('crackling above')
                room14(inventory, events_dict)
                break
            if textinput == 'door':
                if events_dict['seal'] == True:
                    print('You pull the door open, it swings easily on its well oiled')
                    print('hinges, revealing a glowing light beyond.')
                    room34(inventory, events_dict)
                    break
                else:
                    doorchoice = input('The door is electrified, do you want to try to open it?[y/n]')
                    if doorchoice == 'y':
                        #the ring?
                        print('The door is stuck and electrifies you!')
                        end(False)
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

            if textinput == 'knife' and room24_items['knife'] == True and inventory['knife'] == False:
                print('You pick up the steel dagger')
                inventory['knife'] = True
            elif textinput == 'knife' and (room24_items['knife'] == False or inventory['knife'] == True):
                print('command not recognized! Type Help for a list of commands')

            if textinput == 'cup' and room24_items['cup'] == True and inventory['cup'] == False:
                print('You pick up the ornate bronze cup')
                inventory['cup'] = True
            elif textinput == 'cup' and (room24_items['cup'] == False or inventory['cup'] == True):
                print('command not recognized! Type Help for a list of commands')

                
            #the altar
            if textinput == 'altar':
                print('There is an ornate altar here')
                if inventory['sapphire'] == True:
                    sapphirechoice = input('do you want to place the sapphire on the altar?[y/n]')
                    if sapphirechoice == 'y':
                        print('you gently place the sapphire on the altar...')
                        inventory['sapphire'] = False
                        print('The sapphire is suddenly consumed in a flash of light, cracking into burnt glass')
                        print('Your mind is suddenly filled with a vision!  Before you there is an altar, above')
                        print('floats a glowing ornate amulet, shaped like an unblinking eye.  Your vision then')
                        print('focuses on a small hole in the wall, and you get a sense of death, of a chocking')
                        print('feeling filling your lungs.')
                        print('You suddenly wake, and find yourself lying on the altar...')
                    else:
                        print('You step away from the altar, turning your attention back on the room')

            if textinput == 'Help':
                Help(room24_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type Help for a list of commands')
                

def room34(inventory, events_dict):
    print('The walls of this room are covered in tapestries, faded with age, covering the cold stone walls.')
    print('In the center of the back wall is an altar,  covered with engraved stone runes.  Above it floats')
    print('a glowing amulet, made of ornate metal, shaped like an unblinking eye,  with a chained of silver')
    print('formed around it. Its soft silver radiance fills the room.')
    print('The door slowly creaks shut on the west wall.')
    
    room34_items = {'amulet':True, 'investigate':True, 'Help':True, 'inventory':True, 'hole':False, 'tapestries': True, 'door':True}
    poisontimer, poison = False, 0

    while True:
        print('')
        textinput = input('>')
        if poisontimer == True:
            poison += 1
            if poison > 1:
                print('You cough up blood as the poison burns your lungs and you suddenly fall to the ground dead')
                end(False)
        if textinput in room34_items:
            if textinput == 'door':
                print('You step out of the room back through the old metal door you came in through')
                room24(inventory, events_dict)
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

            if textinput == 'hole':
                print('you find a small hole, smelling of rotten eggs and smoke')
                if inventory['rag'] == True:
                    ragchoice = input('Would you like to stuff it with the rag?[y/n]')
                    if ragchoice == 'y':
                        print('You stuff the hole with the rag')
                        events_dict['rag'] = True
                    else:
                        print('Your attention shifts away from the small hole towards the glowing amulet')

            if textinput == 'amulet':
                if events_dict['rag'] == True:
                    print('You grab The Amulet of Paryuth off the altar...it glows in your hand and pulses with a faint warmth')
                    inventory['amulet'] = True
                else:
                    print('As you touch the amulet, there is a sudden hiss as from a small hole in the wall a cloud of poisonous gas fills your head...')
                    poisontimer = True
            
            if textinput == 'Help':
                Help(room34_items)
            if textinput == 'inventory':
                inventory_display(inventory)

        else:
            print('command not recognized! type Help for a list of commands')

def end(win):
    if win == True:
        print('you walk down the road, back to civilization, with the amulet of paryuth in your hands')
        print('You Win!')
    else:
        print('You lose!')

main()
