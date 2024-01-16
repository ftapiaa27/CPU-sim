class Memory():
  def __init__(self) -> None:
    self.registries = [ None for i in range(32)]
  
  def save(self, address, value) -> None:
    if address < 0 or address > 31:
      raise Exception("Failed to save to registry (out of bounds)")
    self.registries[address] = value
  
  def read(self, address) -> int:
    if address < 0 or address > 31:
      raise Exception("Failed to read from registry (out of bounds)")
    return self.registries[address]
  

      
