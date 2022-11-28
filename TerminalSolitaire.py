import random

def menu():
	print("TERMINAL SOLITAIRE-----------")
	print("[1] Play")
	print("[2] Load Game")
	print("[3] High Scores")
	print("[0] Exit")
	choice = input("Choice: ")
	if choice.isdigit():
		return int(choice)
	return choice

def play():
	print("[1] Move")
	print("[2] Next card on Deck")
	print("[3] Put card from Deck to Table")
	print("[4] Put card from Table to Foundation")
	print("[5] Put card from Deck to Foundation")
	print("[6] Put card from Foundation to Table")
	choice = input("Choice: ")
	return choice

def options():
	print("[1] Save")
	print("[2] Load")
	print("[3] Help")
	print("[4] Go Back to Main Menu")
	choice = input("Choice: ")
	if choice.isdigit():
		return int(choice)
	return choice

def help():
	print()
	print("\n\nInstructions:")
	print("This is a game of solitaire also known as patience or klondike with a standard game of 1 draw in a deck and with standard scoring.")
	print("To play the game choose one of the following options:")
	print("\t[1] Move")
	print("\t[2] Next card on Deck")
	print("\t[3] Put card from Deck to Table")
	print("\t[4] Put card from Table to Foundation")
	print("\t[5] Put card from Deck to Foundation")
	print("\t[6] Put card from Foundation to Table")
	print(""" \nThe table is represented as follows:

DECK (open part of deck)   			(clover)	(spade)		(hearts)	(diamond) Score:

line 1  	line 2  	line 3  	line 4  	line 5  	line 6  	line 7
card 		x 		x 		x 		x 		x 		x
		card 		x 		x 		x  		x 		x
				card 		x 		x 		x 		x
						card 		x 		x 		x
								card 		x 		x
										card 		x
												card
		""")
	print("In move, you'll get 'Which line:' type the number of the line you want a card to be moved and then 'Move to:' type the number of the line where you want your card to move to.")
	print("\t\tIf you type the line plus part in 'Which line:' and then input the line where you want to put the card in 'Move to:' you'll get a new prompt saying 'From what card:' you can type whatever card it starts on for multiple stacks of cards. Case sensitive for Ace, Jack, Queen and King.")
	print("In next card on deck, you'll see the next open card in the DECK above.")
	print("In put card from deck to table, the current open part of deck will be moved to the line that you typed in 'Move to:'.")
	print("In put card from table to foundation, program will prompt 'Which line:', type the line where you want a card to be put to foundation, in the order Ace first up until King.")
	print("In put card for deck to foundation, the current open card in DECK will be placed in the foundation if valid.")
	print("In put card from foundation to table, pick a suite from foundation, the current card open will be put back to what line you want, if valid.")
	print("Type options in choice to see more.")
	print("Back to Game?")
	x = input("Type Y: ")
	while True:
		if x.capitalize() == 'Y':
			break
		else: 
			break

def restrictions2(a,b):
	for n in range(len(table),0,-1):
		if 'clvr' in table[n][b] or 'spde' in table[n][b]:
			for values in table.values():
				if 'clvr' in values[a] or 'spde' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif 'hrt' in table[n][b] or 'dia' in table[n][b]:
			for values in table.values():
				if 'hrt' in values[a] or 'dia' in values[a]:
					return 1
				elif values[a] != 'x':
					return

def restrictions(a,b):
	if table[1][b] == '':
		for values in table.values():
			if 'A' in values[a] or '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a]:
					return 1
			if values[a] != 'x':
				break
	for n in range(len(table),0,-1): 
		if 'A' in table[n][b]:
			for values in table.values():
				if 'A' in values[a] or '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '2' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '3' in table[n][b]:
			for values in table.values():
				if 'A' in values[a]  or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '4' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or 'A' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '5' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or 'A' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '6' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or 'A' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '7' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or 'A' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '8' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or 'A' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '9' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or 'A' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif '10' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or 'A' in values[a] or '10' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif 'J' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or 'A' in values[a] or 'J' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif 'Q' in table[n][b]:
			for values in table.values():
				if '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'A' in values[a] or 'Q' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return
		elif 'K' in table[n][b]:
			for values in table.values():
				if 'A' in values[a] or '2' in values[a] or '3' in values[a] or '4' in values[a] or '5' in values[a] or '6' in values[a] or '7' in values[a] or '8' in values[a] or '9' in values[a] or '10' in values[a] or 'J' in values[a] or 'K' in values[a]:
					return 1
				elif values[a] != 'x':
					return

