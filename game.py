import pygame
import pentago
import headers
import time
import generator
import bot1
import bot2
from math import sqrt

L=[0, 384]
A=[124, 896]

def check_turn():
    for i in M:
        for j in i:
            print(j, end='')
        print('')
    print('')

class menu:

    def draw(self):
        font1 = pygame.font.SysFont("comicsansms", 32)
        pygame.draw.rect(screen, (50, 100, 150), (256, 128, 512, 50))
        pygame.draw.rect(screen, (50, 100, 150), (256, 192, 512, 50))
        pygame.draw.rect(screen, (50, 100, 150), (256, 256, 250, 50))
        pygame.draw.rect(screen, (50, 100, 150), (518, 256, 250, 50))
        pygame.draw.rect(screen, (50, 100, 150), (256, 320, 250, 50))
        pygame.draw.rect(screen, (50, 100, 150), (518, 320, 250, 50))
        pygame.draw.rect(screen, (50, 100, 150), (256, 384, 512, 50))
        text1 = font1.render("Player vs player", True, (255, 255, 255))
        screen.blit(text1, ( (256 + 768 - text1.get_width()) // 2, (128 + 178 - text1.get_height()) // 2) )
        text2 = font1.render("Player vs bot", True, (255, 255, 255))
        screen.blit(text2, ( (256 + 768 - text2.get_width()) // 2, (192 + 242 - text2.get_height()) // 2) )
        text3 = font1.render("Open 4 (1 turn)", True, (255, 255, 255))
        screen.blit(text3, ( (256 + 512 - text3.get_width()) // 2, (256 + 306 - text3.get_height()) // 2) )
        text4 = font1.render("Open 4 (2 turn)", True, (255, 255, 255))
        screen.blit(text4, ( (768 + 512 - text4.get_width()) // 2, (256 + 306 - text4.get_height()) // 2) )
        text5 = font1.render("Open 3 (1 turn)", True, (255, 255, 255))
        screen.blit(text5, ( (256 + 512 - text5.get_width()) // 2, (320 + 370 - text5.get_height()) // 2) )
        text6 = font1.render("Open 3 (2 turn)", True, (255, 255, 255))
        screen.blit(text6, ( (768 + 512 - text6.get_width()) // 2, (320 + 370 - text6.get_height()) // 2) )
        text7 = font1.render("Bot vs bot", True, (255, 255, 255))
        screen.blit(text7, ( (256 + 768 - text7.get_width()) // 2, (384 + 434 - text7.get_height()) // 2) )

    def check(self, pos):
        x, y = pos
        if 256<=x<=768:
            if 128<=y<=178:
                return (1, 0, 0, 0, 0, 0, 0)
            elif 192<=y<=242:
                return (0, 0, 0, 0, 0, 0, 1)
            elif 384<=y<=434:
                return (0, 1, 0, 0, 0, 0, 0)
        if 256<=x<=506:
            if 256<=y<=306:
                return (0, 0, 1, 0, 0, 0, 0)
            if 320<=y<=370:
                return (0, 0, 0, 0, 1, 0, 0)
        if 518<=x<=768:
            if 256<=y<=306:
                return (0, 0, 0, 1, 0, 0, 0)
            if 320<=y<=370:
                return (0, 0, 0, 0, 0, 1, 0)
        return (0, 0, 0, 0, 0, 0, 0)


        
class Field:
    def draw_arrows(self):
        pygame.draw.polygon(screen, (50, 100, 150), [(128, 60), (178, 20), (178, 40), (250, 40), (250, 80), (178, 80), (178, 100)])
        pygame.draw.polygon(screen, (50, 100, 150), [(128, 956), (178, 916), (178, 936), (250, 936), (250, 976), (178, 976), (178, 996)])
        pygame.draw.polygon(screen, (50, 100, 150), [(896, 60), (846, 20), (846, 40), (774, 40), (774, 80), (846, 80), (846, 100)])
        pygame.draw.polygon(screen, (50, 100, 150), [(896, 956), (846, 916), (846, 936), (774, 936), (774, 976), (846, 976), (846, 996)])
        pygame.draw.polygon(screen, (50, 100, 150), [(60, 128), (20, 178), (40, 178), (40, 250), (80, 250), (80, 178), (100, 178)])
        pygame.draw.polygon(screen, (50, 100, 150), [(956, 128), (916, 178), (936, 178), (936, 250), (976, 250), (976, 178), (996, 178)])
        pygame.draw.polygon(screen, (50, 100, 150), [(60, 896), (20, 846), (40, 846), (40, 774), (80, 774), (80, 846), (100, 846)])
        pygame.draw.polygon(screen, (50, 100, 150), [(956, 896), (916, 846), (936, 846), (936, 774), (976, 774), (976, 846), (996, 846)])


    
    def check_arrows(self, pos):
        x1, y1 = pos
        if 140<=x1<=250:
            if 30<=y1<=90:
                return (2, 0)
            elif 926<=y1<=986:
                return (3, 1)
        elif 774<=x1<=880:
            if 30<=y1<=90:
                return (1, 1)
            elif 926<=y1<=986:
                return (4, 0)
        elif 30<=x1<=90:
            if 140<=y1<=250:
                return(2, 1)
            elif 774<=y1<=880:
                return(3, 0)
        elif 926<=x1<=986:
            if 140<=y1<=250:
                return(1, 0)
            elif 774<=y1<=880:
                return(4, 1)
        return 0

    
    def draw(self, Mat):
        for i in L:
            for j in L:
                pygame.draw.rect(screen, (0, 0, 0), (i+128, j+128, 384, 384), 10)
                pygame.draw.rect(screen, (50, 100, 150), (i+128, j+128, 384, 384))
                for ii in range(60, 384, 130):
                    for jj in range(60, 384, 130):
                        pygame.draw.circle(screen, (160, 160, 160), (i+128+ii, j+128+jj), 25)
        for i in range(6):
            for j in range(6):
                if M[i][j]=='X':
                    pygame.draw.circle(screen, (200, 0, 0), (188+130*(j%3)+384*(j//3), 188+130*(i%3)+384*(i//3)), 20)
                elif M[i][j]=='O':
                    pygame.draw.circle(screen, (0, 0, 0), (188+130*(j%3)+384*(j//3), 188+130*(i%3)+384*(i//3)), 20)    
        for i in A:
            for j in A:
                pygame.draw.rect(screen, (0, 0, 0), (i, j, 5, 5))

                
    def put_ball(self, pos, s):
        t=0
        for i in L:
            for j in L:
                for ii in range(60, 384, 130):
                    for jj in range(60, 384, 130):
                        length=sqrt((i+128+ii-pos[0])**2+(j+128+jj-pos[1])**2)
                        if length<=25:
                            #pygame.draw.circle(screen, (200, 0, 0), (i+128+ii, j+128+jj), 20)
                            x1=(ii-60)//130+3*i//384+1
                            y1=(jj-60)//130+3*j//384+1
                            print(x1, y1)
                            if M[y1-1][x1-1]=='.':
                                for i in M:
                                    for j in i:
                                        print(j, end='')
                                    print('')
                                t=1
                                return (x1, y1)
        return 0

M=pentago.M
pygame.init()
screen = pygame.display.set_mode((1024, 1024), pygame.RESIZABLE)
#screen = pygame.transform.scale(screen, (100, 100))
clock = pygame.time.Clock()
pygame.display.set_caption("Pentago")
background_image = pygame.image.load('images/background.jpg')
fil=Field()
ba, ra, bb, rb = (0, 0, 0, 0)
x, y, q, r=(0, 0, 0, 0)
font = pygame.font.SysFont("comicsansms", 40)
text = font.render("Chose game mode", True, (200, 0, 0))
tr = True
menu1 = menu()
end = 0
menu2 = 1
player = 1
pvp, bvb, o31, o32, o41, o42, pvb = (0, 0, 0, 0, 0, 0, 0)
col = 'X'
while tr:
    screen.blit(background_image, (0, 0))
    if menu2:
        menu1.draw()
    else:
        fil.draw(M)

    if pvp or bvb or pvb:
        if ba == 0 and bb == 0 and ra == 0 and rb == 0 and not end:
            ba = 1
    elif o41 or o42:
        if ba == 0 and bb == 0 and ra == 0 and rb == 0 and not end and o41:
            ba = 1
            M, pass_value = generator.make_4_1()
            counter = 1
        elif ba == 0 and bb == 0 and ra == 0 and rb == 0 and not end and o42:
            ba = 1
            M, *pass_value = generator.make_4_2()
            counter = 2
        else:
            if counter == 0:
                fuflo = generator.check_4(M)
                if fuflo:
                    text = font.render("You are right! press R to play again or Esc to exit", True, (200, 0, 0))
                    bb = 0
                    end = 1
                else:
                    text = font.render("You are not right! press R to play again or Esc to exit", True, (200, 0, 0))
                    bb = 0
                    end = 1
    elif o31 or o32:
        if ba == 0 and bb == 0 and ra == 0 and rb == 0 and not end and o31:
            ba = 1
            M = generator.make_3_1()
            counter = 1
        elif ba == 0 and bb == 0 and ra == 0 and rb == 0 and not end and o32:
            ba = 1
            M, *pass_value = generator.make_3_2()
            counter = 2
        else:
            if counter == 0:
                fuflo = generator.check_3(M)
                if fuflo:
                    text = font.render("You are right! press R to play again or Esc to exit", True, (200, 0, 0))
                    bb = 0
                    end = 1
                else:
                    text = font.render("You are not right! press R to play again or Esc to exit", True, (200, 0, 0))
                    bb = 0
                    end = 1    
    if ba or bb or ra or rb:
        if headers.check('X', M):
            text = font.render("Player A won! Press R to restart or Esc to close", True, (200, 0, 0))
            bb = 0
            ra = 0
            rb = 0
            end = 1
        if headers.check('O', M):
            text = font.render("Player B won! Press R to restart or Esc to close", True, (200, 0, 0))
            ba = 0
            rb = 0
            ra = 0
            end = 1
    t = False
    for i in M:
        for j in i:
            if j == '.':
                t = True
    if not t:
        if ba and bb:
            text = font.render("Draw! Press R to restart or Esc to close", True, (200, 0, 0))
            ba, bb, end = (0, 0, 1)
        
    if ra or rb:
        fil.draw_arrows()
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            tr=False
            break

        if ba:
            if bvb or (pvb and player == 2):
                if event.type == pygame.KEYDOWN:
                    x, y, q, r = bot1.make_turn(M, 'X')
                    pentago.put( x, y, 1, 1, 'X', M)
                    ba=0
                    ra=1
                    check_turn()
                    time.sleep(0.1)
            elif event.type == pygame.MOUSEBUTTONDOWN : 
                pos=event.pos
                z=fil.put_ball(pos, 'X')
                if z:
                    x, y = z
                    pentago.put( x, y, 1, 1, 'X', M)
                    ba=0
                    ra=1
        elif ra:
            if bvb  or (pvb and player == 2):
                if event.type == pygame.KEYDOWN:
                    pentago.rotate(q, r, M)
                    ra = 0
                    bb = 1
                    text = font.render("Player B turn", True, (0, 0, 0))
                    check_turn()
                    time.sleep(0.1)
            elif event.type == pygame.MOUSEBUTTONDOWN: 
                pos=event.pos
                z=fil.check_arrows(pos)
                if z:
                    if o41 or o42 or o31 or o32:
                        counter = counter - 1
                    q, r = z
                    pentago.rotate(q, r, M)
                    ra=0
                    bb=1
                    text = font.render("Player B turn", True, (0, 0, 0))
                    time.sleep(0.1)
                    
        elif bb:
            if (o42 or o32) and event.type == pygame.KEYDOWN:
                x, y, q, r = bot1.make_turn(M, 'O')
                pentago.put( x, y, 1, 1, 'O', M)
                bb=0
                rb=1
                check_turn()
                time.sleep(0.1)
            if bvb or (pvb and player == 1):
                if event.type == pygame.KEYDOWN:
                    if bvb:
                        x, y, q, r = bot2.make_turn(M)
                    else:
                        x, y, q, r = bot1.make_turn(M, 'O')
                    pentago.put( x, y, 1, 1, 'O', M)
                    bb=0
                    rb=1
                    check_turn()
                    time.sleep(0.1)
            elif event.type == pygame.MOUSEBUTTONDOWN and not o32 and not o42: 
                pos=event.pos
                z=fil.put_ball(pos, 'O')
                if z:
                    x, y = z
                    pentago.put( x, y, 1, 1, 'O', M)
                    bb=0
                    rb=1
        elif rb:
            if (o42 or o32) and event.type == pygame.KEYDOWN:
                pentago.rotate(q, r, M)
                rb=0
                ba=1
                text = font.render("Player A turn", True, (200, 0, 0))
                check_turn()
                time.sleep(0.1)
            if bvb or (pvb and player == 1):
                if event.type == pygame.KEYDOWN:
                    pentago.rotate(q, r, M)
                    rb = 0
                    ba = 1
                    text = font.render("Player A turn", True, (200, 0, 0))
                    check_turn()
                    time.sleep(0.1)
            elif event.type == pygame.MOUSEBUTTONDOWN and not o32 and not o42: 
                pos=event.pos
                z=fil.check_arrows(pos)
                if z:
                    q, r = z
                    pentago.rotate(q, r, M)
                    rb=0
                    ba=1
                    text = font.render("Player A turn", True, (200, 0, 0))
                    time.sleep(0.1)
        elif end:
            if event.type == pygame.KEYDOWN :
                key = pygame.key.name(event.key)
                print(key)
                if key == 'r':
                    text = font.render("Player A turn", True, (200, 0, 0))
                    end = 0
                    for i in range(6):
                        for j in range(6):
                            M[i][j] = '.'
                if key == 'escape':
                    
                    text = font.render("Chose gamemode", True, (200, 0, 0))
                    pvp, bvb, o31, o32, o41, o42 = (0, 0, 0, 0, 0, 0)
                    for i in range(6):
                        for j in range(6):
                            M[i][j] = '.'
                    menu2 = 1
                    end = 0
        elif menu2:
            if event.type == pygame.MOUSEBUTTONDOWN: 
                pos=event.pos
                pvp, bvb, o41, o42, o31, o32, pvb = menu1.check(pos)
            if pvp or bvb or o41 or o42 or o31 or o32 or pvb:
                menu2 = 0
                text = font.render("Player A turn", True, (200, 0, 0))
                
        if event.type == pygame.KEYDOWN and menu2 == 0:
            key = pygame.key.name(event.key)    
            if key == 'escape':
                pvp, bvb, o31, o32, o41, o42, pvb = (0, 0, 0, 0, 0, 0, 0)
                text = font.render("Chose gamemode", True, (200, 0, 0))
                ba, ra, bb, rb = (0, 0, 0, 0)
                for i in range(6):
                    for j in range(6):
                        M[i][j] = '.'
                    
                menu2 = 1
                end = 0   
        
                            
    screen.blit(text, ( (774-250 - text.get_width()) // 2 + 250, (128 - text.get_height() )// 2) )
    pygame.display.update()
    
    


if tr:
    print('draw')
pygame.quit()
