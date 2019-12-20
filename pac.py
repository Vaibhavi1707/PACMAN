import pygame
from random import *
from math import *
from level2 import *
pygame.init()
red=(200,0,0)
bright_red=(255,0,0)
black=(0,0,0)
yellow=(255,255,0)
green=(0,200,0)
bright_green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
display_h=1000
display_w=1000
score=0    
newgame_h=40
newgame_w=160
newgame_x=100
newgame_y=920
quitgame_h=40
quitgame_w=160
quitame_x=800
quitgame_y=920
level2_x=100
level2_y=20
level2_h=50
level2_w=160
gameDisplay=pygame.display.set_mode((display_h,display_w))
pygame.display.set_caption("PACMAN")
clock=pygame.time.Clock()
r=8
x=display_h/10
y=display_w/10
grid_width=80
x1=int(x+(grid_width/2))
y1=int(y+(grid_width/2))
arr=[[0,0,0,0,0,0,0,0,0,0],
	[0,1,1,1,0,1,1,1,1,0],
	[0,1,0,0,0,0,0,0,1,0],
	[0,1,0,1,0,1,1,0,1,0],
	[0,1,0,1,0,1,1,0,1,0],
	[0,0,0,0,0,0,0,0,0,0],
	[0,1,0,1,1,1,1,0,1,0],
	[0,1,0,0,0,0,0,0,1,0],
	[0,1,1,1,0,1,1,1,1,0],
	[0,0,0,0,0,0,0,0,0,0]]

def hover_and_functionality(size,x,y,w,h,c,text,action=None):
	mouse_x=pygame.mouse.get_pos()[0]
	mouse_y=pygame.mouse.get_pos()[1]
	click=pygame.mouse.get_pressed()
	if x<=mouse_x<=x+w and y<=mouse_y<=y+w:
		pygame.draw.rect(gameDisplay,c,(x,y,w+25,h+25))
		message_display(text,size,x,y,w+25,h+25,black)
		
		if click[0]==1 and action!=None:
			if action=='new game':
				for i in range(10):
					for j in range(10):
						if arr[j][i]==2:
							arr[j][i]=0
				gameloop()
			elif action=='level 2':
				gameloop_2ghosts()
			elif action=='quit':
				pygame.quit()
				quit()
def button():
	message_display(size,x,y,w,h,c)
def board():
	for i in range(10):
		for j in range(10):
			pygame.draw.rect(gameDisplay,black,(x+i*grid_width,y+j*grid_width,grid_width,grid_width))
			if arr[j][i]==0:
				pygame.draw.circle(gameDisplay,yellow,(x1+(i*grid_width),y1+(j*grid_width)),r,0)
			elif arr[j][i]==1:
				pygame.draw.rect(gameDisplay,blue,(x+i*grid_width,y+j*grid_width,grid_width,grid_width))
			elif arr[j][i]==2:
				pygame.draw.rect(gameDisplay,black,(x+i*grid_width,y+j*grid_width,grid_width,grid_width))
def display_text(text,font,c):
	TextSurface=font.render(text,True,c)
	return TextSurface,TextSurface.get_rect()
def message_display(text,size,x,y,w,h,c):
	Text=pygame.font.Font("freesansbold.ttf",size)
	Text_Surface,Text_Rect=display_text(text,Text,c)
	Text_Rect.center=(x+w/2,y+h/2)
	gameDisplay.blit(Text_Surface,Text_Rect)
def scoring(s):
	message_display(('SCORE:'+str(s)),40,400,900,320,80,black)
