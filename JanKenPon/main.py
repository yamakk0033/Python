import sys
import pygame
import LineInfo
import random

from pygame.locals import QUIT, MOUSEBUTTONDOWN


IMAGE_NUM_MIN = 1
IMAGE_NUM_MIN = 4

SCREEN_WIDTH = 624
SCREEN_HEIGHT = 816


pygame.init()
pygame.display.set_caption("Pygame Test")

# 変数
surface = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
fpsClock = pygame.time.Clock()



def limit(n, nMax, nMin):
    if n > nMax:
        n = nMax
    elif n < nMin:
        n = nMin
    return n

def loop(n, nMax, nMin):
    if n > nMax:
        n = nMin
    elif n < nMin:
        n = nMax
    return n



def drawLine(buff, cnt = -1, viewCnt = -1):
    if cnt < 0:
        cnt = 0
    if viewCnt < 0:
        viewCnt = 0
    return LineInfo.DrawLinesEx(surface, (255, 255, 255), buff[cnt], viewCnt)

def main():

    changeCounter = 0
    viewCounter = 0

    enemyState = -1

    guWakuData = []
    guWakuData.append(LineInfo.InputData("material\\gu_waku1.dat"))
    guWakuData.append(LineInfo.InputData("material\\gu_waku2.dat"))
    guWakuData.append(LineInfo.InputData("material\\gu_waku3.dat"))
    guWakuData.append(LineInfo.InputData("material\\gu_waku4.dat"))

    tyokiWakuData = []
    tyokiWakuData.append(LineInfo.InputData("material\\tyoki_waku1.dat"))
    tyokiWakuData.append(LineInfo.InputData("material\\tyoki_waku2.dat"))
    tyokiWakuData.append(LineInfo.InputData("material\\tyoki_waku3.dat"))
    tyokiWakuData.append(LineInfo.InputData("material\\tyoki_waku4.dat"))

    paWakuData = []
    paWakuData.append(LineInfo.InputData("material\\pa-waku1.dat"))
    paWakuData.append(LineInfo.InputData("material\\pa-waku2.dat"))
    paWakuData.append(LineInfo.InputData("material\\pa-waku3.dat"))
    paWakuData.append(LineInfo.InputData("material\\pa-waku4.dat"))



    guData = []
    guData.append(LineInfo.InputData("material\\gu1.dat"))
    guData.append(LineInfo.InputData("material\\gu2.dat"))
    guData.append(LineInfo.InputData("material\\gu3.dat"))
    guData.append(LineInfo.InputData("material\\gu4.dat"))

    tyokiData = []
    tyokiData.append(LineInfo.InputData("material\\tyoki1.dat"))
    tyokiData.append(LineInfo.InputData("material\\tyoki2.dat"))
    tyokiData.append(LineInfo.InputData("material\\tyoki3.dat"))
    tyokiData.append(LineInfo.InputData("material\\tyoki4.dat"))

    paData = []
    paData.append(LineInfo.InputData("material\\pa-1.dat"))
    paData.append(LineInfo.InputData("material\\pa-2.dat"))
    paData.append(LineInfo.InputData("material\\pa-3.dat"))
    paData.append(LineInfo.InputData("material\\pa-4.dat"))



    guTekiData = []
    guTekiData.append(LineInfo.InputData("material\\teki_gu-1.dat"))
    guTekiData.append(LineInfo.InputData("material\\teki_gu-2.dat"))
    guTekiData.append(LineInfo.InputData("material\\teki_gu-3.dat"))
    guTekiData.append(LineInfo.InputData("material\\teki_gu-4.dat"))

    tyokiTekiData = []
    tyokiTekiData.append(LineInfo.InputData("material\\teki_tyoki1.dat"))
    tyokiTekiData.append(LineInfo.InputData("material\\teki_tyoki2.dat"))
    tyokiTekiData.append(LineInfo.InputData("material\\teki_tyoki3.dat"))
    tyokiTekiData.append(LineInfo.InputData("material\\teki_tyoki4.dat"))

    paTekiData = []
    paTekiData.append(LineInfo.InputData("material\\teki_pa-1.dat"))
    paTekiData.append(LineInfo.InputData("material\\teki_pa-2.dat"))
    paTekiData.append(LineInfo.InputData("material\\teki_pa-3.dat"))
    paTekiData.append(LineInfo.InputData("material\\teki_pa-4.dat"))



    guRect    = pygame.Rect(  0, 600, 208, 216)
    tyokiRect = pygame.Rect(208, 600, 208, 216)
    paRect    = pygame.Rect(416, 600, 208, 216)




    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == MOUSEBUTTONDOWN and event.button == 1:
                x, y = event.pos

                if x in range(guRect.left, guRect.right) and y in range(guRect.top, guRect.bottom):
                    enemyState = random.randint(0, 2)

                elif x in range(tyokiRect.left, tyokiRect.right) and y in range(tyokiRect.top, tyokiRect.bottom):
                    enemyState = random.randint(0, 2)

                elif x in range(paRect.left, paRect.right) and y in range(paRect.top, paRect.bottom):
                    enemyState = random.randint(0, 2)


        changeCounter = loop(changeCounter + 1, 10000, 0)
        viewCounter = limit(viewCounter + 1, 10000, 0)



        surface.fill((0, 0, 0))

#        pygame.draw.rect(surface, (255, 255, 255), guRect)
#        pygame.draw.rect(surface, (255, 255, 255), tyokiRect)
#        pygame.draw.rect(surface, (255, 255, 255), paRect)



        changeCnt = ((int)(changeCounter/10))%4
        seekViewCnt = 0

        drawLine(guWakuData, changeCnt, viewCounter - seekViewCnt)

        seekViewCnt += len(guWakuData[0])
        drawLine(guData, changeCnt, viewCounter - seekViewCnt)

        seekViewCnt += len(guData[0])
        drawLine(tyokiWakuData, changeCnt, viewCounter - seekViewCnt)

        seekViewCnt += len(tyokiWakuData[0])
        drawLine(tyokiData, changeCnt, viewCounter - seekViewCnt)

        seekViewCnt += len(tyokiData[0])
        drawLine(paWakuData, changeCnt, viewCounter - seekViewCnt)

        seekViewCnt += len(paWakuData[0])
        drawLine(paData, changeCnt, viewCounter - seekViewCnt)


        if enemyState == 0:
            drawLine(guTekiData, changeCnt, 10000)
        elif enemyState == 1:
            drawLine(tyokiTekiData, changeCnt, 10000)
        elif enemyState == 2:
            drawLine(paTekiData, changeCnt, 10000)


        pygame.display.update()
        fpsClock.tick(20)


if __name__ == "__main__":
    main()























