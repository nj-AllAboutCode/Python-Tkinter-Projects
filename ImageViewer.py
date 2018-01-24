from tkinter import *
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import PIL
from PIL import ImageTk, Image
class application:
	def __init__(self,master):
		self.master = master
		self.c_size = (700,500)
		self.setup_gui(self.c_size)
		self.img=None

	def setup_gui(self,s):
		Label(self.master,text = 'Image Viewer',pady=5,bg='white',
			font=('Ubuntu',30)).pack()
		self.canvas = Canvas(self.master,height=s[1],width=s[0],
			bg='black',bd=10,relief='ridge')
		self.canvas.pack()
		txt = '''
			      !
	  		No Image
		'''
		self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt
			,font=('',30),fill='white')
		f=Frame(self.master,bg='white',padx=10,pady=10)
		Button(f,text='Open New Image',bd=2,fg='white',bg='black',font=('',15)
			,command=self.make_image).pack(side=LEFT)
		f.pack()
		self.status=Label(self.master,text = 'Current Image: None',bg='gray',
			font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
		self.status.pack(side=BOTTOM,fill=X)


	def make_image(self):
		try:
			File = fd.askopenfilename()
			self.pilImage = Image.open(File)
			re=self.pilImage.resize((700,500),Image.ANTIALIAS)
			self.img = ImageTk.PhotoImage(re)
			self.canvas.delete(ALL)
			self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
				anchor=CENTER,image=self.img)
			self.status['text']='Current Image:'+File
		except:
			ms.showerror('Error!','File type is unsupported.')

root=Tk()
root.configure(bg='white')
root.title('Image Viewer')
application(root)
root.resizable(0,0)
root.mainloop()