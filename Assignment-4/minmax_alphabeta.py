from random import randint

class Node():
	def __init__(self, depth, current, sticks, val=0):
		self.depth = depth
		self.current = current
		self.sticks = sticks
		self.val = val
		self.children = list()
		self.get_children()

	def get_children(self):
		if self.depth >= 0:
			for i in range(1,4):
				v, val = self.sticks-i, 0
				if v == 0:
					val = infinity * (-self.current)
				elif v < 0: 
					val = infinity * (-self.current)
				else:
					val = 0
				self.children.append(Node(self.depth-1, -self.current, v, val))

def minmax(node, alpha, beta, current, depth=4):
	if depth == 0 or abs(node.val) == infinity:
		return node.val

	if current == 1:
		for i in range(len(node.children)):
			child = node.children[i]
			alpha = max(alpha, minmax(child, depth - 1, alpha, beta, 1))
			if beta <= alpha:
				break
		return alpha
		
	else:
		for i in range(len(node.children)):
			child = node.children[i]
			beta = min(beta, minmax(child, depth - 1, alpha, beta, -1))
			if beta <= alpha:
				break
		return beta
		
def check_game_status(sticks, current, isHumanPlaying=True):
	if isHumanPlaying:
		if sticks <= 0:
			print("\n---------------------------------")
			if current > 0:
				if sticks == 0:
					print("\tAI Won")
				else:
					print("\tHuman Won")
			else:
				if sticks == 0:
					print("\tHuman Won")
				else:
					print("\tAI Won")
			print("---------------------------------\n")
			return False
		return True

	else:
		if sticks <= 0:
			print("\n---------------------------------")
			if current > 0:
				if sticks == 0:
					print("\tAI-1 Won")
				else:
					print("\tAI-2 Won")
			else:
				if sticks == 0:
					print("\tAI-2 Won")
				else:
					print("\tAI-1 Won")
			print("---------------------------------\n")
			return False
		return True


infinity = 10**6
sticks = int(input("\nPick no. of sticks : "))
depth, player = 0, 4
game_choice = input('Enter choice (a or b): [a] AI v/s AI [b] AI v/s Human : ')

# Game for AI v/s AI

if game_choice == 'a':
	AI_num = int(input("Which AI do you want to play first ? (1 or 2) : "))
	player = 1 if AI_num == 1 else -1
	Player_AI, Opp_AI = randint(1,3), 0
	print('AI-{}\'s choice : {}'.format(AI_num, Player_AI))
	node2 = Node(depth, player, sticks)
	sticks -= Player_AI

	while sticks > 0:

		# current player
		player = 1

		if check_game_status(sticks, player, False):

			# opponent player
			player *= -1
			node = Node(depth, player, sticks)
			res = -100
			current = infinity * (-player)

			for i in range(len(node.children)):
				children = node.children[i]
				val = minmax(children, depth, infinity, -infinity, player)

				if abs(player * infinity - val) <= abs(player * infinity - current):
					current = val
					res = i

			res += 1
			if res > sticks:
				res = sticks

			print("AI-{}\'s choice : {}".format(3-AI_num, res))
			sticks -= res
			check_game_status(sticks, player, False)

		player *= -1
		AI_num = 3 - AI_num


# Game for Human v/s AI

elif game_choice == 'b':
	while player != 1 and player != -1:
		player = input("Want to play first ? (y or n) : ")
		player = 1 if player == 'y' else -1
		node2 = Node(depth, player, sticks)

		if player == 1:
			print("Pick 1-3 sticks\n")

		while sticks > 0:
			if player == 1:
				print("Remaining sticks -> {}".format(sticks))
				choice = int(input("Human's choice : "))

				while choice > 3 or choice < 1 or choice > sticks:
					print("Please choose a valid no. of sticks")
					choice = int(input("Human's choice : "))

				sticks -= choice

			# current player
			player = 1
			if check_game_status(sticks, player):

				# opponent player
				player *= -1
				node = Node(depth, player, sticks)
				res = -100
				current = infinity * (-player)

				for i in range(len(node.children)):
					children = node.children[i]
					val = minmax(children, depth, infinity, -infinity, player)

					if abs(player * infinity - val) <= abs(player * infinity - current):
						current = val
						res = i

				res += 1
				if res > sticks:
					res = sticks

				print("AI's choice : {}\n".format(res))
				sticks -= res
				check_game_status(sticks, player)

			player *= -1
