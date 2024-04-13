# Simple pygame program

# Import and initialize the pygame library
import pygame
import os

WIDTH, HEIGHT = 900, 500
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("First Game!")

WHITE = (255, 255, 255)

IMAGE = pygame.image.load(
    os.path.join('Assets', 'gameJam2024_figure.webp'))

image_x = 0
image_y = 0

def draw_window():
    SCREEN.fill(WHITE)
    SCREEN.blit(IMAGE, (image_x, image_y))
    pygame.display.update()

def main():
    global image_x, image_y 
    run = True
    draw_window()
    while run:
        pygame.time.delay(100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        keys = pygame.key.get_pressed()  # This will give us a dictonary where each key has a value of 1 or 0. Where 1 is pressed and 0 is not pressed.

        if keys[pygame.K_LEFT]: # We can check if a key is pressed like this
            image_x -= 5
        if keys[pygame.K_RIGHT]:
            image_x += 5
        if keys[pygame.K_UP]:
            image_y -= 5
        if keys[pygame.K_DOWN]:
            image_y += 5

        draw_window()

    pygame.quit()

if __name__ == "__main__":
    main()