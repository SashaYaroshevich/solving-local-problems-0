print("""
    <-1-ЦА-->
    <-2-Брест-->
	<-3-Пинск-->
	<-4-Гродно-->
	<-5-Барановичи-->
	<-6-Минск1-->
	<-7-Минск2-->
	<-8-Солигорск-->
	<-9-Новополоцк-->
	<-10-Гомель-->
	<-11-могилёв-->
	<-12--Мозырь-->
	<-13--Витебск--> """)
    
your_choice = int(input('Введите нужный филиал для переключения цифрой выше: '))

spisok_dan = {1: '-1-ЦА--',
2: '-2-Брест--',
3: '-3-Пинск--',
4: '-4-Гродно--',
5: '-5-Барановичи--',
6: '-6-Минск1--',
7: '-7-Минск2--',
8: '-8-Солигорск--',
9: '-9-Новополоцк--',
10: '-10-Гомель--',
11: '-11-могилёв--',
12: '-12--Мозырь--',
13: '-13--Витебск--'
    }

print(spisok_dan[your_choice])
    

# with open("D:\\work\connect.xml", encoding="utf-8") as file:


with open("D:\\work\connect.xml", "r", encoding="utf-8") as file1:
	new_file = ''
	for line in file1:
		if 'connect1' not in line:
			new_str = line.replace("connect","connect1")
			new_file += new_str
		else:
			new_file += line

with open("D:\\work\connect.xml", "w", encoding="utf-8") as file2:
	file2.write(new_file)	
	

# with open("D:\\work\connect.xml", "w", encoding="utf-8") as file:	
# 	for line in x:
# 		if 'connect' in line:
# 			new_str = line.replace("connect","connect1")
# 			file.write(new_str)
# 		else:
# 			file.write(line)
	
# with open("D:\\work\connect.xml", "wt") as file:
#     for line in 
#     x = x.replace("connect","connect1")
# 	fin.write(x)