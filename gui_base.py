from tkinter import *
import winsound
from countdown import *
from operandum import *
import datetime


class GuiBase:
  """Main window."""
  
  
  def __init__(self):
      
    self.rows_no = 8
    self.cols_no = 10
    self.root = Tk()
    self.operandum = Operandum(self.rows_no, self.cols_no)

    
  def start(self):
    """Starts the application.

    """
    self.root.title('Drills') 
    self.bootstrap_ui(self.root)
    self.root.mainloop()
    
  def bootstrap_ui(self, root):
    
    countdown = Countdown(root)
    
    mb =  Menubutton ( root, text = "Settings") 
    mb.menu  =  Menu ( mb, tearoff = 0 ) 
    mb["menu"]  =  mb.menu 
    mb.menu.add_command ( label ='Timer', command = countdown.setVisibility ) 
    submenuOperations = Menu(mb.menu)
    submenuOperations.add_command(label="+", command = lambda: self.set_menu_operator('+'))
    submenuOperations.add_command(label="-", command = lambda: self.set_menu_operator('-'))
    submenuOperations.add_command(label="*", command = lambda: self.set_menu_operator('*') )
    mb.menu.add_cascade(label='Operations', menu=submenuOperations)
    """
    submenuDimensions = Menu(mb.menu)
    submenuDimensions.add_command(label="# rows")
    submenuDimensions.add_command(label="# columns")
    mb.menu.add_cascade(label='Dimensions', menu=submenuDimensions)
    """

    mb.grid(row=0,column=0)
    
    menuAbout =  Menubutton ( root, text = "Help") 
    menuAbout.menu  =  Menu ( menuAbout, tearoff = 0 ) 
    menuAbout["menu"]  =  menuAbout.menu 
    # menuAbout.menu.add_command ( label ='Progress', command = lambda: self.progress_report() )
    #menuAbout.grid(row=0,column=1)
    menuAbout.menu.add_command ( label ='About', command = lambda: self.popupmsg("Drills version 1.0\n Copyrigt  Korwin Software Inc, 2020.\n For Claudia.") )
    menuAbout.grid(row=0,column=1)
    

    countdown.start()

    
    self.lbl =  Label(root,
                      font = ('calibri', 12, 'bold'), 
                      background = 'blue',   
                      foreground = 'white') 
    
    self.lbl.config(text = "  "+self.operandum.get_operator()+"  ")
    self.lbl.grid(row = 1, column = 0)
    
    entriesCols = []
    colsStringVars = []
    global cols_values
    cols_values = self.operandum.get_col_vals()
    for c in range (0, self.operandum.cols_no):
      colVar = StringVar()
      colVar.set(cols_values[c])
      colsStringVars.append(colVar)
      entriesCols.append(Entry(root, width=6, textvariable=colsStringVars[c], bg="lightgrey",
                                           justify='center', state = DISABLED))
      entriesCols[c].grid(row=1,column=c+1)

 
    entriesRows = []
    rowsStringVars = []
    global  rows_values 
    rows_values = self.operandum.get_row_vals()
    for r in range (0, self.operandum.rows_no):
      rowVar = StringVar()
      rowVar.set(rows_values[r])
      rowsStringVars.append(rowVar)        
      entriesRows.append(Entry(root, width=6, textvariable=rowsStringVars[r], bg="lightgrey",
                                           justify='center', state = DISABLED))
      entriesRows[r].grid(row=r+2,column=0)

    entriesResponses = []
    resultStringVars = []
    for r in range (0, self.operandum.rows_no):
      resultStringVars.append([])
      entriesResponses.append([])
      for c in range (0, self.operandum.cols_no):
        resultStringVar = StringVar()
        resultStringVars[r].append(resultStringVar)
        entry = Entry(  
                                           root, 
                                           width = 6, 
                                           textvariable = resultStringVars[r][c]
        )
        """,
                                           validate = 'focusout', 
                                           validatecommand = vcmd
                                         )""" 
        entry.bind("<FocusOut>", self.check_computation)
        entriesResponses[r].append(entry)      
        entriesResponses[r][c].grid(row = r+2,column = c+1)
        
    self.lblSuccess =  Label(root,
                      font = ('calibri', 10, 'bold'), 
                      background = 'Green',   
                      foreground = 'white') 
    
    self.lblSuccess.config(text = " Success: 0 ")
    self.lblSuccess.grid(row = 3, column = self.operandum.cols_no+2)
    
    self.lblFailure =  Label(root,
                      font = ('calibri', 10, 'bold'), 
                      background = 'Red',   
                      foreground = 'white') 
    
    self.lblFailure.config(text = " Failure: 0 ")
    self.lblFailure.grid(row = 4, column = self.operandum.cols_no+2)
    
    button = Button(root, text='Close', command=root.destroy) 
    button.grid(row=self.rows_no+2,column=int((self.cols_no+1)/2))
      

  def check_computation(self,  event):
    """
    """
    entry = event.widget
    row = int(entry.grid_info()['row'])-2
    col = int(entry.grid_info()['column'])-1
    row_op = self.operandum.get_row_vals()[row]
    col_op = self.operandum.get_col_vals()[col]
    result = self.operandum.operate(row_op, col_op)
    if(int(result) != int(entry.get())):
        entry.config({"background" : "pink"})
        self.operandum.failure = self.operandum.failure + 1
        self.lblFailure['text']= ' Failure: '+str(self.operandum.failure)
    else:
        entry.config({"background" : "lightgreen"})
        self.operandum.success = self.operandum.success + 1
        self.lblSuccess['text']= ' Success: '+str(self.operandum.success)
        
        
  def set_menu_operator(self, operator):
      """
      """
      self.operandum = Operandum(self.rows_no, self.cols_no, operator)
      self.operandum.set_operator(operator)
      self.bootstrap_ui(self.root)
      self.lbl.config(text = "  "+self.operandum.get_operator()+"  ")
      
      
  def popupmsg(self, msg):
      
    popup = Tk()
    popup.geometry("250x100")
    popup.wm_title("About")
    label = Label(popup, text=msg)#.grid(0, 1)
    label.pack(side="top", fill="x", pady=10)
    B1 = Button(popup, text="Okay", command = popup.destroy)
    B1.pack()
    popup.mainloop()
    
    
  def progress_report(self):
      
    popup = Tk()
    popup.wm_title("Progress Report")
    dates = ["2020-05-30", "2020-05-31", "2020-06-01"]
    x_values = [datetime.datetime.strptime(d,"%Y-%m-%d").date() for d in dates]

    progress = [35, 37, 39]
    plt.scatter(x_values, progress)
    plt.show()
    #plt.pack()
    
    B1 = Button(popup, text="Close", command = popup.destroy)
    B1.pack()
    popup.mainloop()    