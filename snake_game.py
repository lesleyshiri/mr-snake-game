import pygame
import sys
import random
import os


IMAGE_PATH = r"c:\\Users\\shirill\\Documents\\python min project xxx\\6.png"
WIDTH, HEIGHT = 600, 500
CELL_SIZE = 20

SPEED_PRESETS = [
    ("Very Slow", 1),
    ("Slow", 3),
    ("Medium", 5),
    ("Fast", 10),
    ("Very Fast", 15),
]

HIGHSCORE_FILE = "highscore.txt"

current_speed_index = 2
fps_current = SPEED_PRESETS[current_speed_index][1]

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Mr Snake")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 32)
big_font = pygame.font.SysFont(None, 60)

try:
    background = pygame.image.load(IMAGE_PATH).convert()
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
except Exception as e:
    print("Background load error:", e)
    pygame.quit()
    sys.exit()

GRID_LEFT, GRID_TOP = 0, 0
GRID_RIGHT, GRID_BOTTOM = WIDTH, HEIGHT


def load_highscores():
    if not os.path.exists(HIGHSCORE_FILE):
        return []
    try:
        with open(HIGHSCORE_FILE, "r") as f:
            lines = f.read().strip().splitlines()
        scores = [int(s) for s in lines if s.strip().isdigit()]
        scores.sort(reverse=True)
        return scores[:5]
    except:
        return []


def save_highscores(current_score):
    scores = load_highscores()
    scores.append(current_score)
    scores = sorted(scores, reverse=True)[:5]
    with open(HIGHSCORE_FILE, "w") as f:
        for s in scores:
            f.write(str(s) + "\n")


def reset_game():
    global snake, direction, food, score, game_over
    snake = [(200, 200), (180, 200), (160, 200)]
    direction = (CELL_SIZE, 0)
    food = (
        random.randrange(GRID_LEFT, GRID_RIGHT, CELL_SIZE),
        random.randrange(GRID_TOP, GRID_BOTTOM, CELL_SIZE),
    )
    score = 0
    game_over = False


reset_game()

COLOR_NORMAL = (13, 110, 253)
COLOR_HOVER = (11, 94, 215)
COLOR_CLICK = (9, 78, 180)


