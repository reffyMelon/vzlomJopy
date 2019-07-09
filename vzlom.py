import os
def vzlom():
	i = 0
	os.mkdir("ВЗЛОМ ЖОПЫ" + str(i))
	if os.mkdir("ВЗЛОМ ЖОПЫ" + str(i)) == 1:
		i += 1
	else:
		os.mkdir("ВЗЛОМ ЖОПЫ" + str(i))
		i += 1
vzlom()
