import pygame
import random
import sys
from game_over import game_over_screen  

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()

rocket_img = pygame.image.load("rocket.png")
meteor_img = pygame.image.load("meteor.png")
bullet_img = pygame.image.load("bullet.png")

rocket_img = pygame.transform.scale(rocket_img, (120, 120))
bullet_img = pygame.transform.scale(bullet_img, (20, 40))

shoot_sound = pygame.mixer.Sound("shoot_sound.wav")
explosion_sound = pygame.mixer.Sound("explosion_sound.wav")

stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(100)]

class Rocket:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT - 200
        self.speed = 19
        self.bullets = []
        self.health = 100  

    def draw(self, screen):
        screen.blit(rocket_img, (self.x, self.y))

        health_bar_width = 120
        health_bar_height = 10
        pygame.draw.rect(screen, RED, (self.x, self.y - 20, health_bar_width, health_bar_height))
        pygame.draw.rect(screen, GREEN, (self.x, self.y - 20, int(health_bar_width * (self.health / 100)), health_bar_height))

    def move(self, keys):
        if keys[pygame.K_LEFT] and self.x > 0:
            self.x -= self.speed
        if keys[pygame.K_RIGHT] and self.x < WIDTH - 120:
            self.x += self.speed

    def shoot(self):
        bullet = Bullet(self.x + 50, self.y)
        self.bullets.append(bullet)
        shoot_sound.play()

class Bullet:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.speed = 24

    def draw(self, screen):
        screen.blit(bullet_img, (self.x, self.y))

    def move(self):
        self.y -= self.speed

