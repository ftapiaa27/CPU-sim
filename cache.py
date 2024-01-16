from memory import Memory

class Cache():
  def __init__(self) -> None:
    self.memory = Memory()
    self.slots = []

  def read(self, address: int):
    print("Reading from cache...")
    for pair in self.slots:
      if pair[0] == address:
        print("Cache hit!")
        return pair[1]
    print("Cache miss!")  
    value = self.memory.read(address)
    if value is None:
      print("Registry is empty")
      return None
    else:
      self.addToCache(address, value)
      return value

  def write(self, address: int, value: int):
    print('Saving', value, "to register", address)
    for pair in self.slots:
      if pair[0] == address:
        pair[1] = value
        return
    self.addToCache(address, value )

  def addToCache(self, address: int, value: int):
    if len(self.slots) == 8:
      print("Performing write to memory (FIFO from cache)...")
      valueToSave = self.slots.pop(0)
      self.memory.save(valueToSave[0], valueToSave[1])
    print('Updating cache -> address:', address, ', value:', value)
    self.slots.append([address, value])

