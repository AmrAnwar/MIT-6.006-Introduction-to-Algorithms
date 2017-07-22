def fab(num):         
    if num == 1 : return 1
    elif num == 0 : return 0
    return fab(num-1)+fab(num-2)

def fab_memory(num,dict_ = {}):         
    if num == 1 : return 1
    elif num == 0 : return 0
    try:
		dict_['%s'%(num)]
		return dict_['%s'%(num)]
    except:
		dict_['%s'%(num)] = fab_memory(num-1)+fab_memory(num-2)
		return dict_['%s'%(num)]
print fab(10)