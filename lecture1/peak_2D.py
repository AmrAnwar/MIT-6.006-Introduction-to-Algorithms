"""
find peak 2 D 
for any array n * m:
- c - - 
b a d - 
- e - - 
a is a peak if a greater than or equal b,c,d,e
"""

# user input  

# my_list = raw_input("enter the rows number & cols like: 2,3 :")
# rows,cols = map(int, my_list.split(","))
# int_list = list()
# for row in range(rows):
# 	row_data = raw_input("enter the row number %s " %(row))
# 	data = map(int, row_data.split(" "))
# 	if (len(data)!=cols):
# 		raise Exception("col must have %s elements "%(cols))
# 	int_list.append(data)
# print int_list

def greedy_ascent(int_list):
	"""
	this is the striaght forward algorithm for find all peak in 2D array , complexity theta(n*m)
	"""
	n = len(int_list)
	m = len(int_list[0])
	def setvalue(row, col):
		if (row < 0 or row == n ) or (col < 0 or col == m ):
			return None
		return int_list[row][col]


	for row in range(len(int_list)):
		for col in range(len(int_list[row])):
			right = setvalue(row, col+1)
			left = setvalue(row, col-1)
			up = setvalue(row-1, col)
			down = setvalue(row+1, col)
			num = int_list[row][col]
			if all( i <= num for i in [right,left,up,down]):
				yield num


def yield_data(yield_list):
	"""
	convert yield data to normal list , Worst_Case: Log(n)
	"""
	y = [ i  for i in yield_list ]
	return y

	
# user input 
# peak_list = greedy_ascent(int_list)


#input test
input_test = [ 	
				[1,2,5],
				[3,4,3],
				[7,8,9],
			]			
peak_list = greedy_ascent(input_test)
print yield_data(peak_list)	


def fast_algorithm(int_list):
	"""
		complexity theta(n*log(m))
	"""
	def setvalue(row,col):
		if (col < 0 or col == m ):
			return None
		return int_list[row][col]

	n = len(int_list)
	m = len(int_list[0])
	j = (m-1)//2 
	i_ = 0  
	max_ = int_list[i_][j]

	for i in range(n):
		if int_list[i][j] > max_:
			max_ = int_list[i][j]
			i_ = i
	right = setvalue(i_, j+1)
	left = setvalue(i_, j-1)
	
	if (max_ < right):
		new_list = [ i[j+1:] for i in int_list ]
		return fast_algorithm(new_list) 
	elif (max_ < left):
		new_list = [ i[:j] for i in int_list ]
		return fast_algorithm(new_list) 
	else:
		return max_
		

input_test  = [
				[1,2,5],
				[3,4,3],
				[7,8,9],
			]
print fast_algorithm(input_test)