def move(place1,place2):
	global a
	place1 = place1-1
	place2 = place2-1
	z = [] #temporary storage for the card to be moved
	if restrictions2(place1,place2) == 1:
		print("\nInvalid Move!")
		return
	if restrictions(place1,place2) == 1:
		print("\nInvalid Move!")
		return
	if len(table[len(table)][place2]) > 0: #adds a new line for cards greater than the dictionary length
		table[len(table)+1] = ['','','','','','','']
	for values in table.values(): #stores card to move to the temporary storage
		if values[place1] != 'x' and values[place1] != '':
			z.append(values[place1])
			values[place1] = ''	
	for num in range(len(z)): #puts all cards from temp storage to where user will move the cards
		for values in table.values():
			if values[place2] == '':
				values[place2] = z[num]
				break
		if len(table[len(table)][place2]) > 0: #adds new line for every iteration where there is no more space for card
			table[len(table)+1] = ['','','','','','','']
	for empty in range(len(table),0,-1): #checks if there are empty lists in dictionary to prevent empty spaces
		if  max(table[empty]) == '':
			del table[empty]
	for close in range(len(table),0,-1): #replaces x in table (closed cards) with card from list "closed"
		if table[close][place1] == 'x':
			table[close][place1] = closed.pop()
			break

def check(x,y):
	if len(y[0]) == 1:
		z = y
	else:
		z = y[0]
	if 'clvr' in z or 'spde' in z:
		for num in range(len(table),0,-1):
			if 'clvr' in table[num][x] or 'spde' in table[num][x]:
				return 1
			elif table[num][x] != '':
				return
	elif 'hrt' in z or 'dia' in z:
		for num in range(len(table),0,-1):
			if 'hrt' in table[num][x] or 'dia' in table[num][x]:
				return 1
			elif table[num][x] != '':
				return

def move2(x,y):  # checks if moving card from deck to table is valid 
	global score
	x = x-1
	if len(y[0]) == 1:
		z = y
	elif y[0] == 'Aspde':
		if check(x,fspade[len(fspade)-1]) == 1 or table[1][x] == '':
			print("\nInvalid Move!")
			return
		else:
			z = fspade[len(fspade)-1] 
	elif y[0] == 'Aclvr':
		z = fclover[len(fclover)-1]
	elif y[0] == 'Ahrt':
		z = fheart[len(fheart)-1]
	elif y[0] == 'Adia':
		z = fdiamond[len(fdiamond)-1]
	else:
		z = y[0]
	if check(x,z) == 1:
		print("\nInvalid Move!")
		return
	if len(table[len(table)][x]) > 0:
		table[len(table)+1] = ['','','','','','','']
	if 'A' in z: 
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if 'A' in z:
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '2' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '2' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '3' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '2' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '4' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '2' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '5' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '2' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '6' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '6' in table[num][x] or '2' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '7' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '2' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '8' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '2' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '9' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '2' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif '10' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or '2' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a
						score -= 10 
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif 'J' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or '2' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif 'Q' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or '2' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif len(table[num][x]) > 1:
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a
						score -= 10 
						return
				elif len(y[0]) == 1:
					table[num+1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]
				score += 5
				return
	elif 'K' in z:
		for num in range(len(table),0,-1):
			if 'A' in table[num][x] or '2' in table[num][x] or '3' in table[num][x] or '4' in table[num][x] or '5' in table[num][x] or '6' in table[num][x] or '7' in table[num][x] or '8' in table[num][x] or '9' in table[num][x] or '10' in table[num][x] or 'J' in table[num][x] or 'Q' in table[num][x] or 'K' in table[num][x]:
				print("\nInvalid Move!")
				return
			elif table[1][x] == '':
				if y[0] == 'Aspde' or y[0] == 'Aclvr' or y[0] == 'Ahrt' or y[0] == 'Adia':
					if 'clvr' in z:
						a = fclover.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'spde' in z:
						a = fspade.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'hrt' in z:
						a = fheart.pop()
						table[num+1][x] = a 
						score -= 10
						return
					elif 'dia' in z:
						a = fdiamond.pop()
						table[num+1][x] = a 
						score -= 10
						return
				elif len(y[0]) == 1:
					table[1][x] = opendeck.pop()
				else:
					for n in range(len(y)):
						table[num+n+1][x] = y[n]					
				score += 5
				return

