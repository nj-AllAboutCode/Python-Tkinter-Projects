from Tkinter import *
import tkColorChooser, tkMessageBox
from tkFileDialog import *
import ScrolledText as sc
from tkfontchooser import askfont

class main:
	def __init__(self,master):
		self.master = master
		self.filename = 'Untitled'
		self.updateTitle()
		self.widgets()
		self.menubar()
	
	def updateTitle(self):
		print self.filename
		self.master.title(self.filename+": "+'DouchePad')	

	def menubar(self):
		self.menu = Menu(root)
		self.master.config(menu=self.menu)
		filemenu = Menu(self.menu)
		self.menu.add_cascade(label="File", menu=filemenu)
		filemenu.add_command(label="New", command=self.NewFile)
		filemenu.add_command(label="Open", command=self.opn)
		filemenu.add_command(label="Save", command=self.save)
		filemenu.add_command(label="Save As..", command=self.saveas)
		filemenu.add_separator()
		filemenu.add_command(label="Exit", command=self.quit)

		Config = Menu(self.menu)
		self.menu.add_cascade(label="Config", menu=Config)
		Config.add_command(label="Font",command=self.chfont)
		Config.add_command(label="Text Color",command=self.txtcolor)
		bt = Menu(Config)
		bt.add_command(label='Black Theme',command=self.black)
		bt.add_command(label='White Theme',command=self.defalut)
		Config.add_cascade(label="Background Theme",menu=bt)
		helpmenu = Menu(self.menu)
		self.menu.add_cascade(label="Help", menu=helpmenu)
		helpmenu.add_command(label="About...", command=self.about)

	def black(self):
		self.ta['insertbackground'] = 'white'
		self.ta['bg'] = 'black'
		self.ta['fg'] = 'white'

	def defalut(self):
		self.ta['insertbackground'] = 'black'
		self.ta['bg'] = 'white'
		self.ta['fg'] = 'black'		

	def quit(self):
		if tkMessageBox.askyesno("Save","Do you want to save the file before closing."):
			self.save()
		quit()
		
	def about(self):
		pass

	def txtcolor(self):
		color = tkColorChooser.askcolor('black')
		if color:
			self.ta['fg'] = color[1]

	def chfont(self):
		font = askfont(self.master)
		if font:
			font['family'] = font['family'].replace(' ', '\ ')
			font_str = "%(family)s %(size)i %(weight)s %(slant)s" % font
			if font['underline']:
				font_str += ' underline'
			if font['overstrike']:
				font_str += ' overstrike'
			self.ta['font'] = font_str

			self.ta['height'] = self.ta['height']-font['size'] 
			self.ta['width'] =  self.ta['width']-font['size']

	def widgets(self):
		self.master.protocol("WM_DELETE_WINDOW",self.quit)
		self.ta = sc.ScrolledText(self.master,height=40,width=100)
		self.ta.pack(expand=True,fill=BOTH)

		self.ta.bind('<Control-o>',self.opn)
		self.ta.bind('<Control-n>',self.NewFile)
		self.ta.bind('<Control-s>',self.save)
		self.ta.bind('<Control-a>',self.select_all)
		self.ta.bind('<Control-A>',self.select_all)

	def NewFile(self,event=None):
		if tkMessageBox.askyesno("New","Do you want to save the file..."):
			self.save()
		
		self.ta.delete(0.0, END)
		self.filename = "Untitled"
		self.updateTitle()

	def select_all(self,event=None):
		self.ta.tag_add(SEL, "1.0", END)
		self.ta.focus_set()
		
	def opn(self,event=None):
		File = str(askopenfilename(title="Open File",filetypes=[("all files","*.*"),
			('CSS','.css'),('HTML','.html'),('PYTHON','.py')]))
		if len(File) > 0:
			self.ta.delete("1.0",END)
			try:
				f = open(File)
				for line in f:
					self.ta.insert(END,line)
				f.close()
				self.filename = str(File)
				self.updateTitle()
			except IOError:
				tkMessageBox.showwarning("Open file","Cannot open this file...") 

	def save(self,event=None):
		if self.filename == 'Untitled':
			self.saveas()
		else:
			f = open(self.filename,"w")
			text = self.ta.get("1.0",END).encode("utf-8")
			f.write(text)
			f.close()
			self.updateTitle()

	def saveas(self,event=None):
		file=str(asksaveasfilename(title="Save as File",defaultextension=".txt",filetypes=[("all files","*.*"),
			('CSS','.css'),('HTML','.html'),('PYTHON','.py')]))
		if len(file)>0:
			f = open(file,'w')
			text = self.ta.get("1.0",END).encode("utf-8")
			f.write(text)
			f.close()
			self.filename = file 
			self.updateTitle()

root = Tk()
main(root)
root.mainloop()
