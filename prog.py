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

spisok_dan = {1: '<connect1 isInet="1" server="192.168.29.105" port="1792"/><!--ЦА-->',
2: '<connect1 isInet="1" server="192.168.29.104" port="1782"/><!--Брест-->',
3: '<connect1 isInet="1" server="192.168.29.104" port="1789"/><!--Пинск-->',
4: '<connect1 isInet="1" server="192.168.29.104" port="1780"/><!--Гродно-->',
5: '<connect1 isInet="1" server="192.168.29.104" port="1786"/><!--Барановичи-->',
6: '<connect1 isInet="1" server="192.168.29.103" port="1781"/><!--Минск1-->',
7: '<connect1 isInet="1" server="192.168.29.103" port="1791"/><!--Минск2-->',
8: '<connect1 isInet="1" server="192.168.29.103" port="1788"/><!--Солигорск-->',
9: '<connect1 isInet="1" server="192.168.29.103" port="1787"/><!--Новополоцк-->',
10: '<connect1 isInet="1" server="192.168.29.122" port="1785"/><!--Гомель-->',
11: '<connect1 isInet="1" server="192.168.29.122" port="1783"/><!--могилёв-->',
12: '<connect1 isInet="1" server="192.168.29.122" port="1784"/><!--Мозырь-->',
13: '<connect1 isInet="1" server="192.168.29.122" port="1790"/><!--Витебск-->'
    }

print(spisok_dan[your_choice])
    

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

12324
choise = spisok_dan[your_choice]
print(type(choise))
with open("D:\\work\connect.xml", "r", encoding="utf-8") as file3:
	new_file2 = ''
	for line in file3:
		if choise in line:
			new_str = line.replace("connect1","connect")
			new_file2 += new_str
			print("я тут был")
		else:
			new_file2 += line

with open("D:\\work\connect.xml", "w", encoding="utf-8") as file4:
	file4.write(new_file2)


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