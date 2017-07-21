"""
we can split the problem in 2 function one to split any array to 2 arrays
the other function to merge every to sorted array into one  
"""
def merge_div(list):
	"""
	split array into 2 arrays then return the merge from merge(list_a,list_b)
	"""
	if (len(list) == 1): return list
	list_a = merge_div(list[ : len(list)//2])
	list_b = merge_div(list[len(list)//2 : ])	
	return merge(list_a,list_b)


def merge(a,b):
	"""
	Merge 2 arrays into one array 
	"""
	c = list()
	i = j = 0 
	while( i < len(a) and j < len(b) ):
		if a[i] < b[j] :
			c.append(a[i])
			i += 1
			if (i == len(a)):
				c += b[j:]
		else :
			c.append(b[j])
			j += 1
			if(j == len(b)):
				c += a[i:]
	return c


print merge_div([1,2,4,3,5,19,20])