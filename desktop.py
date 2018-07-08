#Author Paweł Poloczek
from tkinter import filedialog
from tkinter import *
import re

class GUI(Frame):

    def __init__(self,master):
        Frame.__init__(self, master)
        self.grid()
        master.minsize(width=480, height=320)

        def buttonClick():
            regexForX = re.compile(r'X\D*\d*\W*')
            fileName = filedialog.askopenfilename(filetypes = [("Text files", "*.txt"),("All files", "*.*")])
            #ileContent = open(fileName, 'r')
            #fileContent = open(fileName, 'rb')
            fileContent = open(fileName, 'r', encoding='iso-8859-1')
            fileLines = fileContent.readlines()
            xValues = {}
            
            self.text = Text(master, bg="white", fg="black")
            
            for i, line in enumerate(fileLines):
                if len(line.strip()) == 0 :
                    continue
                
                if 'X' in line:
                    xSearch = regexForX.search(line)
                    searchValue = xSearch.group()
        
                    if len(searchValue.strip()) != 0 :
                        xValues[i] = searchValue.strip()
            
            for key, value in xValues.items():
                self.text.insert(END, "Line: " + str(key) + " Value: "  + value + "\n")
            
            self.text.grid()
            

        self.button = Button(master, text="Select file", command=buttonClick)
        self.button.configure( 
            width = 60,
            padx = 10, 
            pady = 20,
            background = "#73828e",
            activebackground = "#40a5dc"
        )
        self.button.grid()

if __name__ == "__main__":
    tk = Tk()
    tk.wm_title("ArmorLab App")
    guiFrame = GUI(tk)
    guiFrame.mainloop()
