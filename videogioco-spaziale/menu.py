import pygame
import random
import sys
import math

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
YELLOW = (255, 255, 0)
BLUE = (0, 0, 255)
LIGHT_BLUE = (100, 100, 255)

screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
WIDTH, HEIGHT = screen.get_size()
pygame.display.set_caption("Videogioco Spaziale - Matteo Edition")

pygame.mixer.music.load("title_music.mp3")
pygame.mixer.music.set_volume(0.5)

stars = [(random.randint(0, WIDTH), random.randint(0, HEIGHT)) for _ in range(200)]

def draw_text_with_outline(text, font, x, y, text_color, outline_color, screen):
    text_surface = font.render(text, True, text_color)
    outline_surface = font.render(text, True, outline_color)

    for dx, dy in [(-2, 0), (2, 0), (0, -2), (0, 2)]:
        screen.blit(outline_surface, (x + dx, y + dy))

    screen.blit(text_surface, (x, y))

def show_manual():
    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)
        for star in stars:
            pygame.draw.circle(screen, WHITE, star, 2)
        
        font = pygame.font.SysFont("Arial", 50)
        manual_text = [
            "Manuale del Gioco",
            "1. Usa le frecce per muovere la navicella:",
            "   - Freccia ->: Avanti",
            "   - Freccia <-: Indietro",
            "2. Premi SPAZIO per sparare.",
            "",
            "Premi ESC per tornare al menu."
        ]

        y_offset = 100
        for line in manual_text:
            text_surface = font.render(line, True, WHITE)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, y_offset))
            y_offset += 60

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False

        pygame.display.flip()
        clock.tick(60)

def main_menu():
    pygame.mixer.music.play(-1) 

    running = True
    clock = pygame.time.Clock()

    while running:
        screen.fill(BLACK)

        for i in range(len(stars)):
            pygame.draw.circle(screen, WHITE, stars[i], 2)
            stars[i] = (stars[i][0], (stars[i][1] + 1) % HEIGHT)

        title_font = pygame.font.SysFont("Arial", 120, bold=True)
        subtitle_font = pygame.font.SysFont("Arial", 50, italic=True)
        title_text = "Videogioco Spaziale ES"
        subtitle_text = "Made by Matteo Barcellona"

        draw_text_with_outline(title_text, title_font, WIDTH // 2 - title_font.size(title_text)[0] // 2,
                               HEIGHT // 4, YELLOW, RED, screen)
        draw_text_with_outline(subtitle_text, subtitle_font, WIDTH // 2 - subtitle_font.size(subtitle_text)[0] // 2,
                               HEIGHT // 4 + 100, WHITE, LIGHT_BLUE, screen)

        button_font = pygame.font.SysFont("Arial", 50, bold=True)

        play_color = LIGHT_BLUE if pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2, 400, 80).collidepoint(pygame.mouse.get_pos()) else BLUE
        play_button = pygame.draw.rect(screen, play_color, (WIDTH // 2 - 200, HEIGHT // 2, 400, 80), border_radius=20)
        play_text = button_font.render("Gioca", True, WHITE)
        screen.blit(play_text, (play_button.x + play_button.width // 2 - play_text.get_width() // 2, play_button.y + 15))

        manual_color = LIGHT_BLUE if pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 120, 400, 80).collidepoint(pygame.mouse.get_pos()) else BLUE
        manual_button = pygame.draw.rect(screen, manual_color, (WIDTH // 2 - 200, HEIGHT // 2 + 120, 400, 80), border_radius=20)
        manual_text = button_font.render("Manuale", True, WHITE)
        screen.blit(manual_text, (manual_button.x + manual_button.width // 2 - manual_text.get_width() // 2, manual_button.y + 15))

        exit_color = LIGHT_BLUE if pygame.Rect(WIDTH // 2 - 200, HEIGHT // 2 + 240, 400, 80).collidepoint(pygame.mouse.get_pos()) else BLUE
        exit_button = pygame.draw.rect(screen, exit_color, (WIDTH // 2 - 200, HEIGHT // 2 + 240, 400, 80), border_radius=20)
        exit_text = button_font.render("Esci", True, WHITE)
        screen.blit(exit_text, (exit_button.x + exit_button.width // 2 - exit_text.get_width() // 2, exit_button.y + 15))

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_button.collidepoint(mouse):
                    pygame.mixer.music.stop()
                    try:
                        import game
                        game.main_game()
                    except ImportError:
                        print("Errore: il modulo 'game' non è disponibile.")
                        running = False
                if manual_button.collidepoint(mouse):
                    show_manual()
                if exit_button.collidepoint(mouse):
                    running = False

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main_menu()
