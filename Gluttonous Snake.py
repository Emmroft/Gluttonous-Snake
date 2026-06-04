import pygame,sys,random
from pygame.locals import *
pygame.init()
font=pygame.font.Font(None,36)
lame_mode=0
producer=0
producer_Body=[[160,320],[160,340],[160,360],[160,380],[160,400],[160,420],[160,440],
               [180,320],[180,380],[180,440],
               [200,320],[200,380],[200,440],
               [220,320],[220,340],[220,360],[220,380],[220,400],[220,420],[220,440],
               [240,320],[240,380],[240,440],
               [260,320],[260,380],[260,440],
               [280,320],[280,340],[280,360],[280,380],[280,400],[280,420],[280,440],
               [320,320],[320,360],[320,380],[320,400],[320,420],[320,440],
               [340,320],[340,360],[340,380],[340,420],
               [360,320],[360,360],[360,400],[360,440],
               [380,320],[380,340],[380,360],[380,380],[380,400],[380,420],[380,440],
               [400,320],[400,360],[400,380],[400,420],
               [420,320],[420,360],[420,400],[420,440],
               [440,320],[440,360],[440,380],[440,400],[440,420],[440,440],
               [480,420],
               [500,340],[500,380],[500,420],
               [520,340],[520,380],[520,420],
               [540,320],[540,340],[540,360],[540,380],[540,400],[540,420],[540,440],
               [560,340],[560,380],[560,420],
               [580,340],[580,380],[580,420],
               [600,420]]
DISPLAY=pygame.display.set_mode((800,800))
pygame.display.set_caption('贪吃蛇')
FPSCLOCK=pygame.time.Clock()
WHITE=pygame.Color(255,255,255)
RED=pygame.Color(255,0,0)
GREEN=pygame.Color(0,255,0)
BLUE=pygame.Color(0,0,255)
snake_Head=[100,100]
snake_Body=[[100,100], [80,100],[60,100]]
direction="right"
changeDirection = direction
food_Postion = [300,300]
food_Total = 1
score = 0
def drawProducer(producer_Body):
    for i in producer_Body:
        pygame.draw.rect(DISPLAY,BLUE,Rect(i[0],i[1],20,20))
def drawSnake(snake_Body):
    for i in snake_Body:
        pygame.draw.rect(DISPLAY,GREEN,Rect(i[0],i[1],20,20))
def drawFood(food_Postion):
    pygame.draw.rect(DISPLAY,RED,Rect(food_Postion[0],food_Postion[1],20,20))
def gameover():
    pygame.quit()
    sys.exit()
game_flag=True
while game_flag:
    DISPLAY.fill(WHITE)
    drawSnake(snake_Body)
    drawFood(food_Postion)
    if lame_mode==1:
        for i in range(0,100):
            onSnake=1
            while onSnake == 1:
                    x = random.randrange(1, 39)
                    y = random.randrange(1, 39)
                    for i in range(len(snake_Body)):
                        food_Postions = [int(x * 20), int(y * 20)]
                        if snake_Body[i] == food_Postions:
                            onSnake=1
                            break
                        onSnake=0
            drawFood(food_Postions)
    game_speed=1+len(snake_Body)//3
    score_text=font.render("Score:"+str(score),1,(0,0,0))
    DISPLAY.blit(score_text,[690,760])
    if producer == 1:
        drawProducer(producer_Body)
    pygame.display.flip()
    FPSCLOCK.tick(game_speed)
    for event in pygame.event.get():
        if event.type==QUIT:
            gameover()
        elif event.type == KEYDOWN:
            if event.key == K_RIGHT or event.key == K_d:
                changeDirection = 'right'
            if event.key == K_LEFT or event.key == K_a:
                changeDirection = 'left'
            if event.key == K_UP or event.key == K_w:
                changeDirection = 'up'
            if event.key == K_DOWN or event.key == K_s:
                changeDirection = 'down'
            if event.key == K_ESCAPE:
                pygame.event.post(pygame.event.Event(QUIT))
            if event.key == K_l:
                if lame_mode == 0:
                    lame_mode=1
                elif lame_mode == 1:
                    lame_mode=0
            if event.key ==K_p:
                if producer == 0:
                    producer=1
                elif producer == 1:
                    producer=0
    if changeDirection == 'right' and not direction == 'left':
        direction = changeDirection
    if changeDirection == 'left' and not direction == 'right':
        direction = changeDirection
    if changeDirection == 'up' and not direction == 'down':
        direction = changeDirection
    if changeDirection == 'down' and not direction == 'up':
        direction = changeDirection
    if direction=='right':
        snake_Head[0]+=20
    if direction=='left':
        snake_Head[0]-=20
    if direction=='up':
        snake_Head[1]-=20
    if direction=='down':
        snake_Head[1]+=20
    snake_Body.insert(0,list(snake_Head))
    if snake_Head[0] == food_Postion[0] and snake_Head[1] == food_Postion[1]:
        food_Total = 0
        score+=1
    else:
        snake_Body.pop()
    if food_Total == 0:
        onSnake=1
        while onSnake == 1:
            x = random.randrange(1, 39)
            y = random.randrange(1, 39)
            for i in range(len(snake_Body)):
                food_Postion = [int(x * 20), int(y * 20)]
                if snake_Body[i] == food_Postion:
                    onSnake=1
                    break
                onSnake=0
        food_Total = 1
    if snake_Head[0] > 800 or snake_Head[0] < 0:
        gameover()
    elif snake_Head[1] > 800 or snake_Head[1] < 0:
        gameover()
    for body in snake_Body[1:]:
        if snake_Head[0] == body[0] and snake_Head[1] == body[1]:
            gameover()
