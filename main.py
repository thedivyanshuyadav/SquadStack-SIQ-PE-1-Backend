class ParkingLot:
  """
  A class for parking lot.
  """
  def __init__(self):
    self.lot = {}
    self.slots = {}
    self.available_slots = []
    self.available_count = 0
    self.lot_size = 0
    self.drivers = {}
    self.output_path = 'output.txt'

  def out(self,msg:str):
    """
    A method to save output message to file at output_path.
    Parameters: 
        msg [str]: A output message to be save in output.txt
    """
    with open(self.output_path,'a') as f:
      f.write(msg+'\n')
    
  def Create_parking_lot(self, lot_size:str):
    """
    A method to creates a parking lot with specified lot size.
    Parameters: 
        lot_size [str]: size of parking lot
    """
    self.lot_size = int(lot_size)
    self.available_count = int(lot_size)
    self.available_slots = list(range(1,self.lot_size + 1))[::-1]
    msg = f"Created parking of {self.lot_size} slots"
    self.out(msg)
  
  def Park(self, reg_no:str, _, driver_age:str):
    """
    A method to provide functionality of parking a vehicle.
    Parameters:
      reg_no [str]: registration number of vehicle
      _ [str]: hardcoded value as "driver_age"
      driver_age [str]: the age of the vehicle driver
    """
    if self.available_count == 0:
      self.out("Parking Lot has no space left !")
    else:
      self.available_count -= 1
      assigned_slot = str(self.available_slots.pop(self.available_count))
      self.lot[reg_no] = assigned_slot
      self.slots[assigned_slot] = (reg_no, driver_age)
      if self.drivers.get(driver_age):
        self.drivers[driver_age][assigned_slot] = reg_no
      else:
        self.drivers[driver_age] = {
          assigned_slot : True
        }
      msg = f"Car with vehicle registration number \"{reg_no}\" has been parked at slot number {assigned_slot}"
      self.out(msg)
      
  def Slot_numbers_for_driver_of_age(self, driver_age:str):
    """
    A method to get slot numbers of all vehicles whose driver age is specific.
    Parameters:
      driver_age [str]: the age of the vehicle driver
    """
    msg = ','.join(self.drivers.get(driver_age).keys()) if self.drivers.get(driver_age) else f"No driver found with age={driver_age}"
    self.out(msg)
      
  def Slot_number_for_car_with_number(self, reg_no:str):
    """
    A method to get slot number of the vehicle.
    Parameters:
      reg_no [str]: the registration number of the vehicle
    """
    msg = self.lot.get(reg_no) if self.lot.get(reg_no) else f"No vehicle found with registration number \"{reg_no}\""
    self.out(msg)
    
  def Leave(self, slot_no:str):
    """
    A method to provide leave functionality of parking system.
    Parameters:
      slot_no [str]:  Slot number of the parking lot
    """
    val = self.slots.get(slot_no) if self.slots.get(slot_no) else None
    if val is not None:
      reg_no,driver_age = val
      del self.lot[reg_no]
      del self.slots[slot_no]
      del self.drivers[driver_age][slot_no]
      self.available_count += 1
      self.available_slots.append(slot_no)
      
      msg = f"Slot number {slot_no} vacated, the car with vehicle registration number \"{reg_no}\" left the space, the driver of the car was of age {driver_age}"
      self.out(msg)
    
  def Vehicle_registration_number_for_driver_of_age(self, driver_age:str):
    """
    A method to provide information about the vehicles having driver with specifi age.
    Parameters:
      driver_age [str]:  the age of the vehicle driver
    """
    cars = self.drivers.get(driver_age) if self.drivers.get(driver_age) else None
    if cars:
      msg = ''
      for reg_no,slot_no in cars:
        msg += f"Car with vehicle registration number \"{reg_no}\" has been parked at slot number {slot_no}. "
      self.out(msg)

# Parking Lot
parking_lot = ParkingLot()

# Create or Reset output.txt
with open('output.txt','w+'):pass

# Read commands from input.txt
with open('input.txt','r') as f:
  commands = list(map(lambda line:line.replace('\n',''),f.readlines()))

# Perform operations for each command
for command in commands:
  args = command.split()  # arguments including function name
  fname = args[0]  # Function Name
  function = getattr(parking_lot,fname)  # Get function of Parking Lot
  function(*args[1:])  # Calling function with arguments
  


