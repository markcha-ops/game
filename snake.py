import pygame
import sys
import random

# Pygame 초기화
pygame.init()

# 화면 크기 설정
screen_width = 800
screen_height = 600
cell_size = 20

# 색상 설정
white = (255, 255, 255)
black = (0, 0, 0)
green = (0, 255, 0)

# 화면 생성
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("지렁이 게임")

# 초기 위치 설정
snake_x = screen_width // 2
snake_y = screen_height // 2

# 초기 방향 설정
direction = "RIGHT"

# 초기 뱀 길이와 몸통 위치 설정
snake_length = 1
snake_body = [(snake_x, snake_y)]

# 초기 음식 위치 설정
food_x = random.randint(0, (screen_width // cell_size) - 1) * cell_size
food_y = random.randint(0, (screen_height // cell_size) - 1) * cell_size

# 게임 변수 설정
game_over = False
score = 0

# 게임 오버 메시지 설정
font = pygame.font.Font(None, 36)
game_over_text = font.render("Game Over", True, white)
game_over_text_rect = game_over_text.get_rect(center=(screen_width // 2, screen_height // 2))

# 2초 대기
pygame.time.delay(2000)

# 게임 루프
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and direction != "DOWN":
                direction = "UP"
            elif event.key == pygame.K_DOWN and direction != "UP":
                direction = "DOWN"
            elif event.key == pygame.K_LEFT and direction != "RIGHT":
                direction = "LEFT"
            elif event.key == pygame.K_RIGHT and direction != "LEFT":
                direction = "RIGHT"

    # 뱀 머리 이동
    if direction == "UP":
        snake_y -= cell_size
    elif direction == "DOWN":
        snake_y += cell_size
    elif direction == "LEFT":
        snake_x -= cell_size
    elif direction == "RIGHT":
        snake_x += cell_size

    # 뱀 머리와 음식 충돌 검사
    if snake_x == food_x and snake_y == food_y:
        score += 1
        food_x = random.randint(0, (screen_width // cell_size) - 1) * cell_size
        food_y = random.randint(0, (screen_height // cell_size) - 1) * cell_size
        snake_length += 1

    # 뱀 몸통 길이 관리
    snake_body.append((snake_x, snake_y))
    if len(snake_body) > snake_length:
        del snake_body[0]

    # 화면 초기화
    screen.fill(black)

    # 음식 그리기
    pygame.draw.rect(screen, green, (food_x, food_y, cell_size, cell_size))

    # 뱀 그리기
    for segment in snake_body:
        pygame.draw.rect(screen, white, (segment[0], segment[1], cell_size, cell_size))

    # 게임 오버 조건 추가: 화면 경계를 벗어났을 때
    if (
            snake_x >= screen_width
            or snake_x < 0
            or snake_y >= screen_height
            or snake_y < 0
    ):
        game_over = True

    # 점수 표시
    font = pygame.font.Font(None, 36)
    text = font.render("Score: " + str(score), True, white)
    screen.blit(text, (10, 10))

    # 게임 오버 상태일 때 게임 오버 메시지 표시
    if game_over:
        screen.blit(game_over_text, game_over_text_rect)

    # 화면 업데이트
    pygame.display.update()

    # 게임 속도 조절
    pygame.time.Clock().tick(10)

# 게임 종료 시 창을 닫을 때까지 대기
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()