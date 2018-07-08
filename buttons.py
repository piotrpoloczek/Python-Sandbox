from Tkinter import *

class MyApp:
	def __init__(self, parent):
		
		#------ constants for controlling layout ------
		button_width = 6      ### (1)
		
		button_padx = "2m"    ### (2)
		button_pady = "1m"    ### (2)

		buttons_frame_padx =  "3m"   ### (3)
		buttons_frame_pady =  "2m"   ### (3)		
		buttons_frame_ipadx = "3m"   ### (3)
		buttons_frame_ipady = "1m"   ### (3)
		# -------------- end constants ----------------
		
		self.myParent = parent   
		self.buttons_frame = Frame(parent)
		
		self.buttons_frame.pack(    ### (4)
			ipadx=buttons_frame_ipadx,  ### (3)
			ipady=buttons_frame_ipady,  ### (3)
			padx=buttons_frame_padx,    ### (3)
			pady=buttons_frame_pady,    ### (3)
			)    
		
	
		self.button1 = Button(self.buttons_frame, command=self.button1Click)
		self.button1.configure(text="OK", background= "green")
		self.button1.focus_force()       
		self.button1.configure( 
			width=button_width,  ### (1)
			padx=button_padx,    ### (2) 
			pady=button_pady     ### (2)
			)

		self.button1.pack(side=LEFT)	
		self.button1.bind("<Return>", self.button1Click_a)  
		
		self.button2 = Button(self.buttons_frame, command=self.button2Click)
		self.button2.configure(text="Cancel", background="red")  
		self.button2.configure( 
			width=button_width,  ### (1)
			padx=button_padx,    ### (2) 
			pady=button_pady     ### (2)
			)
	
		self.button2.pack(side=RIGHT)
		self.button2.bind("<Return>", self.button2Click_a)   
		
	def button1Click(self):      
		if self.button1["background"] == "green":  
			self.button1["background"] = "yellow"
		else:
			self.button1["background"] = "green"
	
	def button2Click(self): 
		self.myParent.destroy()     
		
	def button1Click_a(self, event):  
		self.button1Click()
				
	def button2Click_a(self, event): 
		self.button2Click() 
  
	
			
root = Tk()
myapp = MyApp(root)
root.mainloop()
