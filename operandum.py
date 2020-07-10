import random

class Operandum:
  """Contains the mathematical part  of the drill.
  """

  def __init__(self, rows_no=5, cols_no=5, operator='*', min=0, max=100):
    """Constructor.

       Builds two arrays of operands based on number of rows and columns, with numbers
       between a min and a max. An operator is defined to calculate using these numbers.
       the correct results are stored in expected_results.
 
    """

    self.rows_no            = rows_no
    self.cols_no            = cols_no
    self.operator           = operator
    self.min                = min
    self.max                = max

    if(self.operator == "*"):
      self.rows = [2, 3, 4, 5, 6, 7, 8, 9]
      random.shuffle(self.rows)
      self.cols               = random.sample(range(100, 999), self.cols_no)
    else:
      #self.rows               = [ random.randint(self.min, self.max) for iter in range(self.rows_no) ]
      #self.cols               = [ random.randint(self.min, self.max) for iter in range(self.cols_no) ]
      self.rows               = random.sample(range(self.min, self.max), self.rows_no)
      self.cols               = random.sample(range(self.min, self.max), self.cols_no)
    self.success            = 0
    self.failure            = 0
    
    
  def get_row_vals(self):
      """Accesses the row generated values.
      
      """
      
      return self.rows
    
    
  def get_col_vals(self):
      """Accesses the col generated values.
      
      """
      
      return self.cols 
      
      
  def get_operator(self):
      """Returns the operator.

      """

      return self.operator 
      
      
  def set_operator(self, operator):
      """Sets the operator.

      """
      self.operator = operator
      

  def operate(self, op1, op2):
      
      if(self.operator == '+'):
        return int(op1)+int(op2)

      if(self.operator == '-'):
        return int(op1)-int(op2)

      if(self.operator == '*'):
        return int(op1)*int(op2)
      