class Data:
  def PrintMe(self):
    return 'Printed'    
  def __PrintMeNot(self):
    return 'Not Printed'
#Outside class    
DS = Data()
print(DS.PrintMe())
print(DS.__PrintMeNot())