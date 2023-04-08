
#импорт библиотеки pygame
from pygame import *
#импорт библиотеки time
import time as wait
init() #инициация PyGame


'-----------------------------------------------------------------------------ПЕРЕМЕННЫЕ----------------------------------------------------------------------------------------------------------------------------------------------------------'
WIN_WIDTH = 1280 #Ширина создаваемого окна
WIN_HEIGHT = 640 # Высота
DISPLAY = (WIN_WIDTH, WIN_HEIGHT) # Группируем ширину и высоту в одну переменную  

#главный персонаж
MOVE_SPEED = 7 #скорость перемещения 
P_WIDTH = 22 #ширина
P_HEIGHT = 32 #высота
JUMP_POWER = 10 #высота прыжка
GRAVITY = 0.35 # Сила, которая будет тянуть нас вниз

C_WHITE = (255, 255, 255) #белый
C_RED = (255, 0, 0) #красный 
C_GREEN = (0, 255, 0) #зеленый
C_BLACK = (0, 0, 0) #черный

#блок
PLATFORM_WIDTH = 32 #ширина
PLATFORM_HEIGHT = 32 #высота

#опасный блок
DANGER_PPLATFORM_WIDTH = 50 #ширина
DANGER_PPLATFORM_HEIGHT = 50 #высота

#монеты
COIN_WIDTH = 30 #ширина
COIN_HEIGHT = 30 #высота

#звезда
STAR_WIDTH = 60 #ширина
STAR_HEIGHT = 60 #высота

#объект взаимодействия
Doingobject_PLATFORM_WIDTH = 32 #ширина
Doingobject_PLATFORM_HEIGHT = 32 #высота

#платформа
PARKOUR_PPLATFORM_WIDTH = 40 #ширина
PARKOUR_PPLATFORM_HEIGHT = 20 #высота


'-----------------------------------------------------------------------------АНИМАЦИЯ----------------------------------------------------------------------------------------------------------------------------------------------------------'
#главный герой 
walk_right = [ #анимация ходьбы вправо
    transform.scale(image.load('r1.png'), (22, 32)),
    transform.scale(image.load('r2.png'), (22, 32)),
    transform.scale(image.load('r3.png'), (22, 32)),
    transform.scale(image.load('r4.png'), (22, 32)),
    transform.scale(image.load('r5.png'), (22, 32))
    ]

walk_left = [ #анимация ходьбы влево
    transform.scale(image.load('l1.png'), (22, 32)),
    transform.scale(image.load('l2.png'), (22, 32)),
    transform.scale(image.load('l3.png'), (22, 32)),
    transform.scale(image.load('l4.png'), (22, 32)),
    transform.scale(image.load('l5.png'), (22, 32))
            ]
jump_left = [ #анимация прыжка влево
    transform.scale(image.load('jl.png'), (22, 32))
    ]
jump_right = [ #анимация прыжка вправо
    transform.scale(image.load('jr.png'), (22, 32))
    ]
jump = [ #анимация прыжка
    transform.scale(image.load('j.png'), (22, 32))
    ]
stay = [ #анимация бездействия
    transform.scale(image.load('0.png'), (22, 32))
]

#враг
enemyanimleft = [ #анимация ходьбы влево
    image.load('e1.png'),
    image.load('e2.png'),
    image.load('e3.png'),
    image.load('e4.png'),
    image.load('e5.png'),
    image.load('e6.png'),
    image.load('e7.png'),
]
enemyanimright = [ #анимация ходьбы вправо
    image.load('re1.png'),
    image.load('re2.png'),
    image.load('re3.png'),
    image.load('re4.png'),
    image.load('re5.png'),
    image.load('re6.png'),
    image.load('re7.png'),
]

'-----------------------------------------------------------------------------МУЗЫКА И ЗВУКИ----------------------------------------------------------------------------------------------------------------------------------------------------------'

mixer.pre_init(44100, -16, 1, 512) #параметры для отсутствия задержки звука
vol = 0.5 #громкость звуков
mixer.music.set_volume(vol) #установка соответствующей громкости глобально
mixer.music.load('maingamesoundtrack.ogg') #загрузка файла (главная фоновая музыка)

JUMP = mixer.Sound('JUMP.ogg') #подключение звука прыжка
STEP = mixer.Sound('STEP.ogg') #подключение звука шага
DIE = mixer.Sound('DIE.ogg') #подключение звука смерти
COIN = mixer.Sound('COIN.ogg') #подключение звука монеты
OPEN = mixer.Sound('OPEN.ogg') #подключение звука открытия платформы
BONUS = mixer.Sound('BONUS.ogg') #подключение звука подбирания звезды
WIN = mixer.Sound('WIN.OGG') #подключение звука победы

