import sys
sys.path.insert(0, '/opt/minecraft-pi/api/python/mcpi')

from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

wallHeight = input('How many blocks high would you like the walls? ')

mc = Minecraft.create()

x, y, z = mc.player.getPos()
x, y, z = int(x), int(y), int(z)
oX = range(x-1, x+1) # store original position
oZ = range(z-1, z+1)

wallBase = y # current vertical position.
wallTop = y + wallHeight # user defined wall height

mc.postToChat('Start walking the path of your house')

moves = 0

while True:
    a, b, c = mc.player.getPos()
    a, b, c = int(a), int(b), int(c)
    print(str(a) + ' = ' + str(x))
    print(str(c) + ' = ' + str(z))
    if a != x or c != z:
        moves = moves + 1
        mc.setBlocks(x, y, z, x, wallTop, z, 1)
        x, y, z = a, b, c
        
        if moves > 3:
            if x in oX and z in oZ:
                mc.postToChat('Wall complete')
                break
    sleep(0.1)


