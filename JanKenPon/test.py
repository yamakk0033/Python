
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


    depth = 0
    mousepos = []
    fileName = ""


    readRect  = pygame.Rect(644,  20, 152, 100)
    writeRect = pygame.Rect(644, 140, 152, 100)

    sysfont = pygame.font.SysFont(None, 36)
    readImage  = sysfont.render("read",  True, (200, 200, 200))
    writeImage = sysfont.render("write", True, (200, 200, 200))

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(0, SCREEN_WIDTH) and y in range(0, SCREEN_HEIGHT):
                    mousepos.append(LineInfo.LineInfo(depth, x, y))

                elif x in range(readRect.left, readRect.right) and y in range(readRect.top, readRect.bottom):

                    if fileName == "":
                        files = LineInfo.GetFiles(fileName)
                        if len(files) > 1:
                            fileName = files[0]

                    mousepos = LineInfo.InputData(fileName)

                elif x in range(writeRect.left, writeRect.right) and y in range(writeRect.top, writeRect.bottom):

                    if fileName == "":
                        fileName = "test/aa.dat"

                    LineInfo.OutputData(fileName, mousepos)


            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                depth += 1

        SURFACE.fill((0, 0, 0))

        pygame.draw.line(SURFACE, (255, 255, 255), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 1)
        pygame.draw.rect(SURFACE, (255, 255, 255), readRect)
        pygame.draw.rect(SURFACE, (255, 255, 255), writeRect)

        SURFACE.blit(readImage,  (664, 40))
        SURFACE.blit(writeImage, (664, 160))

        LineInfo.DrawLinesEx(SURFACE, mousepos)
        #for info in mousepos:
        #    pygame.draw.circle(SURFACE, (0, 255, 0), (info.x, info.y), 5)

        pygame.display.update()
        FPSCLOCK.tick(5)


if __name__ == "__main__":
    main()