def part(card,b):
	global x
	y = x[0]
	x = int(y)
	x = x-1
	z = []
	for num in range(1,len(table)):
		if card in table[num][x]:
			z.append(table[num][x])
			table[num][x] = ''
			for n in range(1,len(table)-2):
				print(table[num+n][x])
				if table[num+n][x] != '':
					z.append(table[num+n][x])
					table[num+n][x] = ''
			break
	move2(b,z) 

def completing(x): #puts cards from table to foundation
	global score
	x = x-1
	for num in range(len(table),0,-1):
		if 'clvr' in table[num][x]:
			if len(fclover) == 0 and table[num][x] == 'Aclvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 1 and table[num][x] == '2clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 2 and table[num][x] == '3clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 3 and table[num][x] == '4clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 4 and table[num][x] == '5clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 5 and table[num][x] == '6clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 6 and table[num][x] == '7clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 7 and table[num][x] == '8clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 8 and table[num][x] == '9clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 9 and table[num][x] == '10clvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 10 and table[num][x] == 'Jclvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 11 and table[num][x] == 'Qclvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fclover) == 12 and table[num][x] == 'Kclvr':
				fclover.append(table[num][x])
				table[num][x] = ''
				score += 10
			else:
				print("\nInvalid Move!")
				return
			for lol in range(len(table),0,-1): #replaces x in table (closed cards) with card from list "closed"
				if table[lol][x] == 'x' and table[lol+1][x] == '':
					table[lol][x] = closed.pop()
					break
			break
		elif 'spde' in table[num][x]:
			if len(fspade) == 0 and table[num][x] == 'Aspde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 1 and table[num][x] == '2spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 2 and table[num][x] == '3spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 3 and table[num][x] == '4spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 4 and table[num][x] == '5spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 5 and table[num][x] == '6spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 6 and table[num][x] == '7spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 7 and table[num][x] == '8spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 8 and table[num][x] == '9spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 9 and table[num][x] == '10spde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 10 and table[num][x] == 'Jspde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 11 and table[num][x] == 'Qspde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fspade) == 12 and table[num][x] == 'Kspde':
				fspade.append(table[num][x])
				table[num][x] = ''
				score += 10
			else:
				print("\nInvalid Move!")
				return
			for lol in range(len(table),0,-1): #replaces x in table (closed cards) with card from list "closed"
				if table[lol][x] == 'x' and table[lol+1][x] == '':
					table[lol][x] = closed.pop()
					break
			break
		elif 'hrt' in table[num][x]:
			if len(fheart) == 0 and table[num][x] == 'Ahrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 1 and table[num][x] == '2hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 2 and table[num][x] == '3hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 3 and table[num][x] == '4hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 4 and table[num][x] == '5hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 5 and table[num][x] == '6hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 6 and table[num][x] == '7hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 7 and table[num][x] == '8hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 8 and table[num][x] == '9hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 9 and table[num][x] == '10hrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 10 and table[num][x] == 'Jhrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 11 and table[num][x] == 'Qhrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fheart) == 12 and table[num][x] == 'Khrt':
				fheart.append(table[num][x])
				table[num][x] = ''
				score += 10
			else:
				print("\nInvalid Move!")
				return
			for lol in range(len(table),0,-1): #replaces x in table (closed cards) with card from list "closed"
				if table[lol][x] == 'x' and table[lol+1][x] == '':
					table[lol][x] = closed.pop()
					break	
			break
		elif 'dia' in table[num][x]:
			if len(fdiamond) == 0 and table[num][x] == 'Adia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 1 and table[num][x] == '2dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 2 and table[num][x] == '3dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 3 and table[num][x] == '4dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 4 and table[num][x] == '5dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 5 and table[num][x] == '6dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 6 and table[num][x] == '7dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 7 and table[num][x] == '8dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 8 and table[num][x] == '9dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 9 and table[num][x] == '10dia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 10 and table[num][x] == 'Jdia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 11 and table[num][x] == 'Qdia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			elif len(fdiamond) == 12 and table[num][x] == 'Kdia':
				fdiamond.append(table[num][x])
				table[num][x] = ''
				score += 10
			else:
				print("\nInvalid Move!")
				return
			for lol in range(len(table),0,-1): #replaces x in table (closed cards) with card from list "closed"
				if table[lol][x] == 'x' and table[lol+1][x] == '':
					table[lol][x] = closed.pop()
					break	
			break

