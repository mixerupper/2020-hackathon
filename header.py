def initialize_data_root(user):
	if user == "AY":
		return("C:/Users/Andrew/Downloads/datathon/data/")
	if user == "MJ":
		return("/Users/Alec/Documents/DSGA_1001_Homework/data/")
	if user == "AH":
		return("")
	if user == "AP":
		return("")
	else:
		return("Manually modify the data_root variable")

def world():
	print("Hello world")
	return()