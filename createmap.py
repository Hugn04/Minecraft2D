import pygame
import os
pygame.init()
s_width = 1000
s_height = 500
size = 30
cube = int(s_width/size)
block_w = 300
block_h = 15
screen = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Tạo Map")
game = 1
BLACK=(160,160,160)
keep = False
check = False
#worlds =[0]*block_w*block_h
file_data=open("M_Data/M_Save/data.txt",'r',encoding = 'utf-8''')
list_fdata=file_data.read()
worlds = list_fdata.split(",")
worlds.remove("")
for i in range(len(worlds)):
	worlds[i] = int(worlds[i])
if len(worlds) < block_w*block_h:
	worlds =[0]*block_w*block_h
def gpos(x):
	return x*cube
def Draw_line(x,y):
	for i in range(block_w + 1):
		pygame.draw.line(screen,BLACK,(x + gpos(i),y + 0),(x + gpos(i),y + block_h*cube))
	for i in range(block_h + 1):
		pygame.draw.line(screen,BLACK,(x + 0,y + gpos(i)),(x + block_w*cube, y + gpos(i)))


class World:
	def __init__(self,worlds):
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_V"))
		self.image = []
		self.worlds = worlds
		for i in range(self.num_dir):
			self.image.append(pygame.transform.scale(pygame.image.load(f"M_Data/M_Img/Img_V/{i}.png"),(cube,cube)))
		pygame.display.set_icon(self.image[2])
	def Draw(self,mode,temp_x,temp_y):
		pos = pygame.mouse.get_pos()
		for i,n in enumerate(self.worlds):
			if n > 0:
				x = i % block_w * cube
				y = i // block_w * cube
				screen.blit(self.image[n],(temp_x + x,temp_y+ y))
	def Update(self,K_Lctrl):
		if K_Lctrl:
			for i in range(self.num_dir):
				self.image[i] = pygame.transform.scale(pygame.image.load(f"M_Data/M_Img/Img_V/{i}.png"),(cube,cube))
world = World(worlds)
x = 0
y = 0
temp_x = 0
temp_y = 0
time = pygame.time.get_ticks()
mode = 2
type_block = 1
K_Lctrl = False
while game == 1:
	cube = int(s_width/size)
	pos = pygame.mouse.get_pos()
	screen.fill("white")
	world.Draw(mode,x,y)
	world.Update(K_Lctrl)
	Draw_line(x,y)
	if mode == 1:
		if keep:
			x = pos[0] - temp_x
			y = pos[1] - temp_y
	if check:
		if mode == 2:
			inx=int((pos[0] - x)/cube)
			iny=int((pos[1] - y)/cube)
			index=iny*block_w+inx
			if index < block_w * block_h:
				worlds[index]=type_block
		if pygame.time.get_ticks() - time > 50:
			keep = True
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			game = 0
		if e.type == pygame.MOUSEBUTTONDOWN:
			if K_Lctrl:
				if e.button == 4:
					size +=1
				if e.button == 5:
					size -= 1
			temp_x = pos[0] - x
			temp_y = pos[1] - y
			check = True
		if e.type == pygame.MOUSEBUTTONUP:
			time = pygame.time.get_ticks()
			check = False
			keep = False
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_LCTRL:
				K_Lctrl = True
			if e.key == pygame.K_SPACE:
				mode = 1
			if e.key == pygame.K_e:
				type_block = 0
			if e.key == pygame.K_s:
				kq=open("M_Data/M_Save/data.txt","w",encoding = 'utf-8')
				for i in range(len(worlds)):
					kq.write(str(worlds[i]) + ",")
				print("Da luu")
			if e.key == pygame.K_1:
				type_block = 1
			if e.key == pygame.K_2:
				type_block = 2
			if e.key == pygame.K_3:
				type_block = 3
			if e.key == pygame.K_4:
				type_block = 4
		if e.type == pygame.KEYUP:
			if e.key == pygame.K_SPACE:
				mode = 2
			if e.key == pygame.K_LCTRL:
				K_Lctrl = False
	pygame.display.update()
pygame.quit()