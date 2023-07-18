import pygame
from time import sleep

pygame.init()
print(pygame.joystick.get_count())
j = pygame.joystick.Joystick(0)
sleep(2)
j.init()
sleep(2)

try:
    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                print("Button Pressed")
                if j.get_button(1):
                    print('X press')
                elif j.get_button(7):
                    print('R2 press')
            elif event.type == pygame.JOYBUTTONUP:
                print("Button Released")

except KeyboardInterrupt:
    print("EXITING NOW")
    j.quit()