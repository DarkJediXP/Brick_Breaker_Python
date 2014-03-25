import spyral
import random
import math

WIDTH = 1200
HEIGHT = 800
BG_COLOR = (0,0,0)
WHITE = (255, 255, 255)
SIZE = (WIDTH, HEIGHT)

class Ball(spyral.Sprite):
    def __init__(self, scene):
        super(Ball, self).__init__(scene)
        self.image = spyral.Image(size=(20, 20))
        self.image.draw_circle(WHITE, (10, 10), 10)
        
        spyral.event.register("pong_score", self._reset)
        spyral.event.register("director.update", self.update)
        self._reset()
        
    def _reset(self):
        theta = random.random()*2*math.pi
        while ((theta > math.pi/4 and theta < 3*math.pi/4) or
               (theta > 5*math.pi/4 and theta < 7*math.pi/4)):
            theta = random.random()*2*math.pi
        r = 300
        
       # self.vel_x = r * math.cos(theta)
        #self.vel_y = r * math.sin(theta)
        self.vel_x = r * math.cos(1)
        self.vel_y = r * math.sin(math.pi + .4) - 100
        self.anchor = 'center'
        self.pos = (WIDTH/2, HEIGHT/2)
                
    def update(self, delta):
        self.x += delta * self.vel_x
        self.y += delta * self.vel_y
        
        r = self.rect #id itself as rectangle
        if r.top < 0:
            self.vel_y = -self.vel_y      
        # r.top = 0
        # self.vel_y = -self.vel_y
        #  spyral.event.handle("pong_score", spyral.Event(side='left'))
        #if r.bottom > HEIGHT:
          
        # r.bottom = HEIGHT
        # self.vel_y = -self.vel_y
        # spyral.event.handle("pong_score", spyral.Event(side='left'))
        
        if r.left < 0:
            #spyral.event.handle("pong_score", spyral.Event(side='left'))
            print self.vel_x
            print self.vel_y
            self.vel_x = -self.vel_x
          #  if(self.vel_x > 0 ):
           #     self.vel_y = -self.vel_y
        if r.right > WIDTH:
            #spyral.event.handle("pong_score", spyral.Event(side='right'))
            self.vel_x = -self.vel_x
            #if(self.vel_x > 0 ):
             #   self.vel_y = -self.vel_y
            
    def collide_paddle(self, paddle):
        if self.collide_sprite(paddle):
            #self.vel_x = -self.vel_x
            self.vel_y = -self.vel_y
    def collide_brick(self, brick):
        if self.collide_sprite(brick):
           # brick.removeMe()
            if(brick.visible != False):
                self.vel_x = -self.vel_x
                self.vel_y = -self.vel_y
                brick.visible = False;
                
           

class Paddle(spyral.Sprite):
    def __init__(self, scene):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(100, 20)).fill((255, 255, 255))
        self.x = WIDTH/2
        self.y = HEIGHT - 200
#        if side == 'left':
 #           self.anchor = 'midleft'
 #           self.x = 20
  #          self.y = HEIGHT - (HEIGHT - 20)
 #       else:
 #           self.anchor = 'midright'
 #           self.x = WIDTH - 20
 #           self.y = HEIGHT - 20
#        self.side = side
        self.moving = False
      
        left = "left"
        right="right"
      
        spyral.event.register("input.keyboard.down."+left, self.move_left)
        spyral.event.register("input.keyboard.down."+right, self.move_right)
        spyral.event.register("input.keyboard.up."+left, self.stop_move)
        spyral.event.register("input.keyboard.up."+right, self.stop_move)
        spyral.event.register("director.update", self.update)
    
    #    spyral.event.register("pong_score", self._reset)
        
    def move_left(self):
        self.moving = 'left'
    def move_right(self):
        self.moving = 'right'
    def stop_move(self):
        self.moving = False
    def _reset(self): # New might want to change this
        self.y = HEIGHT/2
        
    def update(self, delta):
        paddle_velocity = 250
        
        if self.moving == 'left':
            self.x -= paddle_velocity * delta
        elif self.moving == 'right':
            self.x += paddle_velocity * delta
                
        r = self.rect
        if r.top < 0:
            r.top = 0
        if r.bottom > HEIGHT:
            r.bottom = HEIGHT
            
        #self.pos == getattr(r, self.anchor)
    
