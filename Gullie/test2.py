import math
import random
import pygame

pygame.init()

WIDTH, HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Roomblade")
CLOCK = pygame.time.Clock()

FONT = pygame.font.SysFont(None, 26)
SMALL_FONT = pygame.font.SysFont(None, 21)
LARGE_FONT = pygame.font.SysFont(None, 48)

DOOR_HALF = 80
PLAYER_RADIUS = 15
PLAYER_SPEED = 220
STAIRS = (WIDTH - 78, HEIGHT - 78)

rooms = {}
arrows = []
floor_number = 1
room_x = 0
room_y = 0
game_over = False
floor_notice = 0.0

mouse_pos = [WIDTH // 2 + 100, HEIGHT // 2]
mouse_down = False

class Player:
    def __init__(self):
        self.x = WIDTH // 2
        self.y = HEIGHT // 2
        self.r = PLAYER_RADIUS
        self.speed = PLAYER_SPEED
        self.health = 5
        self.max_health = 5
        self.facing_x = 1.0
        self.facing_y = 0.0
        self.sword_cooldown = 0.0
        self.bow_cooldown = 0.0
        self.invuln = 0.0

player = Player()


def room_key(x, y):
    return (floor_number, x, y)


def room_seed(x, y):
    return (floor_number * 73856093 + x * 19349663 + y * 83492791) & 0xFFFFFFFF


def get_room_enemies(x, y):
    key = room_key(x, y)

    if key not in rooms:
        rng = random.Random(room_seed(x, y))

        # More enemies on later floors, up to 8 per room.
        count = 2 + rng.randint(0, 2) + min(floor_number - 1, 6)

        # Enemies gain health and speed as the floors advance.
        enemy_health = 2 + (floor_number - 1) // 2
        enemy_speed = min(48 + floor_number * 8, 140)

        enemies = []
        for _ in range(count):
            while True:
                ex = rng.randint(90, WIDTH - 90)
                ey = rng.randint(90, HEIGHT - 90)
                if math.hypot(ex - WIDTH / 2, ey - HEIGHT / 2) > 110:
                    break

            enemies.append({
                "x": float(ex),
                "y": float(ey),
                "r": 14,
                "health": enemy_health,
                "max_health": enemy_health,
                "speed": enemy_speed + rng.random() * 12,
                "flash": 0.0,
            })

        rooms[key] = enemies

    return rooms[key]


def current_enemies():
    return get_room_enemies(room_x, room_y)


def update_facing_from_mouse():
    dx = mouse_pos[0] - player.x
    dy = mouse_pos[1] - player.y
    length = math.hypot(dx, dy)

    if length:
        player.facing_x = dx / length
        player.facing_y = dy / length


def damage_enemy(enemy, damage=1):
    enemy["health"] -= damage
    enemy["flash"] = 0.14


def transition_room(dx, dy):
    global room_x, room_y, arrows

    room_x += dx
    room_y += dy
    arrows.clear()

    if dx > 0:
        player.x = player.r + 4
    elif dx < 0:
        player.x = WIDTH - player.r - 4

    if dy > 0:
        player.y = player.r + 4
    elif dy < 0:
        player.y = HEIGHT - player.r - 4


def descend_floor():
    global floor_number, room_x, room_y, arrows, floor_notice

    floor_number += 1
    room_x = 0
    room_y = 0
    arrows.clear()

    player.x = WIDTH // 2
    player.y = HEIGHT // 2
    player.health = min(player.max_health, player.health + 1)

    floor_notice = 2.0


def restart_game():
    global floor_number, room_x, room_y, arrows, game_over

    rooms.clear()
    arrows.clear()
    floor_number = 1
    room_x = 0
    room_y = 0
    game_over = False

    player.x = WIDTH // 2
    player.y = HEIGHT // 2
    player.health = player.max_health
    player.invuln = 0.0
    player.sword_cooldown = 0.0
    player.bow_cooldown = 0.0


def attack_with_sword():
    for enemy in current_enemies():
        dx = enemy["x"] - player.x
        dy = enemy["y"] - player.y
        distance = math.hypot(dx, dy)

        if distance < 62:
            dot = (dx * player.facing_x + dy * player.facing_y) / max(distance, 1)
            if dot > 0.15:
                damage_enemy(enemy)


def shoot_arrow():
    arrows.append({
        "x": player.x + player.facing_x * 20,
        "y": player.y + player.facing_y * 20,
        "vx": player.facing_x * 460,
        "vy": player.facing_y * 460,
        "life": 1.4,
    })


def move_player(dt):
    keys = pygame.key.get_pressed()
    mx = 0
    my = 0

    if keys[pygame.K_a] or keys[pygame.K_LEFT]:
        mx -= 1
    if keys[pygame.K_d] or keys[pygame.K_RIGHT]:
        mx += 1
    if keys[pygame.K_w] or keys[pygame.K_UP]:
        my -= 1
    if keys[pygame.K_s] or keys[pygame.K_DOWN]:
        my += 1

    if mx or my:
        length = math.hypot(mx, my)
        mx /= length
        my /= length
        player.x += mx * player.speed * dt
        player.y += my * player.speed * dt
        player.facing_x = mx
        player.facing_y = my

    vertical_door = abs(player.y - HEIGHT / 2) < DOOR_HALF
    horizontal_door = abs(player.x - WIDTH / 2) < DOOR_HALF

    if player.x < player.r and vertical_door:
        transition_room(-1, 0)
    elif player.x > WIDTH - player.r and vertical_door:
        transition_room(1, 0)
    else:
        player.x = max(player.r, min(WIDTH - player.r, player.x))

    if player.y < player.r and horizontal_door:
        transition_room(0, -1)
    elif player.y > HEIGHT - player.r and horizontal_door:
        transition_room(0, 1)
    else:
        player.y = max(player.r, min(HEIGHT - player.r, player.y))


def update_enemies(dt):
    global game_over

    for enemy in current_enemies():
        enemy["flash"] = max(0.0, enemy["flash"] - dt)

        dx = player.x - enemy["x"]
        dy = player.y - enemy["y"]
        distance = math.hypot(dx, dy) or 1.0

        enemy["x"] += dx / distance * enemy["speed"] * dt
        enemy["y"] += dy / distance * enemy["speed"] * dt

        if distance < player.r + enemy["r"] and player.invuln <= 0:
            player.health -= 1
            player.invuln = 0.9

            if player.health <= 0:
                game_over = True


def update_arrows(dt):
    global arrows

    enemies = current_enemies()

    for arrow in arrows:
        arrow["x"] += arrow["vx"] * dt
        arrow["y"] += arrow["vy"] * dt
        arrow["life"] -= dt

        for enemy in enemies:
            if enemy["health"] > 0:
                distance = math.hypot(
                    arrow["x"] - enemy["x"],
                    arrow["y"] - enemy["y"]
                )
                if distance < enemy["r"] + 5:
                    damage_enemy(enemy)
                    arrow["life"] = 0
                    break

    arrows = [
        arrow for arrow in arrows
        if arrow["life"] > 0
        and 0 < arrow["x"] < WIDTH
        and 0 < arrow["y"] < HEIGHT
    ]


def remove_defeated_enemies():
    key = room_key(room_x, room_y)
    rooms[key] = [enemy for enemy in current_enemies() if enemy["health"] > 0]


def draw_walls():
    wall = (99, 111, 120)
    half = DOOR_HALF
    mid_x = WIDTH // 2
    mid_y = HEIGHT // 2

    # Top and bottom walls, with door openings.
    pygame.draw.rect(SCREEN, wall, (0, 0, mid_x - half, 18))
    pygame.draw.rect(SCREEN, wall, (mid_x + half, 0, WIDTH - mid_x - half, 18))
    pygame.draw.rect(SCREEN, wall, (0, HEIGHT - 18, mid_x - half, 18))
    pygame.draw.rect(SCREEN, wall, (mid_x + half, HEIGHT - 18, WIDTH - mid_x - half, 18))

    # Left and right walls, with door openings.
    pygame.draw.rect(SCREEN, wall, (0, 18, 18, mid_y - half - 18))
    pygame.draw.rect(SCREEN, wall, (0, mid_y + half, 18, HEIGHT - mid_y - half))
    pygame.draw.rect(SCREEN, wall, (WIDTH - 18, 18, 18, mid_y - half - 18))
    pygame.draw.rect(SCREEN, wall, (WIDTH - 18, mid_y + half, 18, HEIGHT - mid_y - half))

    # Door trim.
    trim = (174, 122, 92)
    pygame.draw.rect(SCREEN, trim, (mid_x - half, 0, half * 2, 8))
    pygame.draw.rect(SCREEN, trim, (mid_x - half, HEIGHT - 8, half * 2, 8))
    pygame.draw.rect(SCREEN, trim, (0, mid_y - half, 8, half * 2))
    pygame.draw.rect(SCREEN, trim, (WIDTH - 8, mid_y - half, 8, half * 2))


def draw_background():
    SCREEN.fill((26, 35, 40))

    for x in range(0, WIDTH, 42):
        pygame.draw.line(SCREEN, (38, 52, 58), (x, 0), (x, HEIGHT), 1)
    for y in range(0, HEIGHT, 42):
        pygame.draw.line(SCREEN, (38, 52, 58), (0, y), (WIDTH, y), 1)

    draw_walls()


def draw_stairs():
    if current_enemies():
        return

    x, y = STAIRS
    pygame.draw.rect(SCREEN, (105, 75, 43), (x - 27, y - 25, 54, 50), border_radius=5)
    pygame.draw.rect(SCREEN, (219, 180, 95), (x - 23, y - 21, 46, 42), border_radius=4)

    for step in range(3):
        pygame.draw.line(
            SCREEN, (105, 75, 43),
            (x - 17, y - 12 + step * 12),
            (x + 17, y - 12 + step * 12),
            3,
        )

    if math.hypot(player.x - x, player.y - y) < 60:
        prompt = SMALL_FONT.render("Press E to descend", True, (255, 242, 190))
        SCREEN.blit(prompt, (x - prompt.get_width() // 2, y - 48))


def draw_enemy(enemy):
    color = (255, 241, 166) if enemy["flash"] > 0 else (204, 92, 86)
    pos = (int(enemy["x"]), int(enemy["y"]))
    pygame.draw.circle(SCREEN, color, pos, enemy["r"])

    bar_x = int(enemy["x"] - 14)
    bar_y = int(enemy["y"] - 23)
    pygame.draw.rect(SCREEN, (53, 30, 32), (bar_x, bar_y, 28, 5))
    ratio = max(0, enemy["health"] / enemy["max_health"])
    pygame.draw.rect(SCREEN, (243, 162, 154), (bar_x, bar_y, int(28 * ratio), 5))


def draw_player():
    blinking = player.invuln > 0 and (pygame.time.get_ticks() // 90) % 2 == 0
    if blinking:
        return

    pygame.draw.circle(
        SCREEN, (96, 184, 214),
        (int(player.x), int(player.y)), player.r
    )

    end = (
        int(player.x + player.facing_x * 24),
        int(player.y + player.facing_y * 24),
    )
    pygame.draw.line(
        SCREEN, (223, 239, 255),
        (int(player.x), int(player.y)), end, 3
    )

    if player.sword_cooldown > 0.18:
        angle = math.atan2(player.facing_y, player.facing_x)
        rect = pygame.Rect(player.x - 43, player.y - 43, 86, 86)
        pygame.draw.arc(
            SCREEN, (228, 230, 196), rect,
            angle - 0.7, angle + 0.7, 5
        )


def draw_arrows():
    for arrow in arrows:
        start = (int(arrow["x"]), int(arrow["y"]))
        end = (
            int(arrow["x"] - arrow["vx"] * 0.04),
            int(arrow["y"] - arrow["vy"] * 0.04),
        )
        pygame.draw.line(SCREEN, (244, 209, 138), start, end, 4)


def draw_hud():
    room_text = FONT.render(
        f"Floor {floor_number}   Room {room_x}, {room_y}",
        True, (220, 230, 235)
    )
    SCREEN.blit(room_text, (24, 22))

    enemies = current_enemies()
    status = "Room cleared" if not enemies else f"Enemies: {len(enemies)}"
    SCREEN.blit(SMALL_FONT.render(status, True, (220, 230, 235)), (24, 50))

    hp = FONT.render(f"HP: {player.health}/{player.max_health}", True, (244, 145, 137))
    SCREEN.blit(hp, (WIDTH - hp.get_width() - 24, 22))

    if floor_notice > 0:
        notice = LARGE_FONT.render(f"Floor {floor_number}", True, (255, 224, 153))
        SCREEN.blit(
            notice,
            (WIDTH // 2 - notice.get_width() // 2, 72)
        )


def draw_game_over():
    overlay = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    overlay.fill((0, 0, 0, 185))
    SCREEN.blit(overlay, (0, 0))

    title = LARGE_FONT.render("You were defeated", True, (255, 255, 255))
    subtitle = FONT.render("Press R to restart", True, (255, 255, 255))

    SCREEN.blit(title, (WIDTH // 2 - title.get_width() // 2, HEIGHT // 2 - 30))
    SCREEN.blit(subtitle, (WIDTH // 2 - subtitle.get_width() // 2, HEIGHT // 2 + 25))


def main():
    global mouse_pos, mouse_down, game_over, floor_notice

    running = True
    while running:
        dt = min(CLOCK.tick(60) / 1000.0, 0.033)
        floor_notice = max(0.0, floor_notice - dt)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_r and game_over:
                    restart_game()

                elif event.key == pygame.K_SPACE and not game_over:
                    if player.sword_cooldown <= 0:
                        player.sword_cooldown = 0.38
                        attack_with_sword()

                elif event.key == pygame.K_e and not game_over:
                    if not current_enemies():
                        if math.hypot(
                            player.x - STAIRS[0],
                            player.y - STAIRS[1]
                        ) < 60:
                            descend_floor()

            elif event.type == pygame.MOUSEMOTION:
                mouse_pos = list(event.pos)

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                mouse_down = True
                mouse_pos = list(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                mouse_down = False

        if not game_over:
            player.sword_cooldown = max(0.0, player.sword_cooldown - dt)
            player.bow_cooldown = max(0.0, player.bow_cooldown - dt)
            player.invuln = max(0.0, player.invuln - dt)

            update_facing_from_mouse()
            move_player(dt)

            if mouse_down and player.bow_cooldown <= 0:
                player.bow_cooldown = 0.28
                shoot_arrow()

            update_enemies(dt)
            update_arrows(dt)
            remove_defeated_enemies()

        draw_background()
        draw_stairs()

        for enemy in current_enemies():
            draw_enemy(enemy)

        draw_arrows()
        draw_player()
        draw_hud()

        if game_over:
            draw_game_over()

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    main()