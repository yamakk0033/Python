import sys
import pygame
import LineInfo
from pygame.locals import QUIT, MOUSEBUTTONDOWN


SCREEN_WIDTH = 624
SCREEN_HEIGHT = 816

def main():
    pygame.init()
    pygame.display.set_caption("Pygame Test")

    # 変数
    # SURFACE = pygame.display.set_mode((624, 816))
    SURFACE = pygame.display.set_mode((SCREEN_WIDTH + 192, SCREEN_HEIGHT))
    FPSCLOCK = pygame.time.Clock()

    sysfont = pygame.font.SysFont(None, 36)

    mousepos = []

    readRect  = pygame.Rect(644,  20, 152, 100)
    writeRect = pygame.Rect(644, 140, 152, 100)
    read_image = sysfont.render("read", True, (200, 200, 200))
    write_image = sysfont.render("write", True, (200, 200, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN:
                if event.pos[0] in range(0, SCREEN_WIDTH) and event.pos[1] in range(0, SCREEN_HEIGHT):
                    mousepos.append(event.pos)
                    
                


        SURFACE.fill((0, 0, 0))

        pygame.draw.line(SURFACE, (255, 255, 255), (624, 0), (624, 816), 1)
        pygame.draw.rect(SURFACE, (255, 255, 255), readRect)
        pygame.draw.rect(SURFACE, (255, 255, 255), writeRect)

        SURFACE.blit(read_image,  (664, 40))
        SURFACE.blit(write_image, (664, 160))

        for i, j in mousepos:
            pygame.draw.circle(SURFACE, (0, 255, 0), (i, j), 5)


        pygame.display.update()
        FPSCLOCK.tick(30)


if __name__ == "__main__":
    main()



