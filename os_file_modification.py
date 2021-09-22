import os
import uuid
from os_file_search import getCurrentDirectory

# Create a folder
def createFolder(folderName):
	cur_dir = getCurrentDirectory() + '\\Python Testing\\' + folderName 
	if not os.path.isdir(cur_dir):
		os.makedirs(cur_dir)

#createFolder('Location A')


# Changes folder name from old to new string.  This also works for moving files.
def changeFolderName(oldFolderName, newFolderName):

	cur_dir = getCurrentDirectory() + '\\Python Testing\\' + oldFolderName 
	new_dir = getCurrentDirectory() + '\\Python Testing\\' + newFolderName 
	if os.path.isdir(cur_dir):
		os.rename(cur_dir,new_dir)
		print('Directory renamed from ' + oldFolderName + ' to '+ newFolderName)
	else:
		print('Directory does not exist')

#changeFolderName('Location A','Location B')


# Creates text file in directory
def createTxtFile(folderName, fileName):
	cur_dir = getCurrentDirectory() + '\\Python Testing\\' + folderName 
	txt_dir = getCurrentDirectory() + '\\Python Testing\\' + folderName + '\\' + fileName + ".txt"
	if os.path.isdir(cur_dir):
		textFile = open(txt_dir,'w')

#createTxtFile('Location B','Hello World')
