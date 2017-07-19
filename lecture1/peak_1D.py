"""
Find Peak algorithms 1D
"""
my_list = raw_input("enter the array elements: ")
int_list = map(int, my_list.split(" "))
if len(int_list) < 2 :
	raise Exception("enter list please")

def check_peak_simple_algorithm(int_list):
	"""
	straight Forward simple Algorithm for find all Peaks ,Worst_Case: O(n)
	"""
	for i in range(len(int_list)) :
		if i == 0 :
			if int_list[i] >= int_list[i+1] :
				yield int_list[i]
		elif (i == (len(int_list)-1)):
			if int_list[i] >= int_list[i-1] :
				yield int_list[i]
		elif int_list[i] >= int_list[i+1] and int_list[i] >= int_list[i-1]:
			yield int_list[i]


def check_peak_binary(int_list):
	"""
	using binary search for find a peak , Worst_Case: theta(log(n))
	"""
	position  = (len(int_list)-1)//2
	if (len(int_list) == 1): return int_list[0]
	if int_list[position + 1] > int_list[position]:
		return check_peak_binary(int_list[position+1 :])
	elif int_list[position -1] > int_list[position]:
		return check_peak_binary(int_list[:position])
	else:
		return "the peak: %s"%(int_list[position]) 


def yield_data(yield_list):
	"""
	convert yield data to normal list , Worst_Case: Log(n)
	"""
	y = [ i  for i in yield_list ]
	return y


# peak_list = check_peak_simple_algorithm(int_list)
# print yield_data(peak_list)
print check_peak_binary(int_list)
