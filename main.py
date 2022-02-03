import pygame, sys, time
from connect_four import ConnectFour

pygame.init()

def main(screen, s_width, block_size):
    clock = pygame.time.Clock()
    run = True

    connect_four = ConnectFour(block_size)

    font = pygame.font.SysFont('comicsans', 45)

    while run:
        clock.tick(60)
        connect_four.update_game(screen, block_size)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        if connect_four.game_over:
            if connect_four.status == 'Red wins!':
                color = (255,0,0)
            elif connect_four.status == 'Yellow wins!':
                color = (255,255,0)
            else:
                color = (224,224,224)

            label = font.render(f'{connect_four.status}', 0, color)
            label_rect = label.get_rect(midtop = (s_width/2, 5))

            for _ in range(250):
                time.sleep(0.01)
                screen.blit(label, label_rect)
                pygame.display.update()
            else:
                run = False

        pygame.display.update()

def main_menu():
    clock = pygame.time.Clock()
    font = pygame.font.SysFont('comicsans', 50)

    layout = [[['O', (j,i)] if i > 0 else [' ', (j,i)] for j in range(10)] for i in range(10)]

    block_size = 64
    s_width, s_height = len(layout[0]) * block_size, len(layout) * block_size
    screen = pygame.display.set_mode((s_width, s_height))
    pygame.display.set_caption('Connect Four')

    connect_four_text = pygame.image.load('connect_four.png').convert_alpha()
    connect_four_text = pygame.transform.scale(connect_four_text, (442.75, 253.5))

    connect_four_rect = connect_four_text.get_rect(center = (s_width//2, s_height//4))

    while True:
        clock.tick(60)
        screen.fill((0,128,255))
        screen.blit(connect_four_text, connect_four_rect)

        label = font.render('Press Enter to start', 0, (255,255,255))
        label_rect = label.get_rect(midtop = (connect_four_rect.midbottom[0], connect_four_rect.midbottom[1] + 5))

        screen.blit(label, label_rect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    main(screen, s_width,block_size)

        pygame.display.update()

if __name__ == '__main__':
    main_menu()