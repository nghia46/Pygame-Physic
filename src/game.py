import pygame
import pymunk
import pymunk.pygame_util

# Initialize Pygame
pygame.init()

# Set up the display
screen = pygame.display.set_mode((800, 600))
clock = pygame.time.Clock()
running = True

# Initialize Pymunk space
space = pymunk.Space()
space.gravity = (0, 900)  # Gravity (x, y)

# Draw options for Pymunk
draw_options = pymunk.pygame_util.DrawOptions(screen)

# Function to add a static line (ground)
def add_static_line(space):
    body = pymunk.Body(body_type=pymunk.Body.STATIC)
    shape = pymunk.Segment(body, (50, 500), (750, 500), 5)
    shape.elasticity = 0.8
    space.add(body, shape)

# Function to add a ball
def add_ball(space, position):
    mass = 1
    radius = 25
    inertia = pymunk.moment_for_circle(mass, 0, radius)
    body = pymunk.Body(mass, inertia)
    body.position = position
    shape = pymunk.Circle(body, radius)
    shape.elasticity = 0.8
    space.add(body, shape)

# Add the ground
add_static_line(space)

# Main loop
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            add_ball(space, mouse_pos)

    # Clear screen
    screen.fill((255, 255, 255))

    # Update the physics
    space.step(1/60.0)

    # Draw the space
    space.debug_draw(draw_options)

    # Flip the screen
    pygame.display.flip()

    # Tick the clock
    clock.tick(60)

pygame.quit()
