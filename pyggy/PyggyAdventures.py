import pygame
import random


pygame.init()

    # This is to create the screen on which the game will run (we need the width and the height of it)
screen_width = 1040
screen_height = 680
screen = pygame.display.set_mode((screen_width,screen_height))

    # This will allow us to load a visual represntation of us and the enemy in the game as well as the prize
enemy = pygame.image.load("skeleton_enemy.jpg")
enemy2 = pygame.image.load("skeleton_enemy.jpg")
enemy3 = pygame.image.load("skeleton_enemy.jpg")
hero = pygame.image.load("piggy.jpg")
holygrail = pygame.image.load("holy_grail.jpg")

    # This will change the size of the images to 100 by 100
hero = pygame.transform.scale(hero,(100, 100))
enemy = pygame.transform.scale(enemy,(100, 100))
enemy2 = pygame.transform.scale(enemy2,(100, 100))
enemy3 = pygame.transform.scale(enemy3,(100, 100))
holygrail = pygame.transform.scale(holygrail,(100,100))

# This will fetch the height and width of the player, the enemies and the prize
hero_height = hero.get_height()
hero_width = hero.get_width()

enemy_height = enemy.get_height()
enemy_width = enemy.get_width()

enemy2_height = enemy2.get_height()
enemy2_width = enemy2.get_width()

enemy3_height = enemy3.get_height()
enemy3_width = enemy3.get_width()

holygrail_height = holygrail.get_height()
holygrail_width = holygrail.get_width()




# These will be the cordinates of the player, the prize and the enemies

heroXPosition = screen_width - 1000
heroYPosition = random.randint(0, screen_height - hero_height)

enemyXPosition = screen_width - enemy_width
enemyYPosition = random.randint(0, screen_height - enemy_height)

enemy2XPosition = screen_width - 500
enemy2YPosition = random.randint(0, screen_height - enemy2_height)

enemy3XPosition = screen_width - 250
enemy3YPosition = random.randint(0, screen_height - enemy3_height)

holygrailXPosition = screen_width - holygrail_width
holygrailYPosition = random.randint(0, screen_height - holygrail_height)


while 1:
    screen.fill(0) # This will clear the screen
        # This wil spawn the hero, enemies and prize
    screen.blit(hero, (heroXPosition, heroYPosition))
    screen.blit(enemy, (enemyXPosition, enemyYPosition))
    screen.blit(enemy2, (enemy2XPosition, enemy2YPosition))
    screen.blit(enemy3, (enemy3XPosition, enemy3YPosition))
    screen.blit(holygrail, (holygrailXPosition, holygrailYPosition))
        # This updates every iteration graphically
    pygame.display.update()

        # This loops through occurrances in the game
    for event in pygame.event.get():

            # check if the user quits
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        # The following code checks if the user presses left, right, up or down and tests if the player quits
        # If the user prefers he or she can also use 'w','a','s' or 'd' to navigate the screen

        if event.type == (pygame.KEYDOWN):
                if event.key == ord('q'):
                    pygame.quit()
                    
                if event.key == pygame.K_LEFT or event.key == ord('a'):
                    heroXPosition -= 50
                if event.key == pygame.K_RIGHT or event.key == ord('d'):
                    heroXPosition += 50
                if event.key == pygame.K_UP or event.key == ord('w'):
                    heroYPosition -= 50
                if event.key == pygame.K_DOWN or event.key == ord('s'):
                    heroYPosition += 50

        # Boudning Box is an area defined by two longitudes and two latitudes
        #These are the boudning boxes for the hero, the enemies and the prize        
        # Hero bounding box
    heroBox = pygame.Rect(hero.get_rect())
    heroBox.top = heroYPosition
    heroBox.left = heroXPosition

    # Enemies' bounding box
    enemyBox = pygame.Rect(enemy.get_rect())
    enemyBox.top = enemyYPosition
    enemyBox.left = enemyXPosition

    enemy2Box = pygame.Rect(enemy.get_rect())
    enemy2Box.top = enemy2YPosition
    enemy2Box.left = enemy2XPosition

    enemy3Box = pygame.Rect(enemy.get_rect())
    enemy3Box.top = enemy3YPosition
    enemy3Box.left = enemy3XPosition

    # Holy Grail bounding box
    holygrailBox = pygame.Rect(holygrail.get_rect())
    holygrailBox.top = holygrailYPosition
    holygrailBox.left = holygrailXPosition

        # This will test if the any of the enemy bounding boxes collide with heroBox (Hero's Bounding Box)

    if heroBox.colliderect(enemyBox) or heroBox.colliderect(enemy2Box) or heroBox.colliderect(enemy3Box):

        print("Tis but a flesh wound!")

        pygame.quit()
        exit(0)
        # This will test if the hero collides with the prize and if so the program will declare you've won in Monty Python!
    if heroBox.colliderect(holygrailBox):
        print("You fight with the strength of many pig Sir Knight!")

        pygame.quit()
        exit(0)


    enemyXPosition -= 0.15
    enemy2XPosition -= 0.20
    enemy3XPosition -= 0.30