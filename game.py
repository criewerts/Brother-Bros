"""cwp4kh | car2xz"""

import pygame
import gamebox
import random

camera = gamebox.Camera(800, 600)

game = False
end = False
win = False
has_pumpkin = False
facing_L = False
swap = False

score = 0
fps = 30
timer = 60
counter = 0
shot_timer = 0

score_box = gamebox.from_text(400, 50, str(score), 50, 'purple', False, True)

timer_box = gamebox.from_text(400, 50, str(timer), 50, 'purple', False, True)

pygame.display.set_caption('brother bros.')

skybox = gamebox.from_image(camera.x, camera.y, 'sprites\skybox.png')

ground = gamebox.from_image(5000, 500, 'sprites\ground.png')

ghosts = [
    gamebox.from_image(2710, 170, 'sprites\ghost.png'),
]

pilots = [
    gamebox.from_image(1863, 250, 'sprites\pilot.png'),
    gamebox.from_image(4749, 250, 'sprites\pilot.png'),
    gamebox.from_image(6300, 250, 'sprites\pilot.png'),
]

for pilot in pilots:
    pilot.speedy = -4

tanks = [
    gamebox.from_image(997, 455, r'sprites\tank.png'),
    gamebox.from_image(2415, 455, r'sprites\tank.png'),
    gamebox.from_image(3124, 455, r'sprites\tank.png'),
    gamebox.from_image(5222, 455, r'sprites\tank.png'),
    gamebox.from_image(5342, 455, r'sprites\tank.png'),
    gamebox.from_image(5472, 455, r'sprites\tank.png'),
    gamebox.from_image(5600, 455, r'sprites\tank.png'),
]

for tank in tanks:
    tank.speedx = -3

floor = [
    #  opening blocks,
    gamebox.from_image(500, 350, r'sprites\block2.png'),
    gamebox.from_image(560, 350, r'sprites\block.png'),
    gamebox.from_image(620, 350, r'sprites\block2.png'),

    #  first pipes
    gamebox.from_image(800, 420, 'sprites\pipe.png'),
    gamebox.from_image(1000, 350, r'sprites\block2.png'),
    gamebox.from_image(1200, 420, 'sprites\pipe.png'),

    # platform jump
    gamebox.from_image(1500, 350, r'sprites\longblock.png'),
    gamebox.from_image(1700, 250, r'sprites\longblock.png'),
    gamebox.from_image(2100, 250, r'sprites\platform.png'),
    gamebox.from_image(2200, 250, r'sprites\platform.png'),

    # item block cross
    gamebox.from_image(2600, 350, r'sprites\block.png'),

    # stairs
    gamebox.from_image(2900, 455, 'sprites\stairblock1.png'),
    gamebox.from_image(2940, 440, 'sprites\stairblock2.png'),
    gamebox.from_image(2980, 425, 'sprites\stairblock3.png'),
    gamebox.from_image(3020, 410, 'sprites\stairblock4.png'),

    gamebox.from_image(3270, 410, 'sprites\stairblock4.png'),
    gamebox.from_image(3310, 425, 'sprites\stairblock3.png'),
    gamebox.from_image(3350, 440, 'sprites\stairblock2.png'),
    gamebox.from_image(3390, 455, 'sprites\stairblock1.png'),

    #  pipes 2
    gamebox.from_image(3700, 420, 'sprites\pipe.png'),
    gamebox.from_image(3835, 350, r'sprites\block.png'),
    gamebox.from_image(4000, 420, 'sprites\pipe.png'),
    gamebox.from_image(4300, 400, 'sprites\longpipe.png'),

    #  platforms 2
    gamebox.from_image(4600, 250, 'sprites\longblock.png'),
    gamebox.from_image(4900, 250, 'sprites\longblock.png'),
    gamebox.from_image(4900, 350, 'sprites\platform.png'),

    #  open space

    #  big staircase
    gamebox.from_image(5900, 455, 'sprites\stairblock1.png'),
    gamebox.from_image(5940, 440, 'sprites\stairblock2.png'),
    gamebox.from_image(5980, 425, 'sprites\stairblock3.png'),
    gamebox.from_image(6020, 410, 'sprites\stairblock4.png'),
    gamebox.from_image(6060, 395, 'sprites\stairblock5.png'),
    gamebox.from_image(6100, 380, 'sprites\stairblock6.png'),
    gamebox.from_image(6140, 365, 'sprites\stairblock7.png'),
    gamebox.from_image(6180, 350, 'sprites\stairblock8.png'),
]

