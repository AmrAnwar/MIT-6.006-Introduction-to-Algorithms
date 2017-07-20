# it's just a try to get better run time 
from __future__ import division
import re
import math

def doc_string(doc_x, doc_y):
	list_x = re.findall(r'\w+',doc_x)
	list_y = re.findall(r'\w+',doc_y)

	count_dict = count_string(list_x,0)
	count_dict = count_string(list_y,1,dict_doc=count_dict)

	magnitude_x = get_magnitude(count_dict.values(),0)
	magnitude_y = get_magnitude(count_dict.values(),1)

	product = sum(v[0]*v[1] for v in count_dict.values() if len(v) == 2 )/ (magnitude_x * magnitude_y)
	# print product 
	return  math.acos(product)*(180/math.pi)

def count_string(doc, level,dict_doc=dict()):
	for i in doc:
		try: dict_doc[i]
		except:
			if level == 1 : 
				dict_doc = [None] 
			dict_doc[i]=[]
		try:
			dict_doc[i][level] += 1
		except:
			
			dict_doc[i].append(1)
	return dict_doc


def get_magnitude(my_list,level):
	sum_ = 0 
	for i in my_list :
		try : i[level]
		except:continue
		if i[level]:
			sum_ += i[level]**2
	return math.sqrt(sum_)


doc_x = "hi there it's amr , hi"
doc_y = "hi there it's , hi"
doc_string(doc_x, doc_y)

