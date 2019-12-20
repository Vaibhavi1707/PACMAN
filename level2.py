import pygame
from random import *
from math import *
from pac import *
level2Display=pygame.display.set_mode((display_h,display_w))
pygame.display.set_caption("PACMAN")
def gameloop_2ghosts():
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
			level2Display.fill(white)
			board()
			drawImg=pygame.image.load('pac.png')
			level2Display.blit(drawImg,(x0,y0))
			pygame.draw.rect(level2Display,black,(g,h,grid_width,grid_width))
			ghost1=pygame.image.load('ghost1.png')
			level2Display.blit(ghost1,(xg1,yg1))
			ghost2=pygame.image.load('ghost2.png')
			level2Display.blit(ghost2,(xg2,yg2))
			pygame.draw.rect(level2Display,green,(newgame_x,newgame_y,newgame_w,newgame_h))
			message_display('NEW GAME',20,newgame_x,newgame_y,newgame_w,newgame_h,black)
			pygame.draw.rect(level2Display,red,(800,920,160,40))
			message_display('QUIT',20,800,920,160,40,black)
			hover_and_functionality(40,newgame_x,newgame_y,newgame_w,newgame_h,bright_green,'RESTART','new game')
			hover_and_functionality(40,800,920,160,40,bright_red,'QUIT','quit')
			drawImg=pygame.image.load('pac.png')
			level2Display.blit(drawImg,(x0,y0))
			if event.type==pygame.KEYDOWN:
				ch=randint(1,4)
				ch1=randint(1,4)
				if ch!=ch1:
					if ch==1 and 0<=floor((yg1-y)/grid_width)<10 and 0<=floor((xg1+grid_width-x)/grid_width)<10 and not arr[floor((yg1-y)/grid_width)][floor((xg1+grid_width-x)/grid_width)]==1:
						xg1+=grid_width
					elif ch==2 and 0<=floor((yg1-y)/grid_width)<10 and 0<=floor((xg1-grid_width-x)/grid_width)<10 and not arr[floor((yg1-y)/grid_width)][floor((xg1-grid_width-x)/grid_width)]==1 :
						xg1-=grid_width
					elif ch==3 and 0<=floor((xg1-x)/grid_width)<10 and 0<=floor((yg1+grid_width-y)/grid_width)<10 and not arr[floor((yg1+grid_width-y)/grid_width)][floor((xg1-x)/grid_width)]==1:
						yg1+=grid_width
					elif ch==4 and 0<=floor((xg1-x)/grid_width)<10 and 0<=floor((yg1-grid_width-y)/grid_width)<10 and not arr[floor((yg1-grid_width-y)/grid_width)][floor((xg1-x)/grid_width)]==1:
						yg1-=grid_width
					if ch1==1 and 0<=floor((yg2-y)/grid_width)<10 and 0<=floor((xg2+grid_width-x)/grid_width)<10 and not arr[floor((yg2-y)/grid_width)][floor((xg2+grid_width-x)/grid_width)]==1:
						xg2+=grid_width
					elif ch1==2 and 0<=floor((yg2-y)/grid_width)<10 and 0<=floor((xg2-grid_width-x)/grid_width)<10 and not arr[floor((yg2-y)/grid_width)][floor((xg2-grid_width-x)/grid_width)]==1 :
						xg2-=grid_width
					elif ch1==3 and 0<=floor((xg2-x)/grid_width)<10 and 0<=floor((yg2+grid_width-y)/grid_width)<10 and not arr[floor((yg2+grid_width-y)/grid_width)][floor((xg2-x)/grid_width)]==1:
						yg2+=grid_width
					elif ch1==4 and 0<=floor((xg2-x)/grid_width)<10 and 0<=floor((yg2-grid_width-y)/grid_width)<10 and not arr[floor((yg2-grid_width-y)/grid_width)][floor((xg2-x)/grid_width)]==1:
						yg2-=grid_width
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
						#print(c,arr)
			if (x0==xg1 and y0==yg1) or (x0==xg2 and y0==yg2):
				t+=1
				message_display('GAME OVER',80,g,h,800,320,red)
			if c==0 and t==0:
				message_display('YOU WON',80,g,h,800,320,green)
			level2Display.blit(ghost1,(xg1,yg1))
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
