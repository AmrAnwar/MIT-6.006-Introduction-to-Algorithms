def insection_sort(my_list):
	for i in range(len(my_list)):
		for j in range(i+1,len(my_list)):
			
			if my_list[i] > my_list[j]:
				my_list[i], my_list[j] = my_list[j], my_list[i]
	return my_list


# sorted_list = insection_sort([3,2,1,6,5,4,7,8,9,10])
# if sorted_list == [1,2,3,4,5,6,7,8,9,10]:
# 	print "GOOD"
