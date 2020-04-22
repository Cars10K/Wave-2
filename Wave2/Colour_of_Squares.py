
GridPosition = input("Please enter a position located on the chess board: ")

Column = GridPosition[0].lower()
Row = int(GridPosition[1])

if Column in "aceg":
	ColumnStartsWithBlack = True 
else:
	ColumnStartsWithBlack = False
	
	
if ColumnStartsWithBlack:
	if Row % 2 == 0:
		white = True
	else:
		white = False
else:
	if Row % 2 == 0:
		white = False
	else:
		white = True
		
if white:
	print("That position is coloured white.")
else:
	print("That position is coloured black.")