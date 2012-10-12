from __future__ import print_function
import ipdb
import re

def p(string
	print(string, end='')

def puts(string):
	print(string)

def str_plus(string, number = 1):
	return chr((ord(to_position[0])+ number))

def get_char(number):
	return chr(number + 64)

class Chest(object):
	def __init__(self, size): #size of the chest board
		self.size = size
		self.generate_chest()
		self.turn = 'x'
		self.result = None
		self.error = None 
	def __wall_generate(self)
		wall_set = set([])
		size = self.size
		for num in [0, size + 1]:
			for char in range(0, size + 2):
				wall_set.add(get_char(char) + str(num))
		for char in [0, size+1]:
			for num in range(1, size + 1):
				wall_set.add(get_char(char) + str(num))
		return wall_set
	def generate_chest(self):
		size = self.size
		self.wall = __wall_generate()
		self.supporter = set([]) 
		for num in [1, size]:
			for char in range(1, size + 1):
				position = get_char(char) + str(num)
				if(char != (size + 1) / 2):
					self.supporter.add(position)
				elif(num == 1):
					self.x = position  
				elif(num == size):
					self.y = position  
	def print_chest(self):
		size = self.size 
		for num in range(0, size + 1):
			for char in range(0, size + 1):
				position = get_char(char) + str(num)
				if(position in self.supporter ):
					p("S")
				elif(position == self.x:
					p('X')
				elif(position == self.y:
					p('Y')
				elif(position in self.wall):
					if(num == 0 and char == 0):
						p(' ')
					elif(num == 0):
						p(char)
					elif(char == 0):
						p(num)
				else:
					p(".")
			p("\n")

	def user_input(self):
			self.user_input =  raw_input("player {:s} move(eg: a1:b2): ".format(self.turn)).upper()

	def __validate_board_size(self):
			pass

	def __validate_input_format(self):
		pattern = re.compile('^[a-zA-z][0-9]:[a-zA-Z][0-9]$')
		if (pattern.match(self.user_input)):
			self.from_position, self.to_position = self.user_input.split(':')	
		else:
			self.error = "Please use the the right format like a4:b6"

	def __validate_move_others(self):
		if (self.from_position in self.supporter['supporter_position'] or 
			(self.turn == 'x' and self.from_position == self.x) or
			(self.turn == 'y' and self.from_position == self.y)):
		else:
			self.error = "Don't move other's piece, or the piece you choose are not there"


def validate_full_move(from_position, to_position, position_hash):
	to_position[0]	
	

		
chest = Chest(9)

while(chest.result == None):
	chest.print_chest()	
	chest.user_input()
	if(validate(chest_)):
		from_position, to_position = input_value.split(':')
		if(validate_move_rule(from_position, to_position, position_hash)):
		 	who_move = validate_who_move(from_position, user_turn, position_hash)
			if(who_move):
				if(who_move == 'x'):
					position_hash['x_position'] = to_position 
				elif(who_move == 'y'):
					position_hash['y_position'] = to_position 
				elif(who_move == 'supporter'):
					position_hash['supporter_position'].remove(from_position)
					position_hash['supporter_position'].append(to_position)
				user_turn = 'y' if user_turn == 'x' else 'x'
				puts("the validation is pass the user_turn is {:s}".format(user_turn))

def __to_pos(self, x, y, next=0):
	return "{0:s}:{1:d}".format(chr(x + next ),y + next)	

def validate_full_extend(self):
	to_pos_x = ord(self.to_position[0])
	to_pos_y = int(self.to_position[1])
	obstacles = set([])
	obstacles.update(self.supporter)
	obstacles.update(self.wall)	
	obstacles.add(self.x)
	obstacles.add(self.y)

	delta_pos_x = to_pos_x - ord(self.from_position[0])
	delta_pos_y = to_pos_y - int(self.from_position[1])
	if(abs(delta_pos_x) == abs(delta_pos_y)):
		if(delta_pos_x > 0 and delta_pos_y >0 and self.__to_pos(to_pos_x, to_pos_y) not in obstacles) 
			self.error = "In you right down direction still have "
