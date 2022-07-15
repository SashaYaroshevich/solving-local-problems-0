from tkinter import *
from tkinter import messagebox
from child_window import ChildWindow
from tkinter.scrolledtext import ScrolledText
from tkinter import filedialog as fd
import subprocess


class window:
	def __init__(self, width, height, title="MyWindow", resizable=(False, False), icon="@/home/sasha/projects/certus/solving-local-problems-0/psc.xbm"):
		self.root = Tk()
		self.root.title(title)
		self.root.geometry(f"{width}x{height}+200+200")
		self.root.resizable(resizable[0], resizable[1])
		if icon:
			self.root.iconbitmap(icon)

		self.st = ScrolledText(self.root, width=600, height=600)
		self.label = Label(self.root, text="Сразу выберите файл connect.xml из корня Certus", bg="grey", font="TimesNewRoman 15")
		self.label2 = Label(self.root, text="Далее выберите нужный филиал и нажмите на нужную кнопку", bg="grey", font="TimesNewRoman 15")
		self.button = Button(self.root, text="1--ЦА--", command=self.button_action)
		self.buttonbr = Button(self.root, text="2--Брест-->", command=self.button_actionbr)
		self.buttonpn = Button(self.root, text="3--Пинск-->", command=self.button_actionpn)
		self.buttongr = Button(self.root, text="4--Гродно-->", command=self.button_actiongr)
		self.buttonba = Button(self.root, text="5--Барановичи-->", command=self.button_actionba)
		self.buttonmn1 = Button(self.root, text="6--Минск1-->", command=self.button_actionmn1)
		self.buttonmn2 = Button(self.root, text="7--Минск2-->", command=self.button_actionmn2)
		self.buttonsl = Button(self.root, text="8--Солигорск-->", command=self.button_actionsl)
		self.buttonno = Button(self.root, text="9--Новополоцк-->", command=self.button_actionno)
		self.buttongm = Button(self.root, text="10--Гомель-->", command=self.button_actiongm)
		self.buttonmg = Button(self.root, text="11--могилёв-->", command=self.button_actionmg)
		self.buttonmo = Button(self.root, text="12--Мозырь-->", command=self.button_actionmo)
		self.buttonvt = Button(self.root, text="13--Витебск-->", command=self.button_actionvt)
		self.button2 = Button(self.root, text="Применить", command=self.exit)
		self.button3 = Button(self.root, text="Открыть файл", command=self.open_file)

	def button_action(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.105" port="1792"/><!--ЦА-->'
		print("123")

	def button_actionbr(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.104" port="1782"/><!--Брест-->'

	def button_actionpn(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.104" port="1789"/><!--Пинск-->'

	def button_actiongr(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.104" port="1780"/><!--Гродно-->'

	def button_actionba(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.104" port="1786"/><!--Барановичи-->'

	def button_actionmn1(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.103" port="1781"/><!--Минск1-->'

	def button_actionmn2(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.103" port="1791"/><!--Минск2-->'

	def button_actionsl(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.103" port="1788"/><!--Солигорск-->'

	def button_actionno(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.103" port="1787"/><!--Новополоцк-->'

	def button_actiongm(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.122" port="1785"/><!--Гомель-->'

	def button_actionmg(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.122" port="1783"/><!--могилёв-->'

	def button_actionmo(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.122" port="1784"/><!--Мозырь-->'

	def button_actionvt(self):
		global choise
		choise = '<connect1 isInet="1" server="192.168.29.122" port="1790"/><!--Витебск-->'

	def open_file(self):
		global file_name
		file_name = fd.askopenfilename(initialdir="D:/", title="FIND A FILE", )
		self.st.insert(END, f"путь?: {file_name}\nсодержимое:")
		if file_name:
			with open(file_name, "r") as f:
				self.st.insert(END, f.read())

	def exit(self):
		choice = messagebox.askyesno("Программа закроется и откроется Certus")
		if choice:
			self.root.destroy()

	def run(self):
		self.draw_widgets()
		self.root.mainloop()

	def quit():
		global root
		root.quit()

	def draw_widgets(self):
		self.label.pack()
		self.label2.pack()
		self.button3.pack()
		self.button.pack()
		self.buttonbr.pack()
		self.buttonpn.pack()
		self.buttongr.pack()
		self.buttonba.pack()
		self.buttonmn1.pack()
		self.buttonmn2.pack()
		self.buttonsl.pack()
		self.buttonno.pack()
		self.buttongm.pack()
		self.buttonmg.pack()
		self.buttonmo.pack()
		self.buttonvt.pack()
		self.button2.pack()
		self.st.pack()

	def create_child(self, width, height, title="Child", resizable=(False, False), icon=None):
		ChildWindow(self.root, width, height, title, resizable, icon)


if __name__ == "__main__":
	window = window(800, 800, "Change PS")
	# window.create_child(200, 100)

	
	window.run()


with open(file_name, "r", encoding="utf-8") as file1:
	new_file = ''
	for line in file1:
		if 'connect1' not in line:
			new_str = line.replace("connect","connect1")
			new_file += new_str
		else:
			new_file += line


with open(file_name, "w", encoding="utf-8") as file2:
	file2.write(new_file)


# choise = spisok_dan[your_choice]

with open(file_name, "r", encoding="utf-8") as file3:
	new_file2 = ''
	for line in file3:
		if choise in line:
			new_str = line.replace("connect1","connect")
			new_file2 += new_str
		else:
			new_file2 += line

with open(file_name, "w", encoding="utf-8") as file4:
	file4.write(new_file2)

file_name_new = file_name[0:-11]
file_name_new_2 = file_name_new + 'Certus.exe'
subprocess.Popen(file_name_new_2)