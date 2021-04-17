import pygame
from dame.constants import FULLWIDTH, WIDTH, HEIGHT, SQUARE_SIZE, WHITE, BLACK
from dame.game import Game
from minimax.algo import minimax

FPS = 60

WIN = pygame.display.set_mode((FULLWIDTH, HEIGHT))
pygame.display.set_caption('Jeu de dames')

def get_row_col_from_mouse(pos):
    x, y = pos
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    return row, col

def show_text(screen, turn):
    font = pygame.font.SysFont('Arial', 25)
    text = font.render("Tour : " + str(turn), True, (255, 255, 255))
    screen.blit(text, (910, 50))

def main():
    run = True
    clock = pygame.time.Clock()
    game = Game(WIN)

    pygame.init()

    while run:
        clock.tick(FPS)

        if game.turn == BLACK:
            show_text(WIN, "Noir")
            pygame.display.update()
            value, new_board = minimax(game.get_board(), 3, BLACK, game)
            game.ai_move(new_board)
        elif game.turn == WHITE:
            show_text(WIN, "Blanc")
            pygame.display.update()

        if game.winner() != None:
            print(game.winner())
            run = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = get_row_col_from_mouse(pos)
                game.select(row, col)

        game.update()
    
    pygame.quit()

main()