'-----------------------------------------------------------------------------ШРИФТЫ----------------------------------------------------------------------------------------------------------------------------------------------------------'
#создание типов шрифтов
big_font = font.Font("pixelfont.ttf", 100) #жирный
regular_font = font.Font("pixelfont.ttf", 40) #тонкий

#создание текстов в переменных
game_over = big_font.render('Игра окончена', True, C_RED) 
restart_text = regular_font.render('Нажми R чтобы начать заново', True, C_WHITE)
win = big_font.render('Ты выиграл', True, C_GREEN)
pause_text = big_font.render('Игра приостановлена', True, C_WHITE)

'-----------------------------------------------------------------------------КЛАССЫ И ФУНКЦИИ----------------------------------------------------------------------------------------------------------------------------------------------------------'

'=================================конечный объект================================='
class EndingObject(sprite.Sprite):
    def __init__(self, x, y, width, height): 
        sprite.Sprite.__init__(self)
        self.width = width 
        self.height = height
        self.rect = Rect(x, y, width, height)
        self.add(EndingObjects) 

'=================================блок================================='
class Platform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("platform.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)

'=================================монета================================='
class Coin(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("coin.png"), (COIN_WIDTH, COIN_HEIGHT))
        self.rect = Rect(x, y, COIN_WIDTH, COIN_HEIGHT)

'=================================звезда================================='
class Star(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("bonus.png"), (STAR_WIDTH, STAR_HEIGHT))
        self.rect = Rect(x, y, STAR_WIDTH, STAR_HEIGHT)

'=================================заблокированный блок================================='
class LockedPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("lockedblock.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, PLATFORM_WIDTH, PLATFORM_HEIGHT)
        self.locked = True #заблокирован или нет?

'=================================опасный объект================================='
class DangerPlatform(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("dangerobject.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, DANGER_PPLATFORM_WIDTH, DANGER_PPLATFORM_HEIGHT)

class DangerPlatformleft(sprite.Sprite): #для левой стены
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("dangerobjectleft.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, DANGER_PPLATFORM_WIDTH, DANGER_PPLATFORM_HEIGHT)

class DangerPlatformright(sprite.Sprite): #для правой стены
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("dangerobjectright.png"), (PLATFORM_WIDTH, PLATFORM_HEIGHT))
        self.rect = Rect(x, y, DANGER_PPLATFORM_WIDTH, DANGER_PPLATFORM_HEIGHT)
'=================================платформа направленная влево================================='
class ParkourPlatformLeft(sprite.Sprite):
    def __init__(self, x, y, direction):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("parkourplatformright.png"), (PARKOUR_PPLATFORM_WIDTH, PARKOUR_PPLATFORM_HEIGHT))
        self.rect = Rect(x, y, PARKOUR_PPLATFORM_WIDTH, PARKOUR_PPLATFORM_HEIGHT)
        self.direction = direction #расположение: справа или слева

'=================================платформа направленная вправо================================='
class ParkourPlatformRight(sprite.Sprite):
    def __init__(self, x, y, direction):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("parkourplatformleft.png"), (PARKOUR_PPLATFORM_WIDTH, PARKOUR_PPLATFORM_HEIGHT))
        self.rect = Rect(x, y, PARKOUR_PPLATFORM_WIDTH, PARKOUR_PPLATFORM_HEIGHT)
        self.direction = direction #расположение: справа или слева

'=================================объект взаимодействия================================='
class Doingobject(sprite.Sprite):
    def __init__(self, x, y):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("nonactiveobject.png"), (Doingobject_PLATFORM_WIDTH, Doingobject_PLATFORM_HEIGHT))
        self.rect = Rect(x, y, Doingobject_PLATFORM_WIDTH, Doingobject_PLATFORM_HEIGHT)

'=================================передвигающийся блок================================='
class Movingblock(sprite.Sprite):
    def __init__(self, x, y, width, height):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("movingblock.png"), (width, height))
        self.rect = Rect(x, y, width, height)

    
    def collide(self, platforms): #обозначение границ
        if self.rect.x < 545: #левая граница
            self.rect.x = 545
        if self.rect.x > 920: #правая граница
            self.rect.x = 920

