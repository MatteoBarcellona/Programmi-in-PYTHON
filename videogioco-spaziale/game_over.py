import pygame
import sys

def game_over_screen(score):
    pygame.init()

    # Schermata
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
    WIDTH, HEIGHT = screen.get_size()

    # Font
    title_font = pygame.font.SysFont("Arial", 120, bold=True)
    text_font = pygame.font.SysFont("Arial", 60)
    button_font = pygame.font.SysFont("Arial", 50)

    # Musica di Game Over
    pygame.mixer.music.load("game_over_music.wav")
    pygame.mixer.music.play(-1)

    running = True
    while running:
        screen.fill((0, 0, 20))  # Sfondo più scuro per effetto spaziale

        # Testo "Game Over"
        game_over_text = title_font.render("GAME OVER", True, (255, 0, 0))
        screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))

        # Mostra punteggio
        score_text = text_font.render(f"PUNTEGGIO: {score}", True, (255, 255, 255))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2 - 100))

        # Mouse
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        # Pulsante "Riprova"
        retry_color = (0, 200, 0) if pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 80).collidepoint(mouse) else (0, 255, 0)
        retry_button = pygame.draw.rect(screen, retry_color, (WIDTH // 2 - 150, HEIGHT // 2 + 50, 300, 80), border_radius=20)
        retry_text = button_font.render("Riprova", True, (0, 0, 0))
        screen.blit(retry_text, (retry_button.x + retry_button.width // 2 - retry_text.get_width() // 2, retry_button.y + 15))

        # Pulsante "Esci"
        exit_color = (200, 0, 0) if pygame.Rect(WIDTH // 2 - 150, HEIGHT // 2 + 150, 300, 80).collidepoint(mouse) else (255, 0, 0)
        exit_button = pygame.draw.rect(screen, exit_color, (WIDTH // 2 - 150, HEIGHT // 2 + 150, 300, 80), border_radius=20)
        exit_text = button_font.render("Esci", True, (0, 0, 0))
        screen.blit(exit_text, (exit_button.x + exit_button.width // 2 - exit_text.get_width() // 2, exit_button.y + 15))

        # Eventi
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if retry_button.collidepoint(mouse):
                    pygame.mixer.music.stop()
                    return "retry"  # Ritorna al gioco
                if exit_button.collidepoint(mouse):
                    pygame.quit()
                    sys.exit()

        pygame.display.flip()

    pygame.quit()