# New 
class basicBrick(spyral.Sprite):
    def __init__(self, scene, pos_x, pos_y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(300, 20)).fill((100, 200, 100))
        #if side == 'left':
        #    self.anchor = 'midleft'
       #     self.x = 20
        #    self.y = HEIGHT - (HEIGHT - 20)
       # else:
      #      self.anchor = 'midright'
       #     self.x = WIDTH - 20
        #    self.y = HEIGHT - 20
       # self.side = side
        self.x = pos_x
        self.y = pos_y
        self.moving = False
    def removeMe(self):
        self.kill()

class normalBrick(spyral.Sprite):
    def __init__(self, scene, pos_x, pos_y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(300, 20)).fill((125, 200, 255))
        #if side == 'left':
        #    self.anchor = 'midleft'
       #     self.x = 20
        #    self.y = HEIGHT - (HEIGHT - 20)
       # else:
      #      self.anchor = 'midright'
       #     self.x = WIDTH - 20
        #    self.y = HEIGHT - 20
       # self.side = side
        self.x = pos_x
        self.y = pos_y
        self.moving = False

class superBrick(spyral.Sprite):
    def __init__(self, scene, pos_x, pos_y):
        spyral.Sprite.__init__(self, scene)
        self.image = spyral.Image(size=(300, 20)).fill((200, 100, 100))
        #if side == 'left':
        #    self.anchor = 'midleft'
       #     self.x = 20
        #    self.y = HEIGHT - (HEIGHT - 20)
       # else:
      #      self.anchor = 'midright'
       #     self.x = WIDTH - 20
        #    self.y = HEIGHT - 20
       # self.side = side
        self.x = pos_x
        self.y = pos_y
        self.moving = False


class Pong(spyral.Scene):
    def __init__(self, *args, **kwargs):
        global manager
        spyral.Scene.__init__(self, SIZE)
        self.background = spyral.Image(size=SIZE).fill(BG_COLOR)
        
        self.ball = Ball(self)
        self.paddle = Paddle(self)
     
        # Bricks that player has to break 
        #Row 1
        self.brick_TopRight = superBrick(self, WIDTH - 450, HEIGHT - (HEIGHT - 20))
        self.brick_TopMid = superBrick(self, WIDTH - 760, HEIGHT - (HEIGHT - 20))
        self.brick_TopLeft = superBrick(self, WIDTH - 1070, HEIGHT - (HEIGHT - 20))

        #Row 2
        self.brick_MidRight = normalBrick(self, WIDTH - 450, HEIGHT - (HEIGHT - 45))
        self.brick_MidMid= normalBrick(self, WIDTH - 760, HEIGHT - (HEIGHT - 45))
        self.brick_MidLeft = normalBrick(self, WIDTH - 1070, HEIGHT - (HEIGHT - 45))

        #Row 3
        self.brick_BotRight = basicBrick(self, WIDTH - 450, HEIGHT - (HEIGHT - 70))
        self.brick_BotMid = basicBrick(self, WIDTH - 760, HEIGHT - (HEIGHT - 70))
        self.brick_BotLeft = basicBrick(self, WIDTH - 1070, HEIGHT - (HEIGHT - 70))
        
        spyral.event.register("system.quit", spyral.director.pop)
        spyral.event.register("director.update", self.update)
        spyral.event.register("input.keyboard.down.q", spyral.director.pop)
        
    def update(self, delta):
       
        self.ball.collide_brick(self.brick_BotLeft)
        self.ball.collide_brick(self.brick_BotMid)
        self.ball.collide_brick(self.brick_BotRight)
        self.ball.collide_brick(self.brick_MidLeft)
        self.ball.collide_brick(self.brick_MidMid)
        self.ball.collide_brick(self.brick_MidRight)
        self.ball.collide_brick(self.brick_TopLeft)
        self.ball.collide_brick(self.brick_TopMid)
        self.ball.collide_brick(self.brick_TopRight)
        self.ball.collide_paddle(self.paddle)
       # self.ball.collide_paddle(self.right_paddle)
    
