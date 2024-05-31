import pygame
import os
pygame.init()
block_w = 300
block_h = 15
s_width = 1000
size = 30
cube = int(s_width/size)
s_height = cube * block_h
screen = pygame.display.set_mode((s_width,s_height))
pygame.display.set_caption("Minecraft")
game = 1
file_data=open("M_Data/M_Save/data.txt",'r',encoding = 'utf-8''')
list_fdata=file_data.read()
worlds = list_fdata.split(",")
worlds.remove("")
for i in range(len(worlds)):
	worlds[i] = int(worlds[i])
file_data.close()
if len(worlds) < block_w*block_h:
	worlds =[0]*block_w*block_h
def gpos(x):
	return i*cube
def Draw_line(scr,block_w,block_h,cube,x,y):
	for i in range(block_w + 1):
		pygame.draw.line(scr,"BLACK",(x + i*cube,y + 0),(x + i*cube,y + block_h*cube),2)
	for i in range(block_h + 1):
		pygame.draw.line(scr,"BLACK",(x + 0,y + i*cube),(x + block_w*cube, y + i*cube),2)
class I_Items:
	def __init__(self):
		self.items = []
		file = open("M_Data/M_Save/I_Items.txt",'r',encoding = 'utf-8''')
		list_fdata = file.read()
		self.cube = 60
		self.block_w = 8
		self.block_h = 3
		self.width = self.block_w * self.cube
		self.height = self.block_h * self.cube
		self.x = 0
		self.y = 0
		self.index = 0
		self.temp = 0
		self.items = list_fdata.split(",")
		self.items.remove("")
		for i in range(len(self.items)):
			self.items[i] = int(self.items[i])
		file.close()
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_Item"))
		self.image = []
		for i in range(self.num_dir):
			self.image.append(pygame.transform.scale(pygame.image.load(f"M_Data/M_Img/Img_Item/{i}.png"),(20,46)))
		self.temp_image = 0
		self.temp_image1 = 0
	def Draw(self,scr,x,y):
		self.scr = scr
		self.x = x
		self.y = y
		pygame.draw.rect(self.scr,"BLACK",(0,0,self.width,self.height),5)
		Draw_line(self.scr,self.block_w,self.block_h,60,x,y)
		for i,n in enumerate(self.items):
			if n > 0:
				x = (i % self.block_w * self.cube) + 20
				y = (i // self.block_w * self.cube) + 8
				self.scr.blit(self.image[n],(x,y))
	def Update(self,M_left):
		self.pos = pygame.mouse.get_pos()
		
		if self.pos[0] > inventory.x and self.pos[0] < inventory.x + self.width:
			if self.pos[1] > inventory.y and self.pos[1] < inventory.y + self.height:
				inx=int((self.pos[0] - inventory.x)/self.cube)
				iny=int((self.pos[1] - inventory.y)/self.cube)
				self.index=iny*self.block_w+inx
				if M_left:
					self.items[self.temp] = 0
					
		if M_left or In_mouse:
			screen.blit(self.image[self.temp_image],self.pos)
i_items = I_Items()
class Inventory:
	def __init__(self):
		self.width = 800
		self.height = 350
		self.x = 100
		self.y = 10
		self.scr= pygame.Surface((self.width,self.height),pygame.SRCALPHA)
	def Draw(self):
		screen.blit(self.scr,(self.x,self.y))
		self.scr.fill((0,0,25,100))
		pygame.draw.rect(self.scr,"BLACK",(0,0,self.width,self.height),5)
		i_items.Draw(self.scr,0,0)
		i_items.Update(M_left)
class Items:
	def __init__(self):
		self.width = 481
		self.height = 60
		self.COLOR = (40,40,40)
		self.items = []
		file = open("M_Data/M_Save/Items.txt",'r',encoding = 'utf-8''')
		list_fdata = file.read()
		self.items = list_fdata.split(",")
		self.items.remove("")
		for i in range(len(self.items)):
			self.items[i] = int(self.items[i])
		file.close()
		self.y = s_height - self.height - 40
		self.x = s_width / 2 - self.width/2
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_Item"))
		self.image = []
		for i in range(self.num_dir):
			self.image.append(pygame.transform.scale(pygame.image.load(f"M_Data/M_Img/Img_Item/{i}.png"),(20,46)))
		self.scr= pygame.Surface((self.width + 2,self.height + 2),pygame.SRCALPHA)
		self.item_select = 0
		self.type_item = 0
	def Draw(self):
		if self.item_select > 7:
			self.item_select = 0
		if self.item_select < 0:
			self.item_select = 7
		self.type_item = self.items[self.item_select]
		screen.blit(self.scr,(self.x, self.y))
		self.scr.fill((255,255,255,30))
		x = 0
		y = 0
		vien = 4
		for i in range(8):
			pygame.draw.line(self.scr,self.COLOR,(x,y),(x,y + 60),vien)
			pygame.draw.line(self.scr,self.COLOR,(x,y),(x + 60,y),vien)
			pygame.draw.line(self.scr,self.COLOR,(x + 60,y),(x + 60,y + 60),vien)
			pygame.draw.line(self.scr,self.COLOR,(x,y + 60),(x + 60,y  + 60),vien)
			x +=60
		for i,n in enumerate(self.items):
			if n > 0:
				x = (i % self.width * self.height) + 20
				y = (i // self.width * self.height) + 8
				self.scr.blit(self.image[n],(x,y))
		pos_x = self.item_select % self.width * self.height
		pos_y = self.item_select // self.width * self.height
		pygame.draw.line(self.scr,(255,255,255,255),(pos_x,pos_y),(pos_x,pos_y + 60),vien)
		pygame.draw.line(self.scr,(255,255,255,255),(pos_x,pos_y),(pos_x + 60,pos_y),vien)
		pygame.draw.line(self.scr,(255,255,255,255),(pos_x + 60,pos_y),(pos_x + 60,pos_y + 60),vien)
		pygame.draw.line(self.scr,(255,255,255,255),(pos_x,pos_y + 60),(pos_x + 60,pos_y + 60),vien)
		#pygame.draw.rect(self.scr,(255,255,255,90),(self.item_select % self.width * self.height,self.item_select // self.width * self.height,60,60),5)
	def Update(self):
		
		self.type_item = self.items[self.item_select]
class Weapon:
	def __init__(self):
		self.image = []
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_Item"))
		for i in range(self.num_dir):
			self.image.append(pygame.transform.rotate(pygame.image.load(f"M_Data/M_Img/Img_Item/{i}.png"),-45))
		self.image_flip = []
		for i in range(self.num_dir):
			self.image_flip.append(pygame.transform.flip(self.image[i],True,False))
		self.deg = 45
		self.direction = 1
		self.speed = 150
		self.tick = 1
		self.image_temp = self.image[items.type_item]
		self.image_temp1 = self.image[items.type_item]
		self.time = pygame.time.get_ticks()
	def Draw(self,x,y):
		self.x = x
		self.y = y
		if items.type_item != 0:
			screen.blit(self.image_temp,(x,y))
	def Update(self,direction):
		self.direction = direction
		if self.direction == 1:
			self.image_temp1 = self.image[items.type_item]
		if self.direction == -1:
			self.image_temp1 = self.image_flip[items.type_item]
	def Fire(self,M_left):
		if M_left:
			if pygame.time.get_ticks() - self.time > self.speed:
				self.tick *= -1
				if self.tick == 1:
					self.image_temp = pygame.transform.rotate(self.image_temp1,-self.deg*self.direction)
				if self.tick == -1:
					self.image_temp = self.image_temp1
				self.time = pygame.time.get_ticks()
		else:
			self.image_temp = self.image_temp1
class World:
	def __init__(self,worlds):
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_V"))
		self.image = []
		self.world_x = 0
		self.world_y = 0
		self.worlds = worlds
		for i in range(self.num_dir):
			self.image.append(pygame.transform.scale(pygame.image.load(f"M_Data/M_Img/Img_V/{i}.png"),(cube,cube)))
		pygame.display.set_icon(self.image[2])
	def Draw(self):
		for i,n in enumerate(self.worlds):
			if n > 0:
				x = i % block_w * cube
				y = i // block_w * cube
				self.rect = screen.blit(self.image[n],(self.world_x + x,self.world_y + y))
	def Update(self):
		# Keo hinh
		if player.x + self.world_x > s_width-300:
			if self.world_x > -(cube*block_w - s_width):
				self.world_x -= player.speed
		if player.x  + self.world_x < 250:
			if self.world_x < 0:
				self.world_x += player.speed
class Player:
	def __init__(self):
		self.scr= pygame.Surface((40,60),pygame.SRCALPHA)
		self.x = 0
		self.y = 0
		self.index = 1
		self.w_index_b = 0
		self.speed = 0.7
		self.tick_run = 150
		self.tick_ide = 300
		self.tick_jump = 50
		self.tick = self.tick_ide
		self.time = pygame.time.get_ticks()
		self.sprite = []
		self.type_animation = 0
		self.direction = 1
		self.gravity = 0.018
		self.velocity = 0
		self.collider_r = 1
		self.collider_l = 1
		self.collider_b = 1
		self.collider_t = 1
		self.inx = 100
		self.iny = 1
		self.Jump = False
		self.num_dir=len(os.listdir("M_Data/M_Img/Img_Nv"))
		for i in range(self.num_dir):
			self.sprite.append(pygame.image.load(f"M_Data/M_Img/Img_Nv/{i}.png"))
	def Draw(self):
		screen.blit(self.scr,(world.world_x + self.x,world.world_y + self.y))
		self.scr.fill((0,0,0,0))
		self.scr.blit(self.sprite[self.type_animation],(-(self.index-1)*self.sprite[self.type_animation].get_width()/5,0))
		# Ve vu khi
		if self.direction == 1:
			weapon.Draw(world.world_x + self.x + 25,world.world_y + self.y + 28)
		if self.direction == -1:
			weapon.Draw(world.world_x + self.x - 15,world.world_y + self.y + 28)
		weapon.Update(self.direction)
	def Move(self,Direction,K_space):
		# Roi tu do
		if self.y < self.w_index_b // block_w * cube + 60:
			self.velocity = self.velocity * self.collider_b + self.gravity
			if self.collider_b == 0:
				self.velocity = 0
		else:
			self.velocity = 0
			self.y = self.w_index_b // block_w * cube  + 60
		self.y += self.velocity
		if pygame.time.get_ticks() - self.time > self.tick:
			self.index += 1
			self.time = pygame.time.get_ticks()
		# Nhan vat nhay
		if K_space:
			if self.collider_b == 1:	
				self.y -= 1
			if self.collider_b == 0:
				self.Jump = True
		if self.Jump:
			if self.direction == 1:
				self.type_animation = 4
			if self.direction == -1:
				self.type_animation = 5
			self.tick = self.tick_jump
		# Di chuyen trai phai animation
		if Direction == "IDE":
			if self.direction == 1:
				self.type_animation = 2
			if self.direction == -1:
				self.type_animation = 3
			self.tick = self.tick_ide
		if Direction == "RIGHT":
			self.direction = 1
			self.tick = self.tick_run
			self.type_animation = 0
			self.x += self.speed * self.collider_r
		if Direction == "LEFT":
			self.direction = -1
			self.tick = self.tick_run
			self.type_animation = 1
			self.x -= self.speed * self.collider_l
		if self.index >= 5:
			self.index = 1
	def Update(self):
		#  Va cham vao map
		if self.x < 0:
			self.x = 0
		if self.x > cube * block_w - 40:
			self.x = cube * block_w - 40
		# Tao toa do va cham
		self.inx_r = int((self.x )/cube)
		self.inx_l = int((self.x + 40)/cube)
		self.iny_1 = int((self.y)/cube)
		self.iny_0 = int((self.y + 58)/cube)
		self.w_index_r = (self.iny_0 * block_w + self.inx_r) + 1
		self.w_index_l = (self.iny_0 * block_w+self.inx_l) - 1
		self.w_index_r1 = (self.iny_1 * block_w + self.inx_r) + 1
		self.w_index_l1 = (self.iny_1 * block_w+self.inx_l) - 1

		self.inx_b = int((self.x + 25)/cube)
		self.inx_b1 = int((self.x + 15)/cube)
		self.iny_b = int((self.y + 30)/cube)
		self.inx_t = int((self.x + 30)/cube)
		self.inx_t1 = int((self.x)/cube)
		self.iny_t = int((self.y + 30)/cube)
		self.w_index_b = (self.iny_b * block_w + self.inx_b) + block_w
		self.w_index_b1 = (self.iny_b * block_w + self.inx_b1) + block_w
		self.w_index_t = (self.iny_t * block_w + self.inx_t) - block_w
		self.w_index_t1 = (self.iny_t * block_w + self.inx_t1) - block_w
		# Xu li va cham
		if worlds[self.w_index_r] == 2 or worlds[self.w_index_r1] == 2 or worlds[self.w_index_r] == 1 or worlds[self.w_index_r1] == 1:
			
			self.collider_r = 0
		else:
			self.collider_r = 1
		if worlds[self.w_index_l] == 2 or worlds[self.w_index_l1] == 2 or worlds[self.w_index_l] == 1 or worlds[self.w_index_l1] == 1:
			self.collider_l = 0
		else:
			self.collider_l = 1
		if worlds[self.w_index_b] == 2 or worlds[self.w_index_b1] == 2 or worlds[self.w_index_b] == 1 or worlds[self.w_index_b1] == 1:
			self.collider_b = 0
		else:
			self.collider_b = 1
		if worlds[self.w_index_t - block_w] == 2 or worlds[self.w_index_t1 - block_w] == 2:
			self.collider_t = 0
		else:
			self.collider_t = 1
		#x = i % block_w * cube
		#y = i // block_w * cube
		if self.collider_t == 0:
			if self.y < (self.w_index_t // block_w * cube) :
				self.y = (self.w_index_t // block_w * cube)
inventory = Inventory()
items = Items()
weapon = Weapon()
world = World(worlds)
player = Player()
K_d = False
K_a = False
K_space = False
Jump = False
Direction = "IDE"
M_left = False
K_e = False
fire = False
In_mouse = False
while game == 1:
	screen.fill("white")
	#Draw_line()
	world.Draw()
	items.Draw()
	player.Draw()
	player.Move(Direction,K_space)
	weapon.Fire(fire)
	player.Update()
	if K_e:
		inventory.Draw()
	else:
		items.Update()
		world.Update()
		
		if K_d:
			Direction = "RIGHT"
		if K_a:
			Direction = "LEFT"
	# Event key
	for e in pygame.event.get():
		if e.type == pygame.QUIT:
			kq=open("M_Data/M_Save/I_Items.txt","w",encoding = 'utf-8')
			for i in range(len(i_items.items)):
				kq.write(str(i_items.items[i]) + ",")
			kq.close()
			kq=open("M_Data/M_Save/Items.txt","w",encoding = 'utf-8')
			for i in range(len(items.items)):
				kq.write(str(items.items[i]) + ",")
			kq.close()
			game = 0
		if e.type == pygame.MOUSEBUTTONDOWN:
			if e.button == 4:
				items.item_select += 1
			if e.button == 5:
				items.item_select -= 1
			if e.button == 1:
				if K_e:
					if i_items.pos[0] > inventory.x and i_items.pos[0] < inventory.x + i_items.width and i_items.pos[1] > inventory.y and i_items.pos[1] < inventory.y + i_items.height:
						if In_mouse:
							if i_items.items[i_items.index] == 0:
								i_items.items[i_items.index] = i_items.temp_image
								In_mouse = False
							else:
								i_items.temp_image1 = i_items.items[i_items.index]
								i_items.items[i_items.index] = i_items.temp_image
								i_items.temp_image = i_items.temp_image1
						else:
							i_items.temp = i_items.index
							i_items.temp_image = i_items.items[i_items.temp]
					else:
						In_mouse = False
				M_left = True
				if K_e == False:
					fire = True
		if e.type == pygame.MOUSEBUTTONUP:
			if e.button == 1:
				if K_e:
					if i_items.pos[0] > inventory.x and i_items.pos[0] < inventory.x + i_items.width and i_items.pos[1] > inventory.y and i_items.pos[1] < inventory.y + i_items.height:
						if In_mouse == False:
							if i_items.items[i_items.index] == 0:
								i_items.items[i_items.index] = i_items.temp_image
							else:
								In_mouse = True
								i_items.temp_image1 = i_items.items[i_items.index]
								i_items.items[i_items.index] = i_items.temp_image
								i_items.temp_image = i_items.temp_image1
					else:
						if i_items.temp_image != 0:
							i_items.items[i_items.temp] = i_items.temp_image
				M_left = False
				fire =False
		if e.type == pygame.KEYDOWN:
			if e.key == pygame.K_d:
				K_d = True
			if e.key == pygame.K_a:
				K_a = True
			if e.key == pygame.K_e:
				if K_e:
					K_e = False
				else:
					K_e = True
			if e.key == pygame.K_w:
				if K_e == False:
					K_space = True
					if player.collider_b == 0:
						if player.collider_t == 0:
							player.y -= 20
						else:
							player.y -= 90
			if e.key == pygame.K_SPACE:
				if K_e == False:
					K_space = True
					if player.collider_b == 0:
						if player.collider_t == 0:
							player.y -= 20
						else:
							player.y -= 90
					player.Jump = True
			if e.key == pygame.K_1:
				items.item_select = 0
			if e.key == pygame.K_2:
				items.item_select = 1
			if e.key == pygame.K_3:
				items.item_select = 2
			if e.key == pygame.K_4:
				items.item_select = 3
			if e.key == pygame.K_5:
				items.item_select = 4
			if e.key == pygame.K_6:
				items.item_select = 5
			if e.key == pygame.K_7:
				items.item_select = 6
			if e.key == pygame.K_8:
				items.item_select = 7
		if e.type == pygame.KEYUP:
			Direction = "IDE"
			if e.key == pygame.K_d:
				K_d = False
			if e.key == pygame.K_a:
				K_a = False
			if e.key == pygame.K_w:
				K_space = False
			if e.key == pygame.K_SPACE:
				K_space = False
	pygame.display.flip()
pygame.quit()