def draw_button(rect, text, mouse_pos, mouse_down):
    if rect.collidepoint(mouse_pos):
        color = COLOR_CLICK if mouse_down else COLOR_HOVER
    else:
        color = COLOR_NORMAL

    glass_surf = pygame.Surface((rect.width, rect.height), pygame.SRCALPHA)
    pygame.draw.rect(glass_surf, (255, 255, 255, 70), glass_surf.get_rect(), border_radius=14)
    screen.blit(glass_surf, rect.topleft)

    inner_rect = rect.inflate(-6, -6)
    pygame.draw.rect(screen, color, inner_rect, border_radius=10)
    pygame.draw.rect(screen, (255, 255, 255), inner_rect, 2, border_radius=10)

    label = font.render(text, True, (255, 255, 255))
    screen.blit(
        label,
        (inner_rect.centerx - label.get_width() // 2, inner_rect.centery - label.get_height() // 2),
    )


def menu_loop():
    global current_speed_index, fps_current

    new_rect = pygame.Rect(WIDTH // 2 - 120, 150, 240, 50)
    high_rect = pygame.Rect(WIDTH // 2 - 120, 220, 240, 50)
    speed_rect = pygame.Rect(WIDTH // 2 - 120, 290, 240, 50)
    end_rect = pygame.Rect(WIDTH // 2 - 120, 360, 240, 50)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if new_rect.collidepoint(event.pos):
                    reset_game()
                    return "new"
                if high_rect.collidepoint(event.pos):
                    return "high"
                if speed_rect.collidepoint(event.pos):
                    current_speed_index = (current_speed_index + 1) % len(SPEED_PRESETS)
                    fps_current = SPEED_PRESETS[current_speed_index][1]
                if end_rect.collidepoint(event.pos):
                    pygame.quit()
                    sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key in (pygame.K_1, pygame.K_RETURN):
                    reset_game()
                    return "new"
                if event.key == pygame.K_2:
                    return "high"
                if event.key == pygame.K_3 or event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

        screen.blit(background, (0, 0))
        title = big_font.render("MR SNAKE MENU", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 60))

        draw_button(new_rect, "NEW GAME (1)", mouse_pos, mouse_down)
        draw_button(high_rect, "HIGH SCORE (2)", mouse_pos, mouse_down)

        speed_name, _ = SPEED_PRESETS[current_speed_index]
        draw_button(speed_rect, f"SPEED: {speed_name}", mouse_pos, mouse_down)

        draw_button(end_rect, "END GAME (3)", mouse_pos, mouse_down)

        pygame.display.flip()
        clock.tick(30)


def highscore_screen():
    best_list = load_highscores()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type in (pygame.KEYDOWN, pygame.MOUSEBUTTONDOWN):
                return

        screen.blit(background, (0, 0))
        title = big_font.render("MR SNAKE - TOP 5", True, (255, 255, 255))
        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 60))

        for idx, val in enumerate(best_list[:5]):
            line = font.render(f"{idx + 1}. {val}", True, (255, 215, 0))
            screen.blit(line, (WIDTH // 2 - line.get_width() // 2, 140 + idx * 40))

        info = font.render("Press any key to return", True, (255, 255, 255))
        screen.blit(info, (WIDTH // 2 - info.get_width() // 2, HEIGHT - 60))

        pygame.display.flip()
        clock.tick(30)


def game_over_screen():
    best_list = load_highscores()
    best = best_list[0] if best_list else 0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r:
                    reset_game()
                    return "replay"
                if event.key in (pygame.K_m, pygame.K_ESCAPE):
                    reset_game()
                    return "menu"

        screen.blit(background, (0, 0))

        title = big_font.render("GAME OVER", True, (255, 50, 50))
        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        best_text = font.render(f"Best: {best}", True, (255, 215, 0))
        info1 = font.render("R = Replay", True, (255, 255, 255))
        info2 = font.render("M or ESC = Menu", True, (255, 255, 255))

        screen.blit(title, (WIDTH // 2 - title.get_width() // 2, 120))
        screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, 200))
        screen.blit(best_text, (WIDTH // 2 - best_text.get_width() // 2, 240))
        screen.blit(info1, (WIDTH // 2 - info1.get_width() // 2, 310))
        screen.blit(info2, (WIDTH // 2 - info2.get_width() // 2, 350))

        pygame.display.flip()
        clock.tick(30)


while True:
    choice = menu_loop()

    if choice == "high":
        highscore_screen()
        continue

    menu_button_rect = pygame.Rect(WIDTH - 150, 10, 140, 40)

    while True:
        mouse_pos = pygame.mouse.get_pos()
        mouse_down = pygame.mouse.get_pressed()[0]

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                save_highscores(score)
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    save_highscores(score)
                    reset_game()
                    choice = "menu"
                    break
                if event.key == pygame.K_UP and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)
                elif event.key == pygame.K_DOWN and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif event.key == pygame.K_LEFT and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
                elif event.key == pygame.K_RIGHT and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)

            if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                if menu_button_rect.collidepoint(event.pos):
                    save_highscores(score)
                    reset_game()
                    choice = "menu"
                    break

        if choice == "menu":
            break

        if mouse_down:
            hx, hy = snake[0]
            mx, my = mouse_pos
            dx = mx - hx
            dy = my - hy
            if abs(dx) > abs(dy):
                if dx > 0 and direction != (-CELL_SIZE, 0):
                    direction = (CELL_SIZE, 0)
                elif dx < 0 and direction != (CELL_SIZE, 0):
                    direction = (-CELL_SIZE, 0)
            else:
                if dy > 0 and direction != (0, -CELL_SIZE):
                    direction = (0, CELL_SIZE)
                elif dy < 0 and direction != (0, CELL_SIZE):
                    direction = (0, -CELL_SIZE)

        hx, hy = snake[0]
        nh = (hx + direction[0], hy + direction[1])

        if nh[0] >= GRID_RIGHT:
            nh = (GRID_LEFT, nh[1])
        elif nh[0] < GRID_LEFT:
            nh = (GRID_RIGHT - CELL_SIZE, nh[1])
        if nh[1] >= GRID_BOTTOM:
            nh = (nh[0], GRID_TOP)
        elif nh[1] < GRID_TOP:
            nh = (nh[0], GRID_BOTTOM - CELL_SIZE)

        snake.insert(0, nh)

        if snake[0] == food:
            score += 1
            food = (
                random.randrange(GRID_LEFT, GRID_RIGHT, CELL_SIZE),
                random.randrange(GRID_TOP, GRID_BOTTOM, CELL_SIZE),
            )
        else:
            snake.pop()

        if snake[0] in snake[1:]:
            save_highscores(score)
            game_over = True

        screen.blit(background, (0, 0))

        for i, (x, y) in enumerate(snake):
            if i == 0:
                base_color = (0, 90, 200)
            else:
                base_color = (0, 140, 255)

            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(screen, base_color, rect, border_radius=6)
            pygame.draw.rect(screen, (0, 40, 100), rect, 2, border_radius=6)

            stripe_color = (
                base_color[0],
                min(255, base_color[1] + 50),
                min(255, base_color[2] + 30),
            )
            stripe_w = 2
            gap = 4
            for s in range(2, CELL_SIZE - 2, stripe_w + gap):
                pygame.draw.rect(
                    screen,
                    stripe_color,
                    (x + s, y + 3, stripe_w, CELL_SIZE - 6),
                    border_radius=2,
                )

            if i == 0:
                pygame.draw.circle(screen, (255, 255, 255), (x + 6, y + 7), 3)
                pygame.draw.circle(screen, (255, 255, 255), (x + CELL_SIZE - 6, y + 7), 3)
                pygame.draw.circle(screen, (0, 0, 0), (x + 6, y + 7), 1)
                pygame.draw.circle(screen, (0, 0, 0), (x + CELL_SIZE - 6, y + 7), 1)
                pygame.draw.line(
                    screen,
                    (255, 80, 80),
                    (x + CELL_SIZE // 2, y + CELL_SIZE),
                    (x + CELL_SIZE // 2, y + CELL_SIZE + 3),
                    2,
                )

        fx, fy = food
        cx = fx + CELL_SIZE // 2
        cy = fy + CELL_SIZE // 2
        r = CELL_SIZE // 2 - 1

        pygame.draw.circle(screen, (220, 0, 0), (cx, cy), r)
        pygame.draw.circle(screen, (255, 120, 120), (cx - 3, cy - 4), max(2, r - 4))
        pygame.draw.circle(screen, (150, 0, 0), (cx + 2, cy + 3), r - 2, width=2)
        leaf_rect = pygame.Rect(cx + r // 3, cy - r, r // 2, r // 2)
        pygame.draw.ellipse(screen, (0, 160, 0), leaf_rect)
        pygame.draw.line(screen, (120, 70, 20), (cx, cy - r), (cx, cy - r - 4), 2)

        best_list = load_highscores()
        best = best_list[0] if best_list else 0
        speed_name, _ = SPEED_PRESETS[current_speed_index]

        score_text = font.render(f"Score: {score}", True, (255, 255, 255))
        best_text = font.render(f"Best: {best}", True, (255, 255, 0))
        speed_text = font.render(f"Speed: {speed_name}", True, (255, 255, 255))
        screen.blit(score_text, (10, 10))
        screen.blit(best_text, (10, 40))
        screen.blit(speed_text, (10, 70))

        draw_button(menu_button_rect, "MENU (ESC)", mouse_pos, mouse_down)

        pygame.display.flip()
        clock.tick(fps_current)

        save_highscores(score)

        if game_over:
            result = game_over_screen()
            if result == "replay":
                break
            if result == "menu":
                choice = "menu"
                break
