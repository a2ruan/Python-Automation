import os

#Get current directory, followed by string manipulation
def getCurrentDirectory():
	cur_dir = os.getcwd()
	cur_dir_tokens = cur_dir.split('\\')
	cur_dir = cur_dir_tokens[0] + '\\' + cur_dir_tokens[1] + '\\' + cur_dir_tokens[2]
	print(cur_dir)
	return cur_dir

#Parse folders for first level items (folders, subfolders)
def getSubfolders(directory):
	files = os.listdir(directory)
	for f in files:
		print(f)

getSubfolders(getCurrentDirectory())
