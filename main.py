
# Example file showing a circle moving on screen
import pygame as p

# p setup
p.init()
screen = p.display.set_mode((1000, 1000))
clock = p.time.Clock()
running = True
dt = 0

player_pos = p.Vector2(screen.get_width() / 2, screen.get_height() / 2)

while running:
    # poll for events
    # p.QUIT event means the user clicked X to close your window
    for event in p.event.get():
        if event.type == p.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    screen.fill("purple")

    p.draw.circle(screen, "red", player_pos, 40)

    keys = p.key.get_pressed()
    if keys[p.K_w]:
        player_pos.y -= 300 * dt
    if keys[p.K_s]:
        player_pos.y += 300 * dt
    if keys[p.K_a]:
        player_pos.x -= 300 * dt
    if keys[p.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    p.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

p.quit()

