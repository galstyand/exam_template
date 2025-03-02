from .grid import Grid
from .player import Player
from . import pickups
from .print_status import print_status

player = Player(17, 5)
score = 0
inventory = []

g = Grid()
g.set_player(player)
g.make_walls()
g.make_walls_inside_grid()
pickups.randomize(g)

command = "a"
# Loopa tills användaren trycker Q eller X.
while not command.casefold() in ["q", "x"]:
    print_status(g, score)

    command = input("Use WASD to move, Q/X to quit. ")
    command = command.casefold()[:1]

    #variabel för förflytning över X
    moveX = 0
    #variabel för förflytning över Y
    moveY = 0

    if command == "d":
        moveX = 1
    elif command == "a":
        moveX = -1
    elif command == "w":
        moveY = -1
    elif command == "s":
        moveY = 1

    #Om både moveX och moveY är 0 betyder det att input är något annat än WASD
    if (moveX != 0 or moveY != 0) and player.can_move(moveX, moveY, g):  # move right
        maybe_item = g.get(player.pos_x + moveX, player.pos_y + moveY)
        player.move(moveX, moveY)

        #The floor is lava - för varje steg man går ska man tappa 1 poäng.
        score -= 1

        if isinstance(maybe_item, pickups.Item):
            # we found something
            inventory.append(maybe_item)
            score += maybe_item.value
            print(f"You found a {maybe_item.name}, +{maybe_item.value} points.")
            #g.set(player.pos_x, player.pos_y, g.empty)
            g.clear(player.pos_x, player.pos_y)

    #Kommando: "i", skriver ut innehållet i spelarens inventory.
    if command == "i":
        for item in inventory:
            print(item.name)

# Hit kommer vi när while-loopen slutar
print("Thank you for playing!")