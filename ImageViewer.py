#Created by namah jain From All About Code (youtube channel)
# Channel Link : https://www.youtube.com/channel/UCUGAq4ALoWW4PDU6Cm1riSg?view_as=subscriber
# Simple Image Viewer using tkinter and Python PILLOW library

#Imports
from tkinter import * #download using pip(pip install tkinter) or (in linux) sudo apt-get install python3-tk
from tkinter import filedialog as fd
from tkinter import messagebox as ms
import PIL #pip install pillow
from PIL import ImageTk, Image

# Main Class --Application--
class application:
	#Constructer
	def __init__(self,master):
		#self.master is our root window
		self.master = master
		#Canvas Size
		self.c_size = (700,500)
		#Creates All Of Our Widgets
		self.setup_gui(self.c_size)
		self.img=None

	#Making Widgets
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
		#Text On Canvas Saying No Current Image Open.
		self.wt = self.canvas.create_text(s[0]/2-270,s[1]/2,text=txt
			,font=('',30),fill='white')
		f=Frame(self.master,bg='white',padx=10,pady=10)
		Button(f,text='Open New Image',bd=2,fg='white',bg='black',font=('',15)
			,command=self.make_image).pack(side=LEFT)
		f.pack()
		#Status Bar
		self.status=Label(self.master,text = 'Current Image: None',bg='gray',
			font=('Ubuntu',15),bd=2,fg='black',relief='sunken',anchor=W)
		self.status.pack(side=BOTTOM,fill=X)


	def make_image(self):
		try:
			#Open Image File
			File = fd.askopenfilename()
			self.pilImage = Image.open(File)
			# Resize Image According To Canvas
			re=self.pilImage.resize((700,500),Image.ANTIALIAS)
			self.img = ImageTk.PhotoImage(re)
			# Delete all canvas content(text,image)
			self.canvas.delete(ALL)
			#Create Image
			self.canvas.create_image(self.c_size[0]/2+10,self.c_size[1]/2+10,
				anchor=CENTER,image=self.img)
			# Update Status Bar
			self.status['text']='Current Image:'+File
		except:
			# show error in case of error
			ms.showerror('Error!','File type is unsupported.')

if __name__ == '__main__':
	# Create Object And Run Programme
	root=Tk()
	root.configure(bg='white')
	root.title('Image Viewer')
	application(root)
	root.resizable(0,0)
	root.mainloop()