def completing2(x): #checks if card in deck can be put to foundation
	global score
	if len(fclover) == 0 and x == 'Aclvr': #start of checking of clover
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 1 and x == '2clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 2 and x == '3clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 3 and x == '4clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 4 and x == '5clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 5 and x == '6clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 6 and x == '7clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 7 and x == '8clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 8 and x == '9clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 9 and x == '10clvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 10 and x == 'Jclvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 11 and x == 'Qclvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fclover) == 12 and x == 'Kclvr':
		fclover.append(opendeck.pop())
		score += 10
	elif len(fspade) == 0 and x == 'Aspde': #start of checking of spade
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 1 and x == '2spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 2 and x == '3spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 3 and x == '4spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 4 and x == '5spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 5 and x == '6spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 6 and x == '7spde':
		fcspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 7 and x == '8spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 8 and x == '9spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 9 and x == '10spde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 10 and x == 'Jspde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 11 and x == 'Qspde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fspade) == 12 and x == 'Kspde':
		fspade.append(opendeck.pop())
		score += 10
	elif len(fheart) == 0 and x == 'Ahrt': #start of checking of hearts
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 1 and x == '2hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 2 and x == '3hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 3 and x == '4hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 4 and x == '5hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 5 and x == '6hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 6 and x == '7hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 7 and x == '8hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 8 and x == '9hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 9 and x == '10hrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 10 and x == 'Jhrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 11 and x == 'Qhrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fheart) == 12 and x == 'Khrt':
		fheart.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 0 and x == 'Adia': #start of checking of diamond
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 1 and x == '2dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 2 and x == '3dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 3 and x == '4dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 4 and x == '5dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 5 and x == '6dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 6 and x == '7dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 7 and x == '8dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 8 and x == '9dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 9 and x == '10dia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 10 and x == 'Jdia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 11 and x == 'Qdia':
		fdiamond.append(opendeck.pop())
		score += 10
	elif len(fdiamond) == 12 and x == 'Kdia':
		fdiamond.append(opendeck.pop())
		score += 10
	else:
		print("\nInvalid Move!")
		return

def scores(name):
	fileHandle = open("scores.txt","a")
	fileHandle.write(str(score)+"_"+name+"\n")
	fileHandle.close()

def highscore():
	z = []
	fileReader = open("scores.txt","r")
	for line in fileReader:
		data = line[:-1]
		moredata = data.split("_")
		z.append(moredata)
	fileReader.close()
	z.sort(reverse = True)
	print("\nHIGHSCORES------------\n")
	n = 1
	if len(z) > 5:
		m = 6
	else:
		m = len(z)
	for num in range(0,m):
		print("Top",n,end="\t")
		for line2 in z[num]:
			print(line2,end="\t")
		print()
		n += 1
	print()
		
def save():
	fileWriter = open("game.txt","w")
	for line in closed:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	for line in fspade:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	for line in fclover:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	for line in fheart:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	for line in fdiamond:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	for line in closeddeck:
		fileWriter.write(line+"_")
	fileWriter.write("\n")
	if len(opendeck) == 1:
		fileWriter.write(opendeck[0])
	fileWriter.write("\n")
	for line in table.values():
		for value in range(0,7):
			fileWriter.write(line[value]+"_")
		fileWriter.write("\n")
	fileWriter.write(str(score)+"\n")
	fileWriter.close()
	print("\nGame Saved!")

def load():
	global closed
	global table
	global closeddeck
	global fspade
	global fclover
	global fheart
	global fdiamond
	global opendeck
	global score
	fileReader = open("game.txt","r")
	soupydata = []
	for line in fileReader:
		data = line[:-1]
		moredata = data.split("_")
		soupydata.append(moredata)
	fileReader.close()
	closed = soupydata[0][:-1] 
	fspade,fclover,fheart,fdiamond = soupydata[1][:-1],soupydata[2][:-1],soupydata[3][:-1],soupydata[4][:-1]
	closeddeck = soupydata[5][:-1]
	opendeck = soupydata[6][:-1]
	num = 1
	for n in range(7,len(soupydata)-1):
		table[num] = soupydata[n][:-1]
		num+=1
	score = int(soupydata[len(soupydata)-1][0])