class Meteor:
    def __init__(self, x=None, y=None, size=None, speed=None):
        self.x = x if x is not None else random.randint(0, WIDTH - 120)
        self.y = y if y is not None else random.randint(-200, -50)
        self.speed = speed if speed is not None else random.randint(3, 7)
        self.size = size if size is not None else random.randint(60, 125)
        self.health = self.size 
        self.angle = random.randint(0, 360) 
        self.rotation_speed = random.randint(1, 5)  

    def draw(self, screen):
        rotated_image = pygame.transform.rotate(pygame.transform.scale(meteor_img, (self.size, self.size)), self.angle)
        rect = rotated_image.get_rect(center=(self.x + self.size // 2, self.y + self.size // 2))
        screen.blit(rotated_image, rect.topleft)

    def move(self):
        self.y += self.speed
        self.angle = (self.angle + self.rotation_speed) % 360  

def intro_screen(rocket):
    font = pygame.font.SysFont("Arial", 100, bold=True)
    intro_text = font.render("Pronti a Sparare!", True, WHITE)
    
    intro_duration = 3000 
    start_time = pygame.time.get_ticks()

    while pygame.time.get_ticks() - start_time < intro_duration:
        screen.fill(BLACK)
        
        for i, star in enumerate(stars):
            pygame.draw.circle(screen, WHITE, star, 2)
            stars[i] = (star[0], (star[1] + 1) % HEIGHT) 

        rocket.draw(screen)

        screen.blit(intro_text, ((WIDTH - intro_text.get_width()) // 2, (HEIGHT - intro_text.get_height()) // 2))
        
        pygame.display.flip()
        pygame.time.delay(30) 

menu_music = pygame.mixer.Sound("title_music.mp3")

def main_game():
    menu_music.play(-1)
    rocket = Rocket()
    intro_screen(rocket)

    menu_music.stop()
    game_music = pygame.mixer.Sound("game_music2.mp3")
    game_music.play(-1)

    clock = pygame.time.Clock()

    meteors = [Meteor() for _ in range(6)]
    flashes = []  
    running = True
    paused = False
    FPS = 60
    score = 0

    clone_interval = 1200  
    last_clone_time = pygame.time.get_ticks()

    font = pygame.font.SysFont("Arial", 50)
    
    pause_button_rect = pygame.Rect(WIDTH - 150, 20, 120, 50)

    def show_pause_screen():
        pause_overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
        pause_overlay.fill((0, 0, 0, 200))  
        screen.blit(pause_overlay, (0, 0))

        resume_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 70)
        menu_button_rect = pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 70)

        pygame.draw.rect(screen, (255, 255, 255), resume_button_rect, border_radius=15)
        pygame.draw.rect(screen, (255, 255, 255), menu_button_rect, border_radius=15)

        resume_text = font.render("Riprendi", True, BLACK)
        menu_text = font.render("ESCI", True, BLACK)

        screen.blit(resume_text, (resume_button_rect.centerx - resume_text.get_width() // 2,
                                  resume_button_rect.centery - resume_text.get_height() // 2))
        screen.blit(menu_text, (menu_button_rect.centerx - menu_text.get_width() // 2,
                                menu_button_rect.centery - menu_text.get_height() // 2))

        return resume_button_rect, menu_button_rect

    while running:
        screen.fill(BLACK)
        for i, star in enumerate(stars):
            pygame.draw.circle(screen, WHITE, star, 2)
            stars[i] = (star[0], (star[1] + 1) % HEIGHT)  

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pause_button_rect.collidepoint(event.pos):
                    paused = True

            if paused:
                if event.type == pygame.MOUSEBUTTONDOWN:
                    resume_rect, menu_rect = show_pause_screen()
                    if resume_rect.collidepoint(event.pos):
                        paused = False
                    elif menu_rect.collidepoint(event.pos):

                        running = False
                        game_music.stop()  
                        menu_music.play(-1)  
                  

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    rocket.shoot()


        pygame.draw.rect(screen, WHITE, pause_button_rect, border_radius=15)
        pause_text = font.render("Pausa", True, BLACK)
        screen.blit(pause_text, (pause_button_rect.centerx - pause_text.get_width() // 2,
                                 pause_button_rect.centery - pause_text.get_height() // 2))

        if paused:
            resume_button_rect, menu_button_rect = show_pause_screen()
        else:

            keys = pygame.key.get_pressed()
            rocket.move(keys)

            for bullet in rocket.bullets[:]:
                bullet.draw(screen)
                bullet.move()
                if bullet.y < 0:
                    rocket.bullets.remove(bullet)

            for meteor in meteors[:]:
                meteor.move()
                if meteor.y > HEIGHT:
                    meteors.remove(meteor)
                    meteors.append(Meteor())

                for bullet in rocket.bullets[:]:
                    if (meteor.x < bullet.x < meteor.x + meteor.size and
                            meteor.y < bullet.y < meteor.y + meteor.size):
                        rocket.bullets.remove(bullet)
                        meteor.health -= 20
                        flashes.append((meteor.x, meteor.y, meteor.size))
                        if meteor.health <= 60:
                            meteors.remove(meteor)
                            explosion_sound.play()
                            score += 10

                if (meteor.x < rocket.x + 60 < meteor.x + meteor.size and
                        meteor.y < rocket.y + 60 < meteor.y + meteor.size):
                    damage = random.randint(10, 30)
                    rocket.health -= damage
                    explosion_sound.play()
                    meteors.remove(meteor)
                    meteors.append(Meteor())
                    if rocket.health <= 0:
                        game_music.stop()
                        result = game_over_screen(score)
                        if result == "retry":
                            main_game()
                        else:
                            running = False

            for meteor in meteors:
                meteor.draw(screen)

            current_time = pygame.time.get_ticks()
            if current_time - last_clone_time > clone_interval:
                meteors.append(Meteor())
                last_clone_time = current_time

            rocket.draw(screen)
            for flash in flashes[:]:
                x, y, size = flash
                pygame.draw.circle(screen, WHITE, (x + size // 2, y + size // 2), size // 2, 5)
                flashes.remove(flash)

            font = pygame.font.SysFont("Arial", 30)
            score_text = font.render(f"PUNTEGGIO: {score}", True, WHITE)
            screen.blit(score_text, (10, 10))

        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()
