import os
import shutil
from datetime import datetime
import copyFileUni

pathNewDir = "C:\\Users\\Кирилл\\Desktop\\imagesInKirill" 
if not os.path.exists(pathNewDir): # создание папки для фоток
	os.mkdir(pathNewDir)
	os.chdir(pathNewDir)
	fileOfPath = open("fileOFpath.txt", "a") #журнал Исходных местонахождений фоток
	fileOfPath.write("Журнал исходных местонахождений\n")
	fileOfPath.close()
	
	fileOfname = open("fileOFname.txt", "a")  # журнал имен 
	fileOfname.write("Журнал имен\n") 
	fileOfname.close()

	
def select(node):    # Функция по отбору фоток 
	fileOfPath = open("fileOFpath.txt", "a")
	fileOfname = open("fileOFname.txt", "a")
	count = 1;
	
	for paths, dirs, files in os.walk(node):      # Рекурсивный обход по всем котоологам, который возвращает кортеж путей, имен каталогов, имен файлов 
		"""
		print(paths)
		for _dir in dirs:
			print(_dir)
		"""
		
		notAlowedDir = "C:\\Users\\Кирилл\\Desktop\\notAlowedDir"  # блокировка каталога от обхода
		if (paths.startswith(notAlowedDir)):
			continue
		
		if (paths.startswith(pathNewDir)):  # блокировка созданного коталог от обхода
			continue
		
		for _file in files:
			if(_file[-3::] == "jpg"):       # файлы рассширения .jpg
				fullPath = paths+"\\"+_file 
				
				fileOfPath.write(str(count)+". "+fullPath+"\n") #заполнение журналов
				fileOfname.write(str(count)+". "+_file+"\n")
				count += 1
				
				time = os.path.getctime(fullPath)       # считать время создания файла
				fullTime = datetime.fromtimestamp(time).strftime('%Y-%m-%d %H:%M:%S')
				dateTime = fullTime[:10:]
				
				pathDateDir = pathNewDir + "\\" + str(dateTime) # путь к каталогу по имени дата создания файлов
		
				if (not os.path.exists(pathDateDir)): # если каталог не был создан
					os.mkdir(pathDateDir)
					copyFileUni.uniqueCopy(fullPath,pathDateDir +"\\"+ _file)    # копировать уникально (если есть одинаковые именна добавить уникалььный постфикс (число))
				else:
					copyFileUni.uniqueCopy(fullPath,pathDateDir +"\\"+ _file)
	fileOfPath.close()
	fileOfname.close()		


rootNode = "C:\\Users\\Кирилл\\Desktop"  # обход рабочего стола
print("parsing is begining...")
select(rootNode)  # отбор и сортировка
print("parsing is over.")


"""  
dirs = os.listdir(rootNode)
for file in dirs:
	if(file[-3::] == "jpg"):
		shutil.copy(path+"\\"+file, pathNewDir)
		#os.symlink("C:\\Users\\Кирилл\\Desktop"+"\\"+file, pathNewDir+"\\"+file)
"""