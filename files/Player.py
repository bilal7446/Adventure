import pygame
import random
from pygame import *

class Player(Entity):
    def __init__(self, game):
        Entity.__init__(self)
        #Add Player to Game
        self.icounter=0 #invincible counter
        self.game = game
        self.game.playerentity.add(self)
        #Set Player Velocities
        self.xvel = 0
        self.yvel = 0
        #Set Player Offsets
        self.xoffset = -128
        self.yoffset = 0
        #cooldown
        self.longjumpcooldown=0
        self.m24cooldown=0

        #Counters
        self.walkcounter = 0
        self.standcounter = 0
        self.attackcounter = 0
        self.takedamagecounter = 0
        self.dancecounter=0
        self.d=pygame.mixer.Sound('Media/Music/bts.ogg')
        self.counter=0
        #States
        #abilities
        self.longjump=False
        self.m24=False
        self.dance=False




        self.collideright = False
        self.onGround = True
        self.airborne = False
        self.faceright = True
        self.takingdamage = False
        self.attacking = False
        self.moving = False
        #Create Player Sprite
        self.image = Surface((300, 150),pygame.SRCALPHA)
        self.rect = Rect(0, 0, 300, 150)
        #Create Player Detectable Area
        self.detectable = pygame.sprite.Sprite()
        self.detectable.rect = Rect(0, 0, 80, 90)
        self.detectable.image = Surface((80,90))
        self.detectable.image.fill(Color("#0033FF"))
        self.detectable.image.set_alpha(150)
        self.detectable.image.convert_alpha()
        self.game.detectablegroup.add(self.detectable)
        #Life Meter
        self.lifetotal = ["", "l", "ll", "lll", "llll", "lllll", "llllll", "lllllll", "llllllll", "lllllllll"]
        self.currentlifetotal = 9
        #Inputs
        self.up = False
        self.down = False
        self.right = False
        self.left = False
        self.space = False       
    def startingposition(self,x,y):
        self.rect = Rect(x, y, 300, 150)
        self.detectable.rect = Rect(x, y, 80, 90)

    def inputhandler(self):
        
            for e in pygame.event.get():
                if not inconvo:
                
                    if e.type == QUIT: raise SystemExit("QUIT")
                    if e.type == KEYDOWN and e.key == K_ESCAPE:
                        raise SystemExit("ESCAPE")
                    if e.type == KEYDOWN and e.key == K_UP and not self.dance:
                        self.up = True
                    if e.type == KEYDOWN and e.key == K_DOWN :
                        self.down = True
                    if e.type == KEYDOWN and e.key == K_LEFT and not self.dance:
                        self.left = True
                    if e.type == KEYDOWN and e.key == K_RIGHT and not self.dance:
                        self.right = True
                    if e.type == KEYDOWN and e.key == K_SPACE and not self.dance:
                        self.space = True
                        changemusic('bullet',False)
                    if e.type == KEYDOWN and e.key == K_b  and havehappy:
                        self.longjump=True
                        self.up=True
                    if e.type == KEYDOWN and e.key == K_m  and m24:
                        
                        self.m24=True
                    if e.type == KEYDOWN and e.key == K_d:
                        
                        self.dance=True

                    if e.type == KEYDOWN and e.key == K_RETURN:
                        self.game.pausemenu.createpausemenu()
                        self.game.screenfocus = "Pause Menu"
                if e.type == KEYUP and e.key == K_SPACE:
                    self.space = False    
                if e.type == KEYUP and e.key == K_UP:
                    self.up = False

                if e.type == KEYUP and e.key == K_b and havehappy:
                        self.longjump=False 
                        self.up=False
                if e.type == KEYUP and e.key == K_d:
                        
                        self.dance=False
                        self.dancecounter=0
                        self.d.stop()
                if e.type == KEYUP and e.key == K_m and m24:
                    self.m24=False
                if e.type == KEYUP and e.key == K_DOWN:
                    self.down = False
                    self.dancecounter=0
                if e.type == KEYUP and e.key == K_RIGHT:
                    self.right = False
                    self.counter = 0
                if e.type == KEYUP and e.key == K_LEFT:
                    self.left = False
                    self.counter = 0

    def update(self):
        #cooldown counter
        if havehappy:
            self.longjumpcooldown+=1
        if self.longjumpcooldown>=400:
            self.longjumpcooldown=400
        if m24:
            self.m24cooldown+=1
            if self.m24cooldown>=400:
                self.m24cooldown=400

          
        
                

        self.inputhandler()
        
        #Apply Inputs

        if self.up:
            if self.onGround:
                if self.longjump:
                     if self.longjumpcooldown>=400:
                            self.yvel=-22.6
                            self.longjumpcooldown=0
                else:
                    self.yvel -= 10.6
            # Only jump if on the ground
        if self.down and self.airborne:
            self.yvel=self.yvel+5.6
            # Does nothing
        if self.left:
            self.faceright = False
            if self.takingdamage == False:
                self.xvel = -8
                self.moving = True
            # Move if not taking damage
        if self.right:
            self.faceright = True
            if self.takingdamage == False:
                self.xvel = 8
                self.moving = True
            # Move if not taking damage
        if self.space:
            projectile = Projectile(self,self.game)
            self.game.projectilegroup.add(projectile)
            self.space = False
            self.attacking = True
            #Create projectile on space
        if self.m24:
            if self.m24cooldown>=300:
                changemusic('m24',False)
                projectile = Projectile(self,self.game,"m24")
                self.game.projectilegroup.add(projectile)
                self.m24 = False
                self.attacking = True


                self.m24cooldown=0
            
            #Create projectile on space
        

        #Apply States 
        if self.yvel < 0: self.airborne = True
            #Player is moving up
        if self.yvel > 1.2: self.airborne = True
            #Player is falling
        if self.onGround == True:
            if self.up == True:
                self.airborne == True
            else:
                self.airborne = False
            #Still airborne while pressing up
        if not self.onGround:
            self.yvel += 0.3
            #Apply gravity
            if self.yvel > 100:
                self.yvel = 100
                #Max falling speed
        if not(self.left or self.right):
            if not self.takingdamage:
                self.moving = False
                self.xvel = 0
            #Stop player if not taking damage
        if self.takingdamage:
            if self.collideright:
                self.xvel = -8
            else:
                self.xvel = 8
            #Move player if taking damage
        if self.attackcounter > 8:
            self.attacking = False
            self.attackcounter = 0
            self.standcounter = 0
            #Stop attacking after 9 updates
        if self.takedamagecounter > 13:
            self.takingdamage = False
            self.takedamagecounter = 0
            #Player stops taking damage after 14 updates
        

        #Increase or Reset Counters
        if self.attacking: self.attackcounter = self.attackcounter + 1
        if self.takingdamage: self.takedamagecounter = self.takedamagecounter + 1
        if not self.moving: self.standcounter = 0

        #Collisions
        self.detectable.rect.left += self.xvel
        self.collide(self.xvel, 0)
        self.detectable.rect.top += self.yvel
        self.onGround = False;
        self.collide(0, self.yvel)

        #Offsets
        
        self.rect.x = self.detectable.rect.x + self.xoffset
        self.rect.y = self.detectable.rect.y + self.yoffset

        if inconvo and not (self.airborne):
            pygame.time.delay(200) # if i dont add not airbornecondotion than when player interacts with convo block while in air than player will feel like laggy in air
            
        #moving to checkpoint
     


        
        #Animate
        self.animate()

    def collide(self, xvel, yvel):
        global invincible,press,convoid,m24,vssstates,havehappy,havezuzu
        global inconvo

        if convoid>=10 and inconvo:
            self.right=False
            self.left=False
            self.up=False
            self.counter = 0
     
        
        if invincible: self.icounter+=1
        if self.icounter>=100:
           
            self.icounter=0
            invincible=False
        #collide with convo block
        for c in self.game.convoblock:
            if pygame.sprite.collide_rect(self.detectable,c):
                if c.chatid==1:
                    if not musicplaying=='pubg':changemusic('pubg',True)
                self.game.projectilegroup.empty()
                self.right=False
                self.left=False
                self.up=False
                self.counter = 0
                inconvo=True   
                press=1
                convoid=c.chatid     
                self.game.convoblock.remove(c)
                
                
                

               
            
                 


        #Collide Platforms
        for p in self.game.platforms:
            if pygame.sprite.collide_rect(self.detectable, p):
                if xvel > 0:
                    self.detectable.rect.right = p.rect.left
                if xvel < 0:
                    self.detectable.rect.left = p.rect.right
                if yvel > 0:
                    self.detectable.rect.bottom = p.rect.top
                    self.onGround = True
                    self.yvel = 0
                if yvel < 0:
                    self.detectable.rect.top = p.rect.bottom

        #Collide Enemies
        for e in self.game.enemygroup:
            if pygame.sprite.collide_rect(self.detectable, e.detectable):
                leftdifference = self.detectable.rect.right - e.detectable.rect.left
                rightdifference = self.detectable.rect.left - e.detectable.rect.right
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                if e.type=="rol":
                    self.currentlifetotal=1

                if not invincible:
                    self.takingdamage = True
                    self.currentlifetotal = self.currentlifetotal - 1
                    changemusic('female'+str(random.randint(1,4))+'',False)
                    invincible=True
                
                if self.currentlifetotal<=0 and vssstates=="can atk" and e.type=="vss":
                    self.game.makecheckpoint(7)
                    self.game.screenfocus="Checkpoint"
                    self.d.stop() #stops music of dance

                    self.kill()
                    return

                elif self.currentlifetotal <= 0 and self.game.checkpoint>0:
                        self.game.screenfocus="Checkpoint"
                        self.d.stop() #stops music of dance
                        
                        

                elif self.game.checkpoint==0 and self.currentlifetotal<=0:
                    self.game.screenfocus = "Game Over"
                    self.d.stop() #stops music of dance
                if e.type=="ghost":
                    self.game.enemygroup.remove(e) #remove ghost after hit


                    #self.game.gameover.creategameover()
                    #self.game.screenfocus = "Game Over"
                    #self.currentlifetotal = 0

        #Collide Items
        for i in self.game.itemgroup:
                if i.type=="zuzu":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        havezuzu=True
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        text("YOU GOT SPIRIT OF zuzu....",0,"red",55)
                        pygame.time.delay(1000)
                elif i.type=="checkpoint":
                    if pygame.sprite.collide_rect(self.detectable,i.detectable):
                            self.currentlifetotal=9
                           
                            self.game.makecheckpoint(i.id)


                elif i.type=="m24":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        m24=True
                        self.m24cooldown=400
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        convoid=13
                        inconvo=True
                elif i.type=="happy":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable) and rolstates=="defeat":
                        havehappy=True
                        self.longjumpcooldown=400
                        i.noimage()
                        self.game.itemgroup.remove(i)
                        convoid=12
                        inconvo=True
                elif i.type=="bd":
                    if pygame.sprite.collide_rect(self.detectable, i.detectable):
                        
                    
                        self.game.itemgroup.remove(i)
                        
                        inconvo=True
                        convoid=11
                     
                    #self.game.levelcomplete.createlevelcomplete()
                    #self.game.screenfocus = "Level Complete"
        #collide projectile
        for e in self.game.projectilegroup:
            if pygame.sprite.collide_rect(self.detectable, e):
                leftdifference = self.detectable.rect.right - e.detectable.rect.left
                rightdifference = self.detectable.rect.left - e.detectable.rect.right
                if self.xvel == 0:
                    if abs(leftdifference) < 10: self.collideright = True
                    if abs(rightdifference) < 10: self.collideright = False
                if not invincible:
                    changemusic('female'+str(random.randint(1,4 ))  +'',False)
                    self.game.projectilegroup.remove(e)
                    self.takingdamage = True
                    self.currentlifetotal = self.currentlifetotal - e.damage
                    invincible=True
                if self.currentlifetotal<=0 and vssstates=="can atk" and e.type=="vss":
                    self.game.makecheckpoint(7)
                    self.game.screenfocus="Checkpoint"
                    vssstates="can dmg"
                    self.kill()
                    return
                           
                    self.game.makecheckpoint(7)
                elif self.currentlifetotal <= 0 and self.game.checkpoint>0:

                    self.game.screenfocus="Checkpoint"
                    self.kill()
                    
                    
                elif self.game.checkpoint==0 and self.currentlifetotal<=0:
                    self.game.screenfocus = "Game Over"

                    #self.game.gameover.creategameover()
                    #self.game.screenfocus = "Game Over"
                    #self.currentlifetotal = 0
        #collide Traps
        for t in self.game.trapgroup:
            if pygame.sprite.collide_rect(self.detectable, t):
                changemusic('yell',False)
                self.game.enemygroup.add(Goomba(self.rect.x+(350*3), 153, -14,"ghost"))
                
                self.game.trapgroup.remove(t)

        #collide msggroup
        for m in self.game.msggroup:
        	if pygame.sprite.collide_rect(self.detectable, m):
        		if m.chatid==1:
        			changemusic('10',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==2:
        			changemusic('20',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==3:
        			changemusic('30',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==4:
        			changemusic('40',False)
        			self.game.msggroup.remove(m)
        		elif m.chatid==5:
        			changemusic('5',False)
        			self.game.msggroup.remove(m)


        #Collide Exits
        for x in self.game.exitgroup:
            if pygame.sprite.collide_rect(self.detectable, x):
                if x.roomid==13:
                    if vssstates=="defeat":
                        self.yvel=0
                        self.xvel=0
                        x.changeroom()
                elif x.roomid==19:
                    if cockroachstates=="defeat":
                        self.yvel=0
                        self.xvel=0
                        x.changeroom()
                else:

                    self.yvel=0
                    self.xvel=0
                    x.changeroom()

        #checking checkpoint

    def animate(self):
        
        state = []
        state.append(self.airborne)
        state.append(self.moving)
        state.append(self.faceright)
        state.append(self.takingdamage)
        state.append(self.attacking)
        #Moving
        
        if state[1]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:

                if state[2]:
                    self.walkloop(walkloopright)
                else:
                    self.walkloop(walkloopleft)
        else:
            if state[0]:
                if state[2]:
                    self.updatecharacter(fallright)
                else:
                    self.updatecharacter(fallleft)
            else:
                if self.dance:

                    self.danceloop(dloop)
                elif state[2]:
                    self.standloop(standloopright)
                else:
                    self.standloop(standloopleft)
        
        #Attacking
        if state[4]:
            if state[0]:
                if state[2]:
                    self.updatecharacter(shootfallright)
                else:
                    self.updatecharacter(shootfallleft)
            else:
                if state[1]:
                    if state[2]:
                        self.walkloop(shootrightrunloop)
                    else:
                        self.walkloop(shootleftrunloop)
                else:
                    if state[2]:
                        self.updatecharacter(shootrightstand)
                    else:
                        self.updatecharacter(shootleftstand)

        #Hurt
        if state[3]:
            if state[2]:
                self.updatecharacter(takedamageright)
            else:
                self.updatecharacter(takedamageleft)

        

    #Standing Animation Loop    
    def standloop(self, loop):
        if self.standcounter == 0 or self.standcounter == 1:
            self.walkcounter = 0
            self.updatecharacter(loop[0])
        elif self.standcounter == 200: self.updatecharacter(loop[1])
        elif self.standcounter == 210:
            self.updatecharacter(loop[0])
            self.standcounter = 0
        self.standcounter = self.standcounter + 1

    #Walking Animation Loop
    def danceloop(self, loop):
        print(self.dancecounter)
        if self.dancecounter == 0 or self.dancecounter == 1:
            self.standcounter = 0
            self.counter=0
            self.d.stop()
            self.d.play()
            self.updatecharacter(loop[1])
        elif self.dancecounter==(5+(self.counter*9)):
            try:
                self.updatecharacter(loop[self.counter])
                self.counter+=1
            except IndexError:
                self.dancecounter=0
                self.counter=0
            
            
        elif self.dancecounter >= 995:
            self.updatecharacter(loop[1])
            self.dancecounter = 0
            self.counter=0
        self.dancecounter += 1

    def walkloop(self, loop):
        if self.walkcounter == 0 or self.walkcounter == 1:
            self.standcounter = 0
            self.updatecharacter(loop[1])
        elif self.walkcounter == 5: self.updatecharacter(loop[1])
        elif self.walkcounter == 10: self.updatecharacter(loop[2])
        elif self.walkcounter == 15: self.updatecharacter(loop[3])
        elif self.walkcounter == 20: self.updatecharacter(loop[4])
        elif self.walkcounter == 25: self.updatecharacter(loop[5])
        elif self.walkcounter == 30: self.updatecharacter(loop[6])
        elif self.walkcounter == 35: self.updatecharacter(loop[7])
        elif self.walkcounter == 40: self.updatecharacter(loop[8])
        elif self.walkcounter == 45: self.updatecharacter(loop[9])
        elif self.walkcounter == 50: self.updatecharacter(loop[10])
        elif self.walkcounter == 55: self.updatecharacter(loop[11])
        elif self.walkcounter == 60: self.updatecharacter(loop[12])
        elif self.walkcounter == 65:
            self.updatecharacter(loop[1])
            self.walkcounter = 5
        self.walkcounter = self.walkcounter + 1

    #Update Current Frame
    def updatecharacter(self, ansurf): self.image = ansurf


