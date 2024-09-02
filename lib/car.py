from vehicle import Vehicle

class Car (Vehicle):
  def go(self):
    return "VRRROOOOOOOOOOOOOOOOOOOOOOOM!!!!!"
  pass

lexus = Car(12, 20)
print(lexus.go())