'=================================враг================================='     
class Enemy(sprite.Sprite):
    side = 'left' #сторона движения 
    def __init__(self, width, height, x, y, max_right_position, max_left_position, speed, **args):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("e1.png"), (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = speed #скорость
        self.max_left_position = max_left_position #максимальная левая позиция 
        self.max_right_position = max_right_position #максимальная правая позиция
        self.x = x 
        self.y = y
        self.width = width #ширина
        self.height = height #высота
        self.count = 0 #счетчик анимации
        self.add(enemies, entities) #добавление в группы спрайтов 
    
    def update(self): #передвижение 
        if self.rect.x <= self.max_left_position: #сторона меняется, если достигается заданное значение координат влево
            self.side = 'right'
        if self.rect.x >= self.max_right_position: #сторона меняется, если достигается заданное значение координат вправо
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed     
        self.collide()
        self.animation()

    def collide(self): #столкновение с игроком 
        if sprite.collide_rect(self, hero): #если происходит столкновение
            if self.side == 'right': #справа - игрок проигрывает                    
                hero.lose = True 
            if self.side == 'left': #слева - игрок проигрывает                    
                hero.lose = True 
            else:
                self.kill() #иначе объект исчезает
    
    def animation(self): #анимация 
        if self.count + 1 >= 60: #обновление счетчика раз в 60 секунд
            self.count = 0
        if self.side == 'right': #анимация движения вправо
            self.image = transform.scale(enemyanimright[self.count // 12], (self.width, self.height)) #замена изображение по счетчику
            self.count += 1
        elif self.side == 'left': #анимация движения влево
            self.image = transform.scale(enemyanimleft[self.count // 12], (self.width, self.height)) #замена изображение по счетчику
            self.count += 1

    def flip(self): #разворот объекта (зеркальное отражение)
        self.image = transform.flip(self.image, True, False)

'=================================двигающаяся платформа================================='
class Movingplatform(sprite.Sprite):
    side = 'left' #сторона движения
    def __init__(self, width, height, x, y, max_right_position, max_left_position, speed, **args):
        sprite.Sprite.__init__(self)
        self.image = transform.scale(image.load("movingplatform.png"), (width, height))
        self.rect = Rect(x, y, width, height)
        self.speed = speed #скорость
        self.max_left_position = max_left_position #максимальная позиция слева
        self.max_right_position = max_right_position #максимальная позиция справа
        self.x = x 
        self.y = y
        self.width = width
        self.height = height
        self.add(movingplatforms, entities) #добавление в группы спрайтов

    def update(self): #передвижение
        if self.rect.x <= self.max_left_position: #сторона меняется, если достигается заданное значение координат влево
            self.side = 'right'
        if self.rect.x >= self.max_right_position: #сторона меняется, если достигается заданное значение координат вправо
            self.side = 'left'
        if self.side == 'left':
            self.rect.x -= self.speed
        else:
            self.rect.x += self.speed     
        self.collide()

    def collide(self): #столкновение с игроком  
        if sprite.collide_rect(self, hero):  
            #hero.lose = True
            if hero.xvel > 0 and self.side == 'left':                      # если движется вправо
                hero.rect.right = self.rect.left                           # то сталкивается о границу
                #self.lose = True
            if hero.xvel < 0 and self.side == 'right':                      # если движется влево
                hero.rect.left = self.rect.right                            # то не движется влево                          
                #self.lose = True
            if hero.xvel == 0:
                if self.side == 'left':
                    hero.rect.right = self.rect.left
                if self.side == 'right':
                    hero.rect.left = self.rect.right

'=================================игрок================================='


class Player(sprite.Sprite):
    def __init__(self, x, y, width, height):
        sprite.Sprite.__init__(self)
        self.xvel = 0   #скорость перемещения. 0 - стоять на месте
        self.startX = x # Начальная позиция x
        self.startY = y # Начальная позиция y
        self.yvel = 0 # скорость вертикального перемещения
        self.onGround = False #на земле или нет?
        self.image = transform.scale(image.load("0.png"), (width, height))
        self.rect = Rect(x, y, width, height) 
        self.lose = False #поражение
        self.win = False #победа
        self.count = 0 #счетчик анимации 
        self.COINSCOUNTER = 0 #счетчик монет
        self.STARSCOUNTER = 0 #счетчик звезд
    

    def update(self, left, right, up, platforms): #передвижение
        
        if up: #если прыжок
            if self.onGround: # прыгаем, только когда можем оттолкнуться от земли
                self.yvel = -JUMP_POWER #прыжок
                JUMP.play() #проигрывание звука прыжка
        if left: #если влево
            self.xvel = -MOVE_SPEED #движение влево
            if self.onGround: #если на земле
                STEP.play()  #проигрывание звука шага
        if right: #если вправо
            self.xvel = MOVE_SPEED #движение вправо
            if self.onGround: #если на земле
                STEP.play() #проигрывание звука шага
        if not(left or right): # стоим, когда нет указаний идти
            self.count = 0 #обнуление счетчика
            self.xvel = 0 #скорость = 0
            if not up:
                pass
        if not self.onGround: #если не на земле - падаем
            self.yvel +=  GRAVITY
            
        self.onGround = False; 
        self.rect.y += self.yvel #переносим свои положение на уvel
        self.collide(0, self.yvel, platforms) #фукнция столкновение

        self.rect.x += self.xvel #переносим свои положение на xvel
        self.collide(self.xvel, 0, platforms) #фукнция столкновение
        self.animation() #фукнция анимации
    

    def animation(self): #анимация
        if self.count + 1 >= 60: #обнуление счетчика раз в 60 секунд
            self.count = 0
        if left: #если движение влево
            self.image = walk_left[self.count // 12] #отрисовка анимации по счетчику
            self.count += 1
        elif right: #если движение влево
            self.image = walk_right[self.count // 12] #отрисовка анимации по счетчику
            self.count += 1
        else:
            self.image = stay[0] #если стоим, отрисовка положения бездействия
    
    
    def collide(self, xvel, yvel, platforms): #столкновение
        for p in platforms: #с блоками
            if sprite.collide_rect(self, p): # если есть пересечение блока с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то не движется вправо

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то не движется влево

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # становится на объект
                    self.yvel = 0                 # энергия прыжка пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # энергия прыжка пропадает

        for p in movingobjects: #с передвигаемым объектом
            if sprite.collide_rect(self, p): # если есть пересечение объекта с игроком

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то сталкивается о границу
                    p.rect.x += 2.5               #перемещение объекта

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то движется влево
                    p.rect.x -= 2.5               # перемещение объекта
            
                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # становится на объект
                    self.yvel = 0                 # энергия падения пропадает     

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # энергия прыжка пропадает
        
        for p in enemies: #с врагами
            if sprite.collide_rect(self, p): # если есть пересечение объекта с игроком

                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # становится на объект
                    self.yvel = 0                 # энергия падения пропадает  
                    DIE.play()                    # проигрывание звука смерти 
                    p.kill()                      # удаление объекта 

                if xvel > 0:                      # движется вправо - игрок проигрывает
                    self.lose = True                   

                if xvel < 0:                      # движется влево - игрок проигрывает
                    self.lose = True
                
        for p in Doingobjects: # с объектом взаимодействия 
            if sprite.collide_rect(self, p): # если есть пересечение объекта с игроком
                for block in LockedPlatforms:
                    if block.locked:
                        OPEN.play()                       # проигрывание звука открытия 
                        p.image = transform.scale(image.load("activeobject.png"), (Doingobject_PLATFORM_WIDTH, Doingobject_PLATFORM_HEIGHT)) # изменение изображения
                        for ob in LockedPlatforms:        
                            ob.kill()                     # уборка закрытых объектов
                            ob.locked = False             # разблокирован
                
        for p in movingplatforms: # с движующейся платформой 
            if sprite.collide_rect(self, p):      # если есть пересечение платформы с игроком  
                
                if yvel > 0:                      # если падает вниз
                    self.rect.bottom = p.rect.top # то не падает вниз
                    self.onGround = True          # становится на объект
                    self.yvel = 0                 # энергия падения пропадает

                if yvel < 0:                      # если движется вверх
                    self.rect.top = p.rect.bottom # то не движется вверх
                    self.yvel = 0                 # энергия прыжка пропадает     

                if xvel > 0:                      # если движется вправо
                    self.rect.right = p.rect.left # то сталкивается о границу
                    #self.lose = True

                if xvel < 0:                      # если движется влево
                    self.rect.left = p.rect.right # то движется влево
                    #self.lose = True

               

        for p in dangerplatforms:  # с опасным блоком 
            if sprite.collide_rect(self, p): # если есть пересечение - игрок проигрывает
                self.lose = True 

        for p in EndingObjects: #с конечным объектом 
            if sprite.collide_rect(self, p): # если есть пересечение - игрок выигрывает
                self.win = True

        for p in LockedPlatforms: #с заблокированным блоком 
            if p.locked: # если заблокирован
                if sprite.collide_rect(self, p): # если есть пересечение блока с игроком
                    if xvel > 0:                      # если движется вправо
                        self.rect.right = p.rect.left # то не движется вправо
                    if xvel < 0:                      # если движется влево
                        self.rect.left = p.rect.right # то не движется влево
                    if yvel > 0:                      # если падает вниз
                        self.rect.bottom = p.rect.top # то не падает вниз   
                        self.onGround = True          # становится на что-то твердое
                        self.yvel = 0                 # энергия падения пропадает
                    if yvel < 0:                      # если движется вверх
                        self.rect.top = p.rect.bottom # то не движется вверх
                        self.yvel = 0                 # энергия прыжка пропадает

        for p in Coins: #c монетами
            if sprite.collide_rect(self, p): # если есть пересечение объекта с игроком
                p.kill() #удаление объекта
                COIN.play() #проигрывание звука
                self.COINSCOUNTER += 1 #прибавление к счетчику
        for p in Stars: #со звездами
            if sprite.collide_rect(self, p): # если есть пересечение объекта с игроком
                BONUS.play() #проигровка звука звезды
                p.kill() #удаление объекта
                self.STARSCOUNTER += 1 #прибавление к счетчику
              
'=================================камера================================='

class Camera(object):
    def __init__(self, camera_func, width, height):
        self.camera_func = camera_func
        self.state = Rect(0, 0, width, height)

    def apply(self, target):
        return target.rect.move(self.state.topleft)
        
    def update(self, target):
        time.delay(1)
        self.state = self.camera_func(self.state, target.rect)
        
'=================================движение камеры================================='

def camera_configure(camera, target_rect):
    l, t, _, _ = target_rect
    _, _, w, h = camera
    l, t = -l+WIN_WIDTH / 2, -t+WIN_HEIGHT / 2

    l = min(0, l)                           # Не движемся дальше левой границы
    l = max(-(camera.width-WIN_WIDTH), l)   # Не движемся дальше правой границы

    t = max(-(camera.height-WIN_HEIGHT), t) # Не движемся дальше нижней границы
    t = min(0, t)                           # Не движемся дальше верхней границы
    
    return Rect(l, t, w, h)      

'=================================начальный показ текста================================='
def show_text(text, seconds, color):
    temp_color = [0,0,0]
    screen.fill(C_BLACK)
    display.update()
    for ap in range(int(seconds * 60 / 4)):
        if temp_color[0] < color[0]:
            temp_color[0] += int(color[0] / (seconds * 60 / 4))
        if temp_color[1] < color[1]:
            temp_color[1] += int(color[1] / (seconds * 60 / 4))
        if temp_color[2] < color[2]:
            temp_color[2] += int(color[2] / (seconds * 60 / 4))
        rtext = font.Font("pixelfont.ttf", 120).render(text, True, temp_color, C_BLACK)
        screen.blit(rtext, (WIN_WIDTH / 2 - rtext.get_width() / 2, WIN_HEIGHT / 2 - rtext.get_height() / 2))
        display.update()
        timer.tick(60)
    for kek in range(int(60 * seconds / 2)):
        rtext = font.Font("pixelfont.ttf", 120).render(text, True, C_WHITE, C_BLACK)
        screen.blit(rtext, (WIN_WIDTH / 2 - rtext.get_width() / 2, WIN_HEIGHT / 2 - rtext.get_height() / 2))
        display.update()
        timer.tick(60)
    for ap in range(int(seconds * 60 / 4)):
        if temp_color[0] > 0:
            temp_color[0] -= int(color[0] / (seconds * 60 / 4))
        if temp_color[1] > 0:
            temp_color[1] -= int(color[1] / (seconds * 60 / 4))
        if temp_color[2] > 0:
            temp_color[2] -= int(color[2] / (seconds * 60 / 4))
        rtext = font.Font("pixelfont.ttf", 120).render(text, True, temp_color, C_BLACK)
        screen.blit(rtext, (WIN_WIDTH / 2 - rtext.get_width() / 2, WIN_HEIGHT / 2 - rtext.get_height() / 2))
        display.update()
        timer.tick(60)
    mixer.music.play(-1, vol) #воспроизведение музыки

'=================================конечный объект================================='
def create_all():
    enemy1 = Enemy(40, 60, 1950, 835, 1950, 1250, 2)  #width, height, x, y, max_right_position, max_left_position, speed
    enemy2 = Enemy(40, 60, 2250, 835, 2650, 2050, 2)
    enemy3 = Enemy(30, 40, 5400, 472, 5400, 5100, 1)
    movingplatform1 = Movingplatform(100, 50, 5700, 800, 6150, 5700, 3)  #width, height, x, y, max_right_position, max_left_position, speed
    movingplatform2 = Movingplatform(100, 50, 6400, 800, 6820, 6400, 3) 
    ending = EndingObject(7400, 760, 8, 70) #x, y, width, height        

'=================================создание HUD================================='

def make_frame(): 
    #time.delay(1)
    global positionx, positiony, starimage, displaystar, counterfont
    positionx = WIN_WIDTH - 160 
    positiony = WIN_HEIGHT - 630

    #счетчик монет
    if hero.COINSCOUNTER >= 10: #условие смены координатов надписи для гармоничного расположения
        positionx = WIN_WIDTH - 205
    counterfont = font.Font('pixelfont.ttf', 70) #подключение шрифта
    screen.blit(counterfont.render(str(hero.COINSCOUNTER), 1, (255, 255, 255)), (positionx, positiony)) #текст самого счетчика
    screen.blit(counterfont.render('x', 1, (255, 255, 255)), (WIN_WIDTH - 118, positiony - 7)) # текст х
    screen.blit(transform.scale(image.load("coinhud.png"), (100, 100)), (WIN_WIDTH - 92, positiony - 10))  #отображение монеты рядом

    #счетчик звезд
    starimage = "0_3_stars.png"
    displaystar = transform.scale(image.load("0_3_stars.png"), (210, 70)) #изображение по дефолту, когда собрано 0/3 звезд
    if hero.STARSCOUNTER == 1: #когда собрано 1/3 звезд
        displaystar = transform.scale(image.load("1_3_stars.png"), (210, 70)) 
        starimage = "1_3_stars.png"
    if hero.STARSCOUNTER == 2: #когда собрано 2/3 звезд
        displaystar = transform.scale(image.load("2_3_stars.png"), (210, 70))
        starimage = "2_3_stars.png"
    if hero.STARSCOUNTER == 3: #когда собрано 3/3 звезд
        displaystar = transform.scale(image.load("3_3_stars.png"), (210, 70))
        starimage = "3_3_stars.png"
    
    screen.blit(displaystar, (WIN_WIDTH - 1200, positiony + 5)) #отображение 
    
    
'-----------------------------------------------------------------------------создание объектов----------------------------------------------------------------------------------------------------------------------------------------------------------'

'=================================окно================================='


screen = display.set_mode(DISPLAY)
display.set_caption("Super_Ultra_YuriuGigachad_Run_Play_2077_2D_4K_ULTRAHD") #шапка
bg = transform.scale(image.load('back.jpg'), (WIN_WIDTH,WIN_HEIGHT)) #фон

'=================================спрайты и переменные для них================================='
hero = Player(100, 800, 22, 32) # x,y,width,height
moveobject = Movingblock(600,790,105,105)

left = right = False # по умолчанию - стоим
up = False
    
'=================================группы спрайтов и добавление в них объектов================================='
entities = sprite.Group() # Все объекты
platforms = [] #блоки
parcourplatforms = [] #платформы
LockedPlatforms = [] #заблокированные блоки
movingobjects = sprite.Group() #передвигающийся блок
movingobjects.add(moveobject) 
Stars = sprite.Group() #звезды
Coins = sprite.Group() #монеты
dangerplatforms = sprite.Group() #опасные блоки
movingplatforms = sprite.Group() #двигающиеся платформы
Doingobjects = sprite.Group() #объекты взаимодействия
EndingObjects = sprite.Group() #заканчивающиеся оъекты
entities.add(hero)    
entities.add(moveobject)    
enemies = sprite.Group()
create_all()

'=================================уровень и его создание================================='
level = [
       "----------------------------------------------------------------------------------------------------------------------------------------------------------------------------                                                           ",
       "---------------------------------------------)                                                                                                       -----------------------                                                           ",     
       "--------------------------------------------)                                                                                                      s -----------------------                                                           ",
       "----------------------------------------)                      c                                                               c                     -----------------------                                                          -",
       "------------------------------------)                         ---      c                                                      ---                  -------------------------                                                          -",
       "--------------------------------)                                     ---                                       c                            c       -----------------------                                                          -",
       "--------------------------)                             c                       c              c               ---                   c      ---      -----------------------                                                          -",
       "-------------------)                                   ---                     ---            ---        c               cccc       ---              -----------------------)                                                         -",
       "----------------)                                                                                       ---             ------               c       -----------------------)                                                         -", 
       "---------------)                                                                           c                                                ---      -----------------------                                                          -",
       "-------------)                                               c                            ---                                                        ---)                                                                             -",
       "-----------)                                                ---                      c                                                               --)                                                                              -",
       "---------)                                             c                            ---              c                                              c--                                                                               -",
       "-------)                                              ---                                           ---                                             <--                                                                               -",
       "------)                                                                                                                                              --          c  c  c                                                             (-",
       "-----)                                               ********************************************************                                        --                                                                              (-",
       "-)                                      c -----------------------------------------------------------------------                                    --c      -------------)                                                         (-",
       "-)                                    c ------------------------------------------------------------------------                                    c-->      -------------)                                                         (-",
       "-)                                 c --------------------------------------------------------------------------                                     <--       -------------)                                                         (-",
       "-)                               c---------------------------------------------------------------------------                                        --      c-------------)                                                         (-",
       "-)                               ----------------------------------------------------                                                                --      <-------------)                                                         (-",
       "-)                              ---------                                                                                                            --       -------------)                                                         (-",
       "-)              c               ------                                                      c   c   c   c   c   c                                   c--c      -------------)                                                         (-",
       "-)              -               ----s                                                                                                               <-->      -------------)                                                         (-",
       "-)            c--               ----                                                                                  c c c c c c c c c              ==      c-------------)                                                           ",
       "-)            ---               ----                                                                                ----------------------           ==      <-------------)                         s                     c   c   c   ",
       "-)          c----               ----                                                      -   -   -   -   -   -   --------------------------  c  c c ==   c   -------------------                                        --------------",
       "-)          -----               ---- +                                                -***-***-***-***-***-***-***---------------------------------------------------------------*******************---******************--------------",
       "---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------"]
       
x=y=0 #координаты
for row in level: #вся строка
    for col in row: #каждый символ
        if col == "-": #создание блока
            pf = Platform(x,y)
            entities.add(pf)
            platforms.append(pf)
        if col == '*': #создание опасного блока
            pf = DangerPlatform(x,y)
            entities.add(pf)
            dangerplatforms.add(pf)
        if col == '(':
            pf = DangerPlatformright(x,y)
            entities.add(pf)
            dangerplatforms.add(pf)
        if col == ')':
            pf = DangerPlatformleft(x,y)
            entities.add(pf)
            dangerplatforms.add(pf)
        if col == '+': #создание объекта взаимодействия
            pf = Doingobject(x,y)
            entities.add(pf)
            Doingobjects.add(pf)
        if col == '<': #создание правой платформы
            pf = ParkourPlatformLeft(x-5,y, 'right')
            entities.add(pf)
            platforms.append(pf) 
        if col == '>': #создание левой платформы
            pf = ParkourPlatformRight(x,y, 'left')
            entities.add(pf)
            platforms.append(pf)
        if col == '=': #создание заблокированного блока
            pf = LockedPlatform(x,y)
            entities.add(pf)
            LockedPlatforms.append(pf)
        if col == 'c': #создание монеты
            pf = Coin(x,y)
            entities.add(pf)
            Coins.add(pf)
        if col == 's': #создание звезды
            pf = Star(x,y)
            entities.add(pf)
            Stars.add(pf)
        
        x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
    y += PLATFORM_HEIGHT    #то же самое и с высотой
    x = 0                   #на каждой новой строчке начинаем с нуля
    
total_level_width  = len(level[0])*PLATFORM_WIDTH # Высчитываем фактическую ширину уровня
total_level_height = len(level)*PLATFORM_HEIGHT   # высоту
camera = Camera(camera_configure, total_level_width, total_level_height) 

pause = False
finished = False
game = True

timer = time.Clock()
optimizetimer = time.Clock()
show_text("Level 1", 2, C_WHITE)


def render():
    global game, pause, finished, moveobject, hero, left, right, up
    while game: # Основной цикл программы
        timer.tick(60)  
        for e in event.get(): # Обрабатываем события
            if e.type == QUIT:
                game = False
            elif e.type == KEYDOWN:
                if e.key == K_q: #закрытие программы
                    game = False
                if e.key == K_r and finished: #перезагрузка игры
                    for item in entities:
                        item.kill()
                    x=y=0 # координаты
                    #создание уровня заного
                    for row in level: # вся строка 
                        for col in row: # каждый символ
                            if col == "-":
                                pf = Platform(x,y)
                                entities.add(pf)
                                platforms.append(pf)
                            if col == '*':
                                pf = DangerPlatform(x,y)
                                entities.add(pf)
                                dangerplatforms.add(pf)
                            if col == '(':
                                pf = DangerPlatformright(x,y)
                                entities.add(pf)
                                dangerplatforms.add(pf)
                            if col == ')':
                                pf = DangerPlatformleft(x,y)
                                entities.add(pf)
                                dangerplatforms.add(pf)
                            if col == '+':
                                pf = Doingobject(x,y)
                                entities.add(pf)
                                Doingobjects.add(pf)
                            if col == '<':
                                pf = ParkourPlatformLeft(x-5,y, 'right')
                                entities.add(pf)
                                platforms.append(pf)
                            if col == '>':
                                pf = ParkourPlatformRight(x,y, 'left')
                                entities.add(pf)
                                platforms.append(pf)
                            if col == '=':
                                pf = LockedPlatform(x,y)
                                entities.add(pf)
                                LockedPlatforms.append(pf)
                            if col == 'c':
                                pf = Coin(x,y)
                                entities.add(pf)
                                Coins.add(pf)
                            if col == 's':
                                pf = Star(x,y)
                                entities.add(pf)
                                Stars.add(pf)
                                
                            x += PLATFORM_WIDTH #блоки платформы ставятся на ширине блоков
                        y += PLATFORM_HEIGHT    #то же самое и с высотой
                        x = 0                   #на каждой новой строчке начинаем с нуля
                    create_all()
                    moveobject = Movingblock(600,790,105,105)
                    hero = Player(100, 800, 22, 32) # x,y,width,height
                    movingobjects.add(moveobject)
                    entities.add(moveobject)
                    entities.add(hero)
                    mixer.music.play(-1, vol) #воспроизведение музыки
                    finished = False

                if e.key == K_ESCAPE and not finished: #пауза
                    if pause:
                        mixer.music.unpause() #распауза музыки
                        pause = False
                    elif not pause:
                        mixer.music.pause()
                        pause = True
                        screen.fill(C_BLACK)
                        screen.blit(pause_text, (WIN_WIDTH / 2 - pause_text.get_width() / 2 , WIN_HEIGHT / 2 - pause_text.get_height() / 2))
                        display.update()
            
            #передвижение на клавиши
            if e.type == KEYDOWN and e.key == K_w:
                up = True
            if e.type == KEYDOWN and e.key == K_a:
                left = True
            if e.type == KEYDOWN and e.key == K_d:
                right = True

            if e.type == KEYUP and e.key == K_w:
                up = False
            if e.type == KEYUP and e.key == K_d:
                right = False
            if e.type == KEYUP and e.key == K_a:
                left = False

        if not pause and not finished: 
            movingplatforms.update()
            #time.delay(1)
            enemies.update()
            #time.delay(1)
            moveobject.collide(platforms)
            #time.delay(1)
            camera.update(hero) # центризируем камеру относительно персонажа
            #time.delay(1)
            hero.update(left, right, up, platforms) # передвижение
            #time.delay(2)
            screen.blit(bg, (0,0))      # Каждую итерацию необходимо всё перерисовывать 
            #time.delay(1)
            for e in entities:# отображение
                screen.blit(e.image, camera.apply(e))
            
            make_frame()
            if hero.win: #победа
                WIN.play()
                mixer.music.pause()
                finished = True
                screen.fill(C_BLACK) #заполнение черным цветом
                displaystar = transform.scale(image.load(starimage), (400, 120)) #изображение звезды
                screen.blit(displaystar,  (WIN_WIDTH / 2 - displaystar.get_width() / 2, 50))  #прорисовка звезды
                screen.blit(win, (WIN_WIDTH / 2 - win.get_width() / 2, 250)) #прорисовка надписи победы 
                screen.blit(restart_text, (WIN_WIDTH / 2 - restart_text.get_width() / 2, 350)) #прорисовка надписи рестарта

                screen.blit(counterfont.render(str(hero.COINSCOUNTER), 1, (255, 255, 255)), (positionx, positiony)) #текст самого счетчика
                screen.blit(counterfont.render('x', 1, (255, 255, 255)), (WIN_WIDTH - 118, positiony - 7)) # текст х
                screen.blit(transform.scale(image.load("coin.png"), (100, 100)), (WIN_WIDTH - 92, positiony - 10))  #отображение монеты рядом
            if hero.lose: #поражение
                
                DIE.play()
                mixer.music.pause()
                finished = True        
                screen.fill(C_BLACK)
                screen.blit(game_over, (WIN_WIDTH / 2 - game_over.get_width() / 2, 250))
                screen.blit(restart_text, (WIN_WIDTH / 2 - restart_text.get_width() / 2, 350))
                screen.blit(counterfont.render(str(hero.COINSCOUNTER), 1, (255, 255, 255)), (positionx, positiony)) #текст самого счетчика
                screen.blit(counterfont.render('x', 1, (255, 255, 255)), (WIN_WIDTH - 118, positiony - 7)) # текст х
                screen.blit(transform.scale(image.load("coin.png"), (100, 100)), (WIN_WIDTH - 92, positiony - 10))  #отображение монеты рядом
        time.delay(1)
        display.update()     # обновление и вывод всех изменений на экран
    

render()
