class initTest:

   def __init__(self, number):
       self.number = number

   def returnNumber(self):
       return self.number

var = initTest(7)
print(var.returnNumber()) #Prints '7'