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

print(spisok_dan[3])
    

# with open("D:\\work\connect.xml", encoding="utf-8") as file:
with open("D:\\work\connect.xml", "rt") as file:
	x = file.read()
	
with open("D:\\work\connect.xml", "wt") as file:
    x = x.replace("connect","connect1")
	fin.write(x)