import sys
import pygame
import LineInfo
from pygame.locals import QUIT, MOUSEBUTTONDOWN


SCREEN_WIDTH = 624
SCREEN_HEIGHT = 816


def GetFileName(directory):
    files = LineInfo.GetFiles(directory)
    if len(files) >= 1:
        return files[0]
    return ""


def main():
    pygame.init()
    pygame.display.set_caption("Pygame Test")

    # 変数
    # SURFACE = pygame.display.set_mode((624, 816))
    surface = pygame.display.set_mode((SCREEN_WIDTH + 192, SCREEN_HEIGHT))
    fpsClock = pygame.time.Clock()

    counter = 0
    depth = 0
    mousepos = []

    backLines = []


    readRect  = pygame.Rect(644,  20, 152, 100)
    writeRect = pygame.Rect(644, 140, 152, 100)
    clearRect = pygame.Rect(644, 260, 152, 100)
    backRect  = pygame.Rect(644, 380, 152, 100)

    sysfont = pygame.font.SysFont(None, 36)
    readImage  = sysfont.render("read",  True, (200, 200, 200))
    writeImage = sysfont.render("write", True, (200, 200, 200))
    clearImage = sysfont.render("clear", True, (200, 200, 200))
    backImage  = sysfont.render("back",  True, (200, 200, 200))

    backImg = pygame.image.load("aaa.jpg").convert()

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(0, SCREEN_WIDTH) and y in range(0, SCREEN_HEIGHT):
                    mousepos.append(LineInfo.LineInfo(depth, x, y))
                    counter += 1

                elif x in range(readRect.left, readRect.right) and y in range(readRect.top, readRect.bottom):
                    mousepos = LineInfo.InputData(GetFileName("test/*"))
                    counter = len(mousepos)

                elif x in range(writeRect.left, writeRect.right) and y in range(writeRect.top, writeRect.bottom):
                    LineInfo.OutputData(GetFileName("test/*"), mousepos)
                    depth = mousepos[-1].depth

                elif x in range(clearRect.left, clearRect.right) and y in range(clearRect.top, clearRect.bottom):
                    mousepos = []
                    backLines = []
                    depth = 0
                    counter = 0

                elif x in range(backRect.left, backRect.right) and y in range(backRect.top, backRect.bottom):
                    files = LineInfo.GetFiles("view/*")
                    for name in files:
                        backLines.append(LineInfo.InputData(name))

            elif event.type == MOUSEBUTTONDOWN and event.button == 3:
                depth += 1

        surface.fill((0, 0, 0))

        #surface.blit(backImg, (-380, 50))        # 背景を描画

        pygame.draw.line(surface, (255, 255, 255), (SCREEN_WIDTH, 0), (SCREEN_WIDTH, SCREEN_HEIGHT), 1)
        pygame.draw.rect(surface, (255, 255, 255), readRect)
        pygame.draw.rect(surface, (255, 255, 255), writeRect)
        pygame.draw.rect(surface, (255, 255, 255), clearRect)
        pygame.draw.rect(surface, (255, 255, 255), backRect)

        surface.blit(readImage,  (664, 40))
        surface.blit(writeImage, (664, 160))
        surface.blit(clearImage, (664, 280))
        surface.blit(backImage,  (664, 400))

        countImage = sysfont.render("count {}".format(counter),  True, (200, 200, 200))
        surface.blit(countImage,  (664, 520))

        for arr in backLines:
            LineInfo.DrawLinesEx(surface, (128, 128, 128), arr)

        LineInfo.DrawLinesEx(surface, (255, 255, 255), mousepos)
        #for info in mousepos:
        #    pygame.draw.circle(SURFACE, (0, 255, 0), (info.x, info.y), 5)

        pygame.display.update()
        fpsClock.tick(30)


if __name__ == "__main__":
    main()
























