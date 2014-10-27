#Import required packages
import numpy as np
import math

#Output file name
outfile = open('outfile.csv','w')					#Open file for writing

#Import unsolved puzzle from CSV file and save board as X
X = np.genfromtxt('infile.csv', dtype=int, delimiter=',')

#Count number of missing values in imported puzzle X
blanks = sum(1 for i in X.flat if i == 0)

#Set blank checker initially to True
blank_checker = True

#Function to scan all columns in the row 
def horizontal_check(i, x):
	for j in range(9):
		if X[i][j] == x:
			return True					#If found, return True
	return False							#If not found, return False

#Function to scan all rows in the column 
def vertical_check(j, x):
	for i in range(9):
		if X[i][j] == x:
			return True					#If found, return True
	return False							#If not found, return False

#Function to scan the square the box occupies
def square(i, j, x):
	rows = math.ceil((i+1)/3.0)					#Use ceiling to round up
	columns = math.ceil((j+1)/3.0)
	
	#Loop through the rows and columns of the box
	for r in range(int((rows-1)*3), int(((rows-1)*3+3))):
		for c in range(int((columns-1)*3), int(((columns-1)*3+3))):
			if (X[r][c] == x):
				return True				#If found, return True
	return False							#If not found, return False
	
#Run main while loop - runs as long as blanks exist and blank_checker is True
while (blanks > 0 and blank_checker is True):
	
	#Exit loop once puzzle is complete
	blank_checker = False
	
	#Loop over rows and columns of board
	for i in range(9):						#Rows
		for j in range(9):					#Columns
			if X[i][j] != 0:				#Check to see if box is blank
				continue				#Skip is a number already exists in box
			place_holder = 0;				#If box is empty, initialize place holder to 0
			for x in range(1,10):
				if (horizontal_check(i, x) is False and vertical_check(j, x) is False and square(i, j, x) is False):
					if place_holder == 0:	
						place_holder = x	#If number not found, assign number to placeholder
					else:
						place_holder = 0	#Otherwise, assign 0 to placeholder and break
						break
			if place_holder != 0:
				X[i][j] = place_holder			#Assign place holder to box
				blank_checker = True			#More empty boxes might remain
				blanks = blanks - 1			#Reduce total number of empty boxes

#Write output file
if blank_checker is False:
	outfile.write("Sudoku cannot be solved!")			#If no solution found
else:
	np.savetxt(outfile,X,delimiter=",",fmt = '%i')	#Print solution to CSV 

outfile.close()								#Close file 
		
