# Import pygame
import pygame
# Initialize pygame
pygame.init() 
# Create a game screen with width=600 and height=600 and name it as "screen"
screen = pygame.display.set_mode((600,600))
# Set the game title as "Car Racing Game"
pygame.display.set_caption("Car Racing Game")
# Game loop
carryOn = True
while carryOn:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            carryOn = False
    
    # Store the background image name with extension in a variable "bgImg_name"
    bgImg_name = "road.png"
    # Load the background image and store it in a variable "bgImg"
    bgImg = pygame.image.load(bgImg_name).convert_alpha()
    # Scale the background image to fit the screen with (width, height) = (650, 600)
    # and store scaled image in a variable "bgImg_scaled"
    bgImg_scaled = pygame.transform.smoothscale(bgImg,(650,600))
    # Display scaled background image on screen at location (0, 0)
    screen.blit(bgImg_scaled,(0,0))
    
    # Store the yellow car image name with extension in a variable "yellow_car_name"
    yellow_car_name = "            "
    # Load the yellow car image and store it in a variable "yellow_car"
    yellow_car = pygame.image.load(            ).convert_alpha()
    # Scale the yellow car image to fit the screen with (width, height) = (230, 150)
    # and store scaled image in a variable "yellow_car_scaled"
    yellow_car_scaled = pygame.transform.smoothscale(yellow_car,           )
    # Display scaled yellow car image on screen at location (40,400)
    screen.blit(yellow_car_scaled,            )
    
    # Update the contents of the display
    pygame.display.flip()

# Quit the game 
pygame.quit()