goal = gamebox.from_image(6500, 300, 'sprites\goal.png')

itemblocks = [
    gamebox.from_image(530, 350, 'sprites\itemblock.png'),
    gamebox.from_image(590, 350, 'sprites\itemblock.png'),
    gamebox.from_image(2150, 350, 'sprites\itemblock.png'),

    gamebox.from_image(2500, 350, 'sprites\itemblock.png'),
    gamebox.from_image(2600, 250, 'sprites\itemblock.png'),
    gamebox.from_image(2700, 350, 'sprites\itemblock.png'),

    gamebox.from_image(3865, 350, 'sprites\itemblock.png'),
    gamebox.from_image(4400, 350, 'sprites\itemblock.png'),
]

bounds = [
    gamebox.from_image(-20, 300, r'sprites\barrier.png'),
    gamebox.from_image(6820, 300, r'sprites\barrier.png')

]

coins = [
    gamebox.from_image(1000, 250, 'sprites\coin.png'),
    gamebox.from_image(1675, 160, 'sprites\coin.png'),
    gamebox.from_image(2600, 185, 'sprites\coin.png'),
    gamebox.from_image(3100, 430, 'sprites\coin.png'),
    gamebox.from_image(3150, 430, 'sprites\coin.png'),
    gamebox.from_image(3200, 430, 'sprites\coin.png'),
    gamebox.from_image(3700, 345, 'sprites\coin.png'),
    gamebox.from_image(4000, 345, 'sprites\coin.png'),
    gamebox.from_image(4300, 275, 'sprites\coin.png'),
    gamebox.from_image(4550, 210, 'sprites\coin.png'),
    gamebox.from_image(4600, 210, 'sprites\coin.png'),
    gamebox.from_image(4650, 210, 'sprites\coin.png'),
    gamebox.from_image(4899, 310, 'sprites\coin.png'),
    gamebox.from_image(5250, 310, 'sprites\coin.png'),
    gamebox.from_image(5350, 310, 'sprites\coin.png'),
    gamebox.from_image(5450, 310, 'sprites\coin.png'),
    gamebox.from_image(5550, 310, 'sprites\coin.png'),
    gamebox.from_image(5650, 310, 'sprites\coin.png'),
    gamebox.from_image(5750, 310, 'sprites\coin.png'),
    gamebox.from_image(6350, 140, 'sprites\coin.png'),
    gamebox.from_image(6400, 130, 'sprites\coin.png'),
    gamebox.from_image(6450, 140, 'sprites\coin.png'),
]

watches = [

]

pumpkins = [

]

shots = [

]

lol = gamebox.from_text(7000, 400, 'your castle is in another game', 30, 'blue')
sam = gamebox.from_image(130, 445, r'sprites\not_mario.png')


def start(keys):
    """
    Displays the title screen, and activates the game when the user inputs [space].
    :param keys: will only start the game if it contains [space]
    """
    camera.clear('#323335')
    camera.draw(skybox)
    camera.draw(gamebox.from_text(400, 280, 'Brother Bros.', 100, 'cyan'))
    camera.draw(gamebox.from_text(400, 20, 'cwp4kh | car2xz', 25, 'cyan'))
    camera.draw(gamebox.from_text(400, 400, 'use arrow keys to move and [space] to fire. Jump into item blocks to get an item', 30, 'orange'))
    camera.draw(gamebox.from_text(400, 430, 'jump on enemies to defeat them, and make it to the end of the level', 20, 'orange'))
    camera.draw(gamebox.from_text(400, 500, 'press [space] to begin...', 30, 'purple', False, True))

    if pygame.K_SPACE in keys:
        keys.clear()
        global game
        game = True


