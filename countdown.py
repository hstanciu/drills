from tkinter import *
import winsound



class Countdown:
  """Countdown component.
  
  Counts from initial seconds (initialTime) to 00:00.
  """

  lbl = None
  frequency = 2500
  duration = 100
  

  def __init__(self, root, initialTime = 900 ):
    """Initializes the Countdown component.
    
    If the Tkinter parent is not passed, an exception will raise.

    Parameters
    ----------
    root : Tk, mandatory
    initialTime : initial time in seconds

    Raises
    ------
    NotImplementedError
      If not Tkinter parent is passed.   
      
    """

    if root is None:
      raise NotImplementedError("The parent component where the Countdown should be deployed is missing in the Countdown constructor.")
    
    self.root = root
    self.remaining_time = initialTime
    self.visible = True


  def time(self): 
    """Time handler; prints the time every second.
       At the last minute makes a beep and changes the color of the 
       background.
       
    """
    if(self.visible == True):
      minAsNo = int(self.remaining_time/60)
      secAsNo = self.remaining_time - minAsNo *60
        
      if(minAsNo == 0 and secAsNo == -1):
        return
        
      sec = str(secAsNo)
      if(len(sec) == 1):
        sec = "0"+sec
    
      min = str(minAsNo)
      if(len(min) == 1):
        if(minAsNo == 1 and secAsNo == 0):
          winsound.Beep(Countdown.frequency, Countdown.duration)
          self.lbl.config(bg="gray")
        min = "0"+min
    
      self.lbl.config(text = str(min)+":"+str(sec))
      if(not(minAsNo == 0 and secAsNo == 0)):
        self.remaining_time = self.remaining_time-1
    
    self.lbl.after(1000, self.time)


  def start(self):
    """Starts the component.
    
    """
    
    self.lbl = Label(  self.root, 
                       font = ('calibri', 10, 'bold'), 
                       background = 'blue', 
                       foreground = 'white'
                     ) 
    self.lbl.grid(row=0,column=5)
    
    self.time()
    
  def setVisibility(self):
      
    self.visible = not self.visible

    
  def get_remaining_time(self):
      
      return self.remaining_time
      