def randomizer():
	deck = []
	deck.extend(clover)
	deck.extend(spade)
	deck.extend(heart)
	deck.extend(diamond)
	random.shuffle(deck)
	return deck

def put():
	y = 0
	for line in table:
		table[line][y] = deck[y]
		y += 1
	closed.extend(deck[7:28])
	closeddeck.extend(deck[28:53])

def foundation():
	print("\nDECK",end="\t")
	if len(opendeck) == 1:
		print(opendeck[0],end="\t\t")
	else:
		print(end="\t\t")
	if len(fclover) > 0:
		print(fclover[len(fclover)-1],end="\t")
	else:
		print(end="\t")
	if len(fspade) > 0:
		print(fspade[len(fspade)-1],end="\t")
	else:
		print(end="\t")
	if len(fheart) > 0:
		print(fheart[len(fheart)-1],end="\t")
	else:
		print(end="\t")
	if len(fdiamond) > 0:
		print(fdiamond[len(fdiamond)-1],end="\t")
	else:
		print(end="\t")
	print("Score:",score)
	print()
	for line in table.values():
		for line2 in range(0,7):
			print(line[line2],end="\t")
		print()

while True:
	score = 0
	clover = ['Aclvr','2clvr','3clvr','4clvr','5clvr','6clvr','7clvr','8clvr','9clvr','10clvr','Jclvr','Qclvr','Kclvr']
	spade = ['Aspde','2spde','3spde','4spde','5spde','6spde','7spde','8spde','9spde','10spde','Jspde','Qspde','Kspde']
	heart = ['Ahrt','2hrt','3hrt','4hrt','5hrt','6hrt','7hrt','8hrt','9hrt','10hrt','Jhrt','Qhrt','Khrt']
	diamond = ['Adia','2dia','3dia','4dia','5dia','6dia','7dia','8dia','9dia','10dia','Jdia','Qdia','Kdia']
	table = {1:['','x','x','x','x','x','x'],
         	 2:['','','x','x','x','x','x'],
		 	 3:['','','','x','x','x','x'],
		 	 4:['','','','','x','x','x'],
		 	 5:['','','','','','x','x'],
		 	 6:['','','','','','','x'],
		 	 7:['','','','','','','',]}
	closed = []
	closeddeck = []
	opendeck = []
	fclover,fspade,fheart,fdiamond = [],[],[],[]
	deck = randomizer()
	put()
	choice = menu()
	if choice == 1:
		help()
		while True:
			foundation()
			choice2 = play()
			if 'options' in choice2 or choice2.isalpha():
				print()
				print("[1] Save Game")
				print("[2] Load Game")
				print("[3] End Game")
				print("[4] Help")
				print("[5] Return to Game")
				print("[6] Exit Game without saving")
				x = int(input("Which Choice: "))
				if x == 1:
					save()
				elif x == 2:
					load()
				elif x == 3:
					print("\nGame Over.")
					print("Your score is",score)
					x = input("Type your name: ")
					print()
					scores(x)
					break
				elif x == 4:
					help()
				elif x == 5:
					continue
				elif x == 6:
					break
			elif choice2 == '':
				print("\nInvalid Choice!")
			else:
				choice2 = int(choice2)
			if choice2 == 1:
				x = input("Which line: ")
				y = int(input("Move to: "))
				if len(x) > 1:
					if 'part' in x:
						a = input("From what card: ")
						part(a,y)
					else:
						print("\nInvalid Input!")
				elif len(x) == 1:
					x = int(x)
					if x>7 or x<1 or y>7 or y<1:
						print("\nInvalid Choice!")
					else: 
						move(x,y)
				elif str(y).isalpha():
					print("Invalid Choice!")
				else:
					print("Invalid Choice!")
			elif choice2 == 2:
				if len(opendeck) == 1:
					closeddeck.append(opendeck.pop())
					opendeck.append(closeddeck.pop(0))
				elif len(opendeck) == 0 and len(closeddeck) == 0:
					print("\nNo more Cards in Deck.")
				else:
					opendeck.append(closeddeck.pop(0))
			elif choice2 == 3:
				x = int(input("Move to: "))
				if x>7 or x<1:
					print("\nInvalid Choice!")
				elif len(opendeck) == 0:
					print("\nNo cards open in deck.")
				elif str(x).isalpha():
					print("Invalid Choice!")
				else:
					y = opendeck[0]
					move2(x,y)
			elif choice2 == 4:
				x = int(input("Which line: "))
				if x>7 or x<1:
					print("\nInvalid Choice!")
				elif str(x).isalpha():
					print("Invalid Choice!")
				else: 
					completing(x)
			elif choice2 == 5:
				if len(opendeck) == 1:
					x = opendeck[0]
					completing2(x)
				else:
					print("\nNo cards open in deck.")
			elif choice2 == 6:
				x = input("Which Suite: ")
				if x.lower() == 'spade' and len(fspade) > 0:
					x = fspade
				elif x.lower() == 'clover' and len(fclover) > 0:
					x = fclover
				elif x.lower() == 'hearts' and len(fheart) > 0:
					x = fheart
				elif x.lower() == 'diamond' and len(fdiamond) > 0:
					x = fheart
				else:
					print("\nNo cards in foundation yet.")
					continue
				y = int(input("Which line: "))
				move2(y,x)

			if clover == fclover and spade == fspade and heart == fheart and diamond == fdiamond:
				print("\nCongratulations!")
				print("Your score is",score)
				x = input("Type your name: ")
				print()
				scores(x)

	elif choice == 2:
		load()
		help()
		while True:
			foundation()
			choice2 = play()
			if 'options' in choice2 or choice2.isalpha():
				print()
				print("[1] Save Game")
				print("[2] Load Game")
				print("[3] End Game")
				print("[4] Help")
				print("[5] Return to Game")
				print("[6] Exit Game without saving")
				x = int(input("Which Choice: "))
				if x == 1:
					save()
				elif x == 2:
					load()
				elif x == 3:
					print("\nGame Over.")
					print("Your score is",score)
					x = input("Type your name: ")
					print()
					scores(x)
					break
				elif x == 4:
					help()
				elif x == 5:
					continue
				elif x == 6:
					break
			elif choice2 == '':
				print("\nInvalid Choice!")
			else:
				choice2 = int(choice2)
			if choice2 == 1:
				x = input("Which line: ")
				y = int(input("Move to: "))
				if len(x) > 1:
					if 'part' in x:
						a = input("From what card: ")
						part(a,y)
					else:
						print("\nInvalid Input!")
				elif len(x) == 1:
					x = int(x)
					if x>7 or x<1 or y>7 or y<1:
						print("\nInvalid Choice!")
					else: 
						move(x,y)
				elif str(y).isalpha():
					print("Invalid Choice!")
				else:
					print("Invalid Choice!")
			elif choice2 == 2:
				if len(opendeck) == 1:
					closeddeck.append(opendeck.pop())
					opendeck.append(closeddeck.pop(0))
				elif len(opendeck) == 0 and len(closeddeck) == 0:
					print("\nNo more Cards in Deck.")
				else:
					opendeck.append(closeddeck.pop(0))
			elif choice2 == 3:
				x = int(input("Move to: "))
				if x>7 or x<1:
					print("\nInvalid Choice!")
				elif len(opendeck) == 0:
					print("\nNo cards open in deck.")
				elif str(x).isalpha():
					print("Invalid Choice!")
				else:
					y = opendeck[0]
					move2(x,y)
			elif choice2 == 4:
				x = int(input("Which line: "))
				if x>7 or x<1:
					print("\nInvalid Choice!")
				elif str(x).isalpha():
					print("Invalid Choice!")
				else: 
					completing(x)
			elif choice2 == 5:
				if len(opendeck) == 1:
					x = opendeck[0]
					completing2(x)
				else:
					print("\nNo cards open in deck.")
			elif choice2 == 6:
				x = input("Which Suite: ")
				if x.lower() == 'spade' and len(fspade) > 0:
					x = fspade
				elif x.lower() == 'clover' and len(fclover) > 0:
					x = fclover
				elif x.lower() == 'hearts' and len(fheart) > 0:
					x = fheart
				elif x.lower() == 'diamond' and len(fdiamond) > 0:
					x = fheart
				else:
					print("No cards in foundation yet.")
					continue
				y = int(input("Which line: "))
				move2(y,x)
			if clover == fclover and spade == fspade and heart == fheart and diamond == fdiamond:
				print("\nCongratulations!")
				print("Your score is",score)
				x = input("Type your name: ")
				print()
				scores(x)
	elif choice == 3:
		highscore()
	elif choice == 0:
		print("\nExiting Game...\nGoodbye.")
		break
	elif str(choice).isalpha():
		print("Invalid Choice!")
	else:
		print("Invalid Choice!")
 
#foundation to table -10 points