def drawgame(keys):
    """
    The main man. Defines and draws the game, beginning with variables, then the various enemies
    and blocks' behavior, and the player's behavior. Finally, it draws everything within frame.
    :param keys: user inputs, used in moving the player character
    """

    #  vars

    global score
    global score_box
    global fps
    global end
    global floor
    global counter
    global timer
    global win
    global has_pumpkin
    global facing_L
    global shot_timer
    global sam
    global swap
    global skybox

    draw_lst = []

    #  timers and wins

    skybox.x = camera.x
    skybox.y = camera.y
    camera.draw(skybox)

    timer_box.x = camera.x

    counter += 1
    if shot_timer < 30:
        shot_timer += 1
    if counter % 30 == 0:
        timer -= 1
    if timer <= 0:
        end = True

    camera.draw(goal)
    if sam.touches(goal):
        end = True
        win = True

    # ghosts

    for ghost in ghosts:
        if abs(ghost.x - sam.x) <= 700:
            if sam.x > ghost.x:
                ghost.x += 2
                ghost.image = "sprites\ghost_R.png"
            elif sam.x < ghost.x:
                ghost.x -= 2
                ghost.image = "sprites\ghost.png"
            if sam.y > ghost.y:
                ghost.y += 2
            elif sam.y < ghost.y:
                ghost.y -= 2

        if sam.touches(ghost):
            end = True

    # tanks

    for tank in tanks:
        if abs(tank.x - sam.x) <= 700:
            for item in floor:
                if tank.left_touches(item) or tank.right_touches(item):
                    tank.xspeed = -tank.xspeed
                    if tank.xspeed > 0:
                        tank.image = r"sprites\tank_R.png"
                    else:
                        tank.image = r"sprites\tank.png"

            for item in itemblocks:
                if tank.left_touches(item) or tank.right_touches(item):
                    tank.xspeed = -tank.xspeed
                    if tank.xspeed > 0:
                        tank.image = r"sprites\tank_R.png"
                    else:
                        tank.image = r"sprites\tank.png"
            tank.move_speed()

    for tank in tanks:
        if sam.bottom_touches(tank):
            tanks.remove(tank)
            score += 500
            sam.speedy = -20
        elif sam.touches(tank):
            end = True

    # pilots

    for pilot in pilots:
        if abs(pilot.x - sam.x) <= 700:
            if pilot.y < 150 or pilot.y > 350:
                pilot.speedy = -pilot.speedy
            pilot.move_speed()

    for pilot in pilots:
        if sam.bottom_touches(pilot):
            pilots.remove(pilot)
            score += 1000
            sam.speedy = -20
        elif sam.touches(pilot):
            end = True

    #  shots

    for shot in shots:
        shot.move_speed()
        for tank in tanks:
            if shot.touches(tank):
                tanks.remove(tank)
                score += 500
                shots.remove(shot)
        for ghost in ghosts:
            if shot.touches(ghost):
                ghosts.remove(ghost)
                score += 2000
                shots.remove(shot)
        for pilot in pilots:
            if shot.touches(pilot):
                pilots.remove(pilot)
                score += 1000
                shots.remove(shot)
        if shot.x > camera.x + 500:
            shots.remove(shot)
        if shot.x < camera.x - 500:
            shots.remove(shot)

    # coins

    for coin in coins:
        if sam.touches(coin):
            coins.remove(coin)
            score += 100

    # watches

    for watch in watches:
        if sam.touches(watch):
            watches.remove(watch)
            timer += 5

    # pumpkins

    for item in pumpkins:
        if sam.touches(item):
            pumpkins.remove(item)
            has_pumpkin = True
            score += 250

    if has_pumpkin and swap == False:
        sam = gamebox.from_image(sam.x, sam.y, r'sprites\not_mario_power.png')
        swap = True

    if has_pumpkin and pygame.K_SPACE in keys and shot_timer == 30:
        if facing_L:
            shot = gamebox.from_image(sam.x, sam.y, 'sprites\shot_L.png')
            shot.speedx = -20
            shots.append(shot)
        else:
            shot = gamebox.from_image(sam.x, sam.y, 'sprites\shot.png')
            shot.speedx = 20
            shots.append(shot)
        shot_timer = 0

    #  sam

    #  bounds
    if sam.bottom >= 600:
        end = True
    if 400 < sam.x < 9600:
        camera.x = sam.x

    #  controls
    for item in floor:
        if sam.bottom_touches(item) or sam.bottom_touches(ground):
            if pygame.K_UP in keys:
                sam.yspeed = -20
                keys.remove(pygame.K_UP)
    for item in itemblocks:
        if sam.bottom_touches(item) or sam.bottom_touches(ground):
            if pygame.K_UP in keys:
                sam.yspeed = -20
                keys.remove(pygame.K_UP)

    # air-cancel:
    if pygame.K_DOWN in keys:
        sam.yspeed = 0
        keys.remove(pygame.K_DOWN)

    if pygame.K_RIGHT in keys:
        sam.xspeed += 2
        facing_L = False
    if pygame.K_LEFT in keys:
        sam.xspeed -= 2
        facing_L = True
    if pygame.K_RIGHT not in keys and pygame.K_LEFT not in keys:
        sam.xspeed = 0

    if facing_L:
        if has_pumpkin:
            sam.image = r'sprites\not_mario_power_L.png'
        else:
            sam.image = r'sprites\not_mario_L.png'
    else:
        if has_pumpkin:
            sam.image = r'sprites\not_mario_power.png'
        else:
            sam.image = r'sprites\not_mario.png'

    if sam.speedy > 50:
        sam.speedy = 5
    else:
        sam.yspeed += 1.3
    sam.y = sam.yspeed + sam.y

    if sam.speedx > 5:
        sam.speedx = 5
    sam.x = sam.xspeed + sam.x

    if sam.speedx < -5:
        sam.speedx = -5
    sam.x = sam.xspeed + sam.x

    draw_lst.append(sam)

    for box in itemblocks:
        if sam.top_touches(box):
            temp = random.randint(1, 10)
            if 1 <= temp <= 5:
                coins.append(gamebox.from_image(box.x, box.y - 45, 'sprites\coin.png'))
            elif 6 <= temp <= 8:
                watches.append(gamebox.from_image(box.x, box.y - 45, 'sprites\watch.png'))
            else:
                pumpkins.append(gamebox.from_image(box.x, box.y - 45, 'sprites\pumpkin.png'))
            floor.append(gamebox.from_image(box.x, box.y, 'sprites\itemblock5.png'))
            itemblocks.remove(box)

    #  draw obstacles, etc

    for item in floor:
        if sam.touches(item):
            sam.move_to_stop_overlapping(item)
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in itemblocks:
        if sam.touches(item):
            sam.move_to_stop_overlapping(item)
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in bounds:
        if sam.touches(item):
            sam.move_to_stop_overlapping(item)
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in ghosts:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in tanks:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in pilots:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in coins:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in watches:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in pumpkins:
        if item.left > camera.left or item.right < camera.right:
            camera.draw(item)

    for item in shots:
        camera.draw(item)

    if sam.touches(ground):
        sam.move_to_stop_overlapping(ground)
    camera.draw(ground)
    draw_lst.append(lol)

    draw_lst.append(gamebox.from_text(camera.x + 300, 50, str(timer), 50, 'purple', False, True))
    draw_lst.append(gamebox.from_text(camera.x - 300, 50, str(score), 50, 'purple', False, True))

    # draw

    if not end:
        for item in draw_lst:
            camera.draw(item)
    else:
        for item in draw_lst:
            camera.draw(item)

    if pygame.K_t in keys:
        print((sam.x, sam.y))


def tick(keys):
    """
    Decides to run the game or not, as well as showing the win / lose screens.
    :param keys: user inputs. funneled into drawgame().
    """
    global game
    global end
    global score
    global win
    global timer
    camera.clear('#323335')
    if not game:
        start(keys)
    elif not end:
        drawgame(keys)
    else:
        camera.clear('black')
        if win:
            camera.draw(gamebox.from_text(camera.x, camera.y, 'You Win!', 100, 'green', False))
            score += timer * 10
            camera.draw(gamebox.from_text(camera.x, camera.y + 100, 'Score: '+str(score), 50, 'yellow', False, True))
        else:
            camera.draw(gamebox.from_text(camera.x, camera.y, 'You lose...', 100, 'red', False))
        gamebox.pause()
    camera.display()


gamebox.timer_loop(fps, tick)
