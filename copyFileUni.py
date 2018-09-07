import shutil
import os

def numberIN(nameOFfile):         # возврат последнего числа заключенного в скобки
	secondParenthesis = nameOFfile.find(")",-5,-4)
	firstParenthesis = nameOFfile.rfind("(")
	number = nameOFfile[firstParenthesis+1:secondParenthesis:]
	if(number.isdigit()):
		return int(number)

#print(numberIN("diplo)(1423)(1)(121235).jpg"))

def uniqueFname(pathOfFile):       #подбор уникального имени с постфиксом
	copy = pathOfFile[:-4:] + "(1).jpg" 
	while(os.path.exists(copy)):
		countSimFile = numberIN(copy) + 1
		copy = pathOfFile[:-4:] + "(" + str(countSimFile) + ").jpg"  
	return copy

def uniqueCopy(src,dst):        # уникальное копирование. если файл с именем не сущ - просто копируй, если сущ подбирай уникальное имя
	if(os.path.exists(dst)):
		dst = uniqueFname(dst)
		shutil.copy2(src,dst)
	else:
		shutil.copy2(src,dst)
		

