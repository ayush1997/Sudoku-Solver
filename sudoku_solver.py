import info


    


grid = info.grids	
#grid = [[u'0', u'0', u'5', u'0', u'0', u'6', u'3', u'0', u'0'], [u'8', u'0', u'0', u'3', u'1', u'0', u'0', u'4', u'2   '], [u'0', u'0', u'1', u'0', u'0', u'0', u'0', u'0', u'7'], [u'0', u'0', u'4', u'0', u'0', u'9', u'0', u'0', u'8'], [u'6', u'0', u'0', u'0', u'0', u'5', u'7', u'0', u'0'], [u'9', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'0'], [u'0', u'0', u'0', u'5', u'0', u'0', u'0', u'0', u'0'], [u'2', u'0', u'0', u'0', u'0', u'0', u'0', u'0', u'5'], [u'0', u'0', u'3', u'0', u'0', u'1', u'2', u'0', u'0']]




def solvesudoku():
	global grid
	rc = find_unassigned()
	if rc == []:
		return True
	ROW = rc[0] 
	COLMN = rc[1]
	
	for i in range(1,10):
		if issafe(i,ROW,COLMN):
			grid[ROW][COLMN] = i
			

			if solvesudoku():
				
				return True

			grid[ROW][COLMN] = 0

	return False          #backtrack when all possible numbers didny fit we make 




def UsedinRow(num,row):
	for j in range(0,9):
		if num==grid[row][j]:
			return True
	return False
def UsedinColm(num,colm):
	for j in range(0,9):
		if num==grid[j][colm]:
			return True
	return False
def UsedinBlock(num,row,colm):
	startrow = (row//3)*3
	endrow = startrow+3
	startcol = (colm//3)*3
	endcol = startcol+3
	for p in range(startrow,endrow):
		for q in range(startcol,endcol):
			if grid[p][q]==num:
				return True
	return False
def issafe(num,row,colm):
	return not UsedinRow(num,row) and not UsedinColm(num,colm) and not UsedinBlock(num,row,colm)


def find_unassigned():
	for row in range(0,9):
		for colmn in range(0,9):
			if grid[row][colmn]==0:
				return [row,colmn]
	return []

def printsud():
	for i in range(9):
		for j in range(9):
			print grid[i][j],
		print

def run():
	for i in range(9):
		for j in range(9):
			grid[i][j] = int(grid[i][j])
	
	if solvesudoku():
		
		#printsud()
		return grid 

	else:
		print "not solvable"		








