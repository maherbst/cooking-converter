lemonJuiceCups = float(input('Enter amount of lemon juice (in cups):\n'))

# FIXME (1): Finish reading other items into variables, then output the three ingrdients
waterCups = float(input('Enter amount of water (in cups):\n'))
nectarCups = float(input('Enter amount of agave nectar (in cups):\n'))
servingsDoes = float(input('How many servings does this make?\n'))
print('\nLemonade ingredients - yields' , servingsDoes , 'servings')
print(lemonJuiceCups , 'cup(s) lemon juice')
print(waterCups, 'cup(s) water')
print(nectarCups, 'cup(s) agave nectar')
# FIXME (2): Prompt user for desired number of servings. Convert and output the ingredients
servingsWould = float(input('\nHow many servings would you like to make?\n'))
print('\nLemonade ingredients - yields' , servingsWould , 'servings')
print((servingsWould / servingsDoes) * lemonJuiceCups , 'cup(s) lemon juice')
print((servingsWould / servingsDoes) * waterCups , 'cup(s) water')
print((servingsWould / servingsDoes) * nectarCups , 'cup(s) agave nectar')
# FIXME (3): Convert and output the ingredients from (2) to gallons
servingsWouldLemon = ((servingsWould / servingsDoes) * lemonJuiceCups) / 16 
servingsWouldWater = ((servingsWould / servingsDoes) * waterCups) / 16
servingsWouldNectar = ((servingsWould / servingsDoes) * nectarCups) / 16
print('\nLemonade ingredients - yields' , servingsWould , 'servings')
print(servingsWouldLemon , 'gallon(s) lemon juice')
print(servingsWouldWater , 'gallon(s) water')
print(servingsWouldNectar , 'gallon(s) agave nectar')