def gameloop():
	crashed=False
	x0=100
	y0=420
	xs=100
	ys=420
	g=x0
	h=y0
	score=0
	xg1=x+4*grid_width
	yg1=y+4*grid_width
	xg2=xg1
	yg2=yg1+grid_width
	xg3=xg2+grid_width
	yg3=yg1
	while not crashed:
		for event in pygame.event.get():
			arr[floor((ys-y)/grid_width)][floor((xs-x)/grid_width)]=2
			c=0
			t=0
			up=0
			down=0
			left=0
			right=0
			message_display('PACMAN',40,400,20,160,80,blue)
			if event.type==pygame.QUIT:
				crashed=True
				pygame.quit()
				quit()
			gameDisplay.fill(white)
			board()
			drawImg=pygame.image.load('pac.png')
			gameDisplay.blit(drawImg,(x0,y0))
			pygame.draw.rect(gameDisplay,black,(g,h,grid_width,grid_width))
			ghost1=pygame.image.load('ghost1.png')
			gameDisplay.blit(ghost1,(xg1,yg1))
			pygame.draw.rect(gameDisplay,green,(newgame_x,newgame_y,newgame_w,newgame_h))
			message_display('NEW GAME',20,newgame_x,newgame_y,newgame_w,newgame_h,black)
			pygame.draw.rect(gameDisplay,red,(800,920,160,40))
			message_display('QUIT',20,800,920,160,40,black)
			hover_and_functionality(40,newgame_x,newgame_y,newgame_w,newgame_h,bright_green,'RESTART','new game')
			hover_and_functionality(40,800,920,160,40,bright_red,'QUIT','quit')
			drawImg=pygame.image.load('pac.png')
			gameDisplay.blit(drawImg,(x0,y0))
			if event.type==pygame.KEYDOWN:
				ch=randint(1,4)
				if ch==1 and 0<=floor((yg1-y)/grid_width)<10 and 0<=floor((xg1+grid_width-x)/grid_width)<10 and not arr[floor((yg1-y)/grid_width)][floor((xg1+grid_width-x)/grid_width)]==1:
					xg1+=grid_width
				elif ch==2 and 0<=floor((yg1-y)/grid_width)<10 and 0<=floor((xg1-grid_width-x)/grid_width)<10 and not arr[floor((yg1-y)/grid_width)][floor((xg1-grid_width-x)/grid_width)]==1 :
					xg1-=grid_width
				elif ch==3 and 0<=floor((xg1-x)/grid_width)<10 and 0<=floor((yg1+grid_width-y)/grid_width)<10 and not arr[floor((yg1+grid_width-y)/grid_width)][floor((xg1-x)/grid_width)]==1:
					yg1+=grid_width
				elif ch==4 and 0<=floor((xg1-x)/grid_width)<10 and 0<=floor((yg1-grid_width-y)/grid_width)<10 and not arr[floor((yg1-grid_width-y)/grid_width)][floor((xg1-x)/grid_width)]==1:
					yg1-=grid_width
				if event.key==pygame.K_RIGHT and 0<=floor((y0-y)/grid_width)<10 and 0<=floor((x0+grid_width-x)/grid_width)<10 and not arr[floor((y0-y)/grid_width)][floor((x0+grid_width-x)/grid_width)]==1:
					x0+=grid_width
					arr[floor((y0-y)/grid_width)][floor((x0-x)/grid_width)]=2
					score+=1
					right=1
				elif event.key==pygame.K_LEFT and 0<=floor((y0-y)/grid_width)<10 and 0<=floor((x0-grid_width-x)/grid_width)<10 and not arr[floor((y0-y)/grid_width)][floor((x0-grid_width-x)/grid_width)]==1:
					x0-=grid_width
					arr[floor((y0-y)/grid_width)][floor((x0-x)/grid_width)]=2
					score+=1
					left=1
				elif event.key==pygame.K_UP and 0<=floor((x0-x)/grid_width)<10 and 0<=floor((y0-grid_width-y)/grid_width)<10 and not arr[floor((y0-grid_width-y)/grid_width)][floor((x0-x)/grid_width)]==1: 
					y0-=grid_width
					arr[floor((y0-y)/grid_width)][floor((x0-x)/grid_width)]=2
					score+=1
					up=1
				elif event.key==pygame.K_DOWN and 0<=floor((x0-x)/grid_width)<10 and 0<=floor((y0+grid_width-y)/grid_width)<10 and not arr[floor((y0+grid_width-y)/grid_width)][floor((x0-x)/grid_width)]==1:
					y0+=grid_width
					arr[floor((y0-y)/grid_width)][floor((x0-x)/grid_width)]=2
					score+=1
					down=1
			scoring(score)
			for i in range(10):
				for j in range(10):	
					if arr[j][i]==0:
						c+=1
			if (x0==xg1 and y0==yg1):
				t+=1
				message_display('GAME OVER',80,g,h,800,320,red)
			if c==0 and t==0:
				message_display('YOU WON',80,g,h,800,320,green)
				pygame.draw.rect(gameDisplay,green,(level2_x,level2_y,level2_w,level2_h))
				message_display('LEVEL 2',20,level2_x,level2_y,level2_w,level2_h,black)
				hover_and_functionality(40,level2_x,level2_y,level2_w,level2_h,bright_green,'LEVEL 2','level 2')
			gameDisplay.blit(ghost1,(xg1,yg1))
			if right==1:
				right_pac=pygame.image.load('right.png')
				gameDisplay.blit(right_pac,(x0,y0))
			elif left==1:
				left_pac=pygame.image.load('left.png')
				gameDisplay.blit(left_pac,(x0,y0))
			elif up==1:
				up_pac=pygame.image.load('up.png')
				gameDisplay.blit(up_pac,(x0,y0))
			elif down==1:
				down_pac=pygame.image.load('down.png')
				gameDisplay.blit(down_pac,(x0,y0))
		pygame.display.update()
		clock.tick(60)



if __name__=="__main__": 
	gameloop()
	pygame.quit()
